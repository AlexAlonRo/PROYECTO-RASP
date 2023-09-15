from machine import Pin, ADC
from time import sleep
from hcsr04 import HCSR04
import time
from umqtt.simple import MQTTClient
import network

#HAcemos las configuraciones de MQTT
MQTT_BROKER = "192.168.167.188"
MQTT_USER = "gorra"
MQTT_PASSWORD = "1234"
MQTT_CLIENT_ID = ""
MQTT_PORT = 1883

# Configuración del sensor de ultrasonido HC-SR04
pir_pin = Pin(2, Pin.IN)
sensor = HCSR04(trigger_pin=5, echo_pin=4)

# Configuración del sensor de pulso
ppg_pin = Pin(33, Pin.IN)
ppg_pin.atten(ADC.ATTN_11DB)
ppg_pin.width(ADC.WIDTH_10BIT)
# Pin donde está conectado el sensor LM35
lm35_pin = ADC(Pin(34))
lm35_pin.atten(ADC.ATTN_11DB)

# #Funcion para conectar a la Red Wifi
def wifi_connect():
    print ("Conectando...", end = "")

    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    sta_if.connect('ElBocchitoUwU','andresxd')

    while not sta_if.isconnected():
        print(".", end="")
        sleep(0.3)
    print("Wifi Conectado!")

# Funcion de Publicador de MQTT
def publish (topico, estado):
    client = MQTTClient(MQTT_CLIENT_ID, MQTT_BROKER, port=MQTT_PORT, user=MQTT_USER, password=MQTT_PASSWORD, keepalive=30)
    client.connect()
    print("[OK]")
    client.publish(topico, str(estado))
    print("Publicando estado: ", estado,"   ",topico)

  
wifi_connect()


def leer_bpm():
    # Lee el valor analógico del sensor
    valor_analogico = ppg_pin.read()

    # Realiza el cálculo para convertir el valor en BPM
    # Esta es una fórmula genérica y puede variar según el sensor específico que estés utilizando
    # Debes consultar la documentación de tu sensor para obtener la fórmula correcta
    # Aquí asumimos que el sensor produce una salida lineal en función de la frecuencia cardíaca.
    # Si tu sensor proporciona una salida diferente, debes ajustar la fórmula en consecuencia.
    bpm = valor_analogico  # Esta es una fórmula simplificada, ajusta según la calibración de tu sensor

    return bpm

#Funcion para calcular el ritmo cardiaco
def calcular_pulso(ppg_values):
    return sum(ppg_values)/len(ppg_values)

# Función de detección de movimiento
def deteccion_movimiento():
    distancia = sensor.distance_cm()
    if pir_pin.value() == 1:
        if 1 < distancia <= 50:
            #print("¡Movimiento detectado a {:.2f} cm!".format(distancia))
            return distancia;
    else:
        #print("Sin Movimiento")
        return ;


def read_lm35_temperature():
    # Lee el valor analógico del sensor LM35
    raw_value = lm35_pin.read()
    # Convierte el valor analógico a temperatura en grados Celsius
    temperature_c = (raw_value * 3.3 / 4095 )*100
    return temperature_c

try:
    while True:
        ppg_values=[]
        
        #Verifica el movimiento
        movimiento = deteccion_movimiento();
        #print(deteccion_movimiento())
        pulso = calcular_pulso(ppg_values)
        print("Pulso: {}".format(pulso))
        if(movimiento):
            #Lee valores de la temperatura
            temperature = read_lm35_temperature()
            if (temperature > 33 and temperature < 40):
                publish("sensor/temperatura",temperature)
                print("Temperatura: {:.2f} °C".format(temperature))
        
            
            bpm = leer_bpm()
            # Lee valores PPG durante un período de tiempo
            start_time = time.ticks_ms()
            while time.ticks_diff(time.ticks_ms(), start_time) < 3000:  # Lee durante 3 segundos
                ppg_values.append(bpm)
                time.sleep_ms(5)  # Frecuencia de muestreo de 200 Hz

            # Calcula el pulso a partir de los valores PPG
            pulso = calcular_pulso(ppg_values)
            if 30 < pulso < 150:
                print("Pulso: {}".format(pulso))
                publish("sensor/cardio",pulso)
                
        sleep(1)
        
except KeyboardInterrupt:
    pass