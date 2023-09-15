import machine
import utime
import ssd1306
import dht

############################################################################################3
import network
from umqtt.simple import MQTTClient
import ubinascii

# Credenciales de WiFi
ssid = 'ElBocchitoUwU'#'Fam.Medina'
password = 'andresxd'#'1612ANIo435'

# Configuración del servidor MQTT
mqtt_server = '192.168.167.188'
client_id = ubinascii.hexlify(machine.unique_id())
topic_pub = b'gorra'

# Inicializar la conexión WiFi
station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(ssid, password)

while not station.isconnected():
    pass

print('Conexión exitosa')
print(station.ifconfig())

# Conectarse al broker MQTT
try:
    client = MQTTClient(client_id, mqtt_server)
    client.connect()
    print('Conectado al broker MQTT en %s' % mqtt_server)
except OSError as e:
    print('Error al conectar al broker MQTT.')

# Función para enviar un mensaje MQTT
def enviar_mensaje(msg):
    global client
    try:
        client.publish(topic_pub, msg)
    except:
        print("Error al enviar mensaje MQTT")
#############################################################################################

# Configura el pin GPIO al que está conectado el sensor infrarrojo
sensor_pin = machine.Pin(4, machine.Pin.IN)

# Configura el primer pin GPIO al que está conectado el botón
boton_pin1 = machine.Pin(5, machine.Pin.IN, machine.Pin.PULL_UP)

estado_boton1 = False
estado_anterior_boton1 = False

# Configura el segundo pin GPIO al que está conectado el botón
boton_pin2 = machine.Pin(16, machine.Pin.IN, machine.Pin.PULL_UP)

estado_boton2 = False
estado_anterior_boton2 = False

# Configura el pin GPIO (D34) como entrada analógica
potenciometro_pin = machine.ADC(machine.Pin(34))

# Configura el pin GPIO para el buzzer (D19) como salida
buzzer_pin = machine.Pin(19, machine.Pin.OUT)
pwm = machine.PWM(buzzer_pin)

# Configura el pin GPIO al que está conectado el sensor de movimiento (PIR) en D35
pir_pin = machine.Pin(35, machine.Pin.IN)

# Configura el pin D32 como una salida digital
led_pin = machine.Pin(32, machine.Pin.OUT)

# Configura la pantalla OLED
i2c = machine.I2C(-1, scl=machine.Pin(21), sda=machine.Pin(22))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

# Configura el pin GPIO al que está conectado el sensor DHT11
pin = machine.Pin(33, machine.Pin.IN)  # Cambia el número del pin según tu conexión
# Crea un objeto DHT para interactuar con el sensor
dht_sensor = dht.DHT11(pin)



# Función para cambiar el estado del botón
def toggle_button_state():
    global button_state, prev_button_value
    
    button_value = boton_pin1.value()  # Leer el valor del botón
    
    if button_value != prev_button_value:
        prev_button_value = button_value
        
        if button_value == 0:  # Si el botón se ha presionado
            if button_state == 0:
                button_state = 1
                return 1
            else:
                button_state = 0
                return 0


# Función para manejar el botón y actualizar la variable global
def check_button():
    global global_button_value, previous_button_state
    button_value = boton_pin1.value()
    
    if button_value == 0 and previous_button_state == 1:
        global_button_value = 1 - global_button_value  # Alterna entre 0 y 1
        previous_button_state = 0
    elif button_value == 1:
        previous_button_state = 1
        
button_state = 1  # Estado inicial del botón (suelto)
prev_button_value = 1  # Valor previo del botón
global_button_value = 0  # Estado inicial (suelto)
previous_button_state = 1  # Estado inicial (suelto)  
previous_state = None  # Estado previo del botón (inicialmente desconocido)
  

volume_config = 20



# Función para cambiar el estado del botón
def toggle_button_state2():
    global button_state, prev_button_value
    
    button_value = boton_pin2.value()  # Leer el valor del botón
    
    if button_value != prev_button_value:
        prev_button_value = button_value
        
        if button_value == 0:  # Si el botón se ha presionado
            if button_state == 0:
                button_state = 1
                return 1
            else:
                button_state = 0
                return 0
# Función para manejar el botón y actualizar la variable global
def check_button2():
    global global_button_value2, previous_button_state2
    button_value = boton_pin2.value()
    
    if button_value == 0 and previous_button_state2 == 1:
        global_button_value2 = 1 - global_button_value2  # Alterna entre 0 y 1
        previous_button_state2 = 0
    elif button_value == 1:
        previous_button_state2 = 1
        
button_state2 = 1  # Estado inicial del botón (suelto)
prev_button_value2 = 1  # Valor previo del botón
global_button_value2 = 0  # Estado inicial (suelto)
previous_button_state2 = 1  # Estado inicial (suelto)  
previous_state2 = None  # Estado previo del botón (inicialmente desconocido)



# Función para mapear valores para el ajuste de volumen
def map_value(value, in_min, in_max, out_min, out_max):
    return int((value - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

def adjust_volume():
    # Configurar el potenciómetro en el pin 34
    conversor = machine.ADC(machine.Pin(34))
    pot_value = conversor.read()  # Leer el valor del potenciómetro
    print("Potenciometro:", pot_value)
    pot_value = map_value(pot_value, 0, 1023, 0, 100)  # Mapear el valor a un rango de 0 a 100
    print("Volumen ajustado:", pot_value)
    return pot_value

# Función para activar el buzzer
def activate_buzzer(pot_value):
    pwm.duty(pot_value)  # Establecer el ciclo de trabajo del PWM
    pwm.freq(1000)  # Establecer la frecuencia a 1000 Hz (ajusta según sea necesario)

# Función para desactivar el buzzer
def deactivate_buzzer():
    pwm.duty(0)  # Apagar el buzzer
    
    

# Función para leer y mostrar la temperatura y la humedad
def read_dht11():
    try:
        dht_sensor.measure()  # Realiza una medición
        temperatura = dht_sensor.temperature()
        humedad = dht_sensor.humidity()
        print("Temperatura: {:.2f}°C".format(temperatura))
        print("Humedad: {:.2f}%".format(humedad))
    except Exception as e:
        print("Error al leer el sensor DHT11:", e)
    

try:

    while True:
        # Lee el estado del sensor infrarrojo
        estado_sensor = sensor_pin.value()
    
        #Sensor de temperatura
        dht_sensor.measure()  # Realiza una medición
        temperatura = dht_sensor.temperature()
        humedad = dht_sensor.humidity()
    
        check_button()
        state_changed = toggle_button_state()  # Llamamos a la función y guardamos el resultado

        if state_changed is not None:  # Si el resultado no es None, lo imprimimos
            if state_changed != previous_state:  # Solo imprimimos si ha habido un cambio
                print(state_changed)
                previous_state = state_changed  # Actualizamos el estado previo


        check_button2()
        state_changed2 = toggle_button_state2()  # Llamamos a la función y guardamos el resultado
        if state_changed2 is not None:  # Si el resultado no es None, lo imprimimos
            if state_changed2 != previous_state2:  # Solo imprimimos si ha habido un cambio
                print(state_changed2)
                previous_state2 = state_changed2  # Actualizamos el estado previo
            
            
        # Lee el valor analógico del potenciómetro
        valor_potenciometro = potenciometro_pin.read()
    
        # Lee el estado del sensor de movimiento
        movimiento_detectado = pir_pin.value()
    

        # Borra la pantalla
        oled.fill(0)
        print("B 1",previous_state)
        print("B 2",previous_state2)
        if(previous_state == 0):
            print("funciona")
            oled.text("Bienvenido:", 0, 10)
            if(movimiento_detectado == 1 and estado_sensor == 0):
                oled.text("Obstáculo detectado", 0, 30)
                led_pin.on()
                activate_buzzer(volume_config)
            else:
                if(estado_sensor == 1):
                    oled.text("Bienvenido:", 0, 10)
                    oled.text("No hay obstáculo", 0, 30)
                    led_pin.off()
                    deactivate_buzzer()
        else:
            print("Apagado")
            led_pin.off()
            deactivate_buzzer()
            if(previous_state2 == 0):
                oled.fill(0)
                print("Modo Volumen")
                oled.text("VOLUMEN:", 0, 32)
                pot_value = adjust_volume()
                volume_config = pot_value
                activate_buzzer(pot_value)
                utime.sleep(1)
                deactivate_buzzer()
                oled.text(str(valor_potenciometro), 0, 40)
            else:
                oled.fill(0)
                oled.text("Bienvenido:", 0, 10)
    
    
        #enviar_mensaje(mensaje)
        enviar_mensaje("{" + str(estado_sensor) + "," + str(movimiento_detectado) + "," + str(previous_state) + "," + str(previous_state2) + "," + str(valor_potenciometro) + "," + str(temperatura) + "," + str(humedad) +"}")
    
        # Actualiza la pantalla OLED
        oled.show()
    
        # Espera 1 segundo antes de realizar la siguiente lectura
        utime.sleep(1)
except Exception as e:
    print("Error al enviar mensaje MQTT:", e)

time.sleep(0.1)