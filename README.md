# PROYECTO-RASP

# <p align="center">CAJA DE SEGURIDAD</p>

## Objetivo del Proyecto
El proyecto consiste en la creación de un sistema de seguridad y monitoreo para la entrada de una casa, utilizando una variedad de componentes electrónicos. La caja colocada frente a la puerta estará equipada con un sensor de movimiento (HC-SR505) que detectará cualquier movimiento cercano y activará un buzzer para alertar a los residentes. Además, se empleará un sensor de gas para detectar posibles fugas peligrosas y un sensor de temperatura para monitorear las condiciones ambientales. Para un control más avanzado, se integrará un módulo ESP32 que permitirá la conectividad Wi-Fi y envío de alertas a dispositivos móviles. La Raspberry Pi 4 actuará como el cerebro del sistema, gestionando la recopilación de datos y la interfaz de usuario a través de una pantalla inteligente LVGL y un display LCD 128x64. Además, se incorporará un sensor de pulso cardíaco para verificar el estado de salud de los residentes en caso de emergencia. En resumen, el objetivo de este proyecto es crear un sistema de seguridad integral que detecte movimiento, anomalías en la temperatura y la presencia de gas, y proporcione alertas a través de una interfaz amigable, brindando a los residentes una mayor tranquilidad y control sobre su entorno.

## Benficiario
- El beneficiario principal de este proyecto sería la comunidad de personas invidentes. 
## Integrantes del Proyecto
- Alexander Alonso Rodriguez
- Andres Arredondo Escalante
- Victor Manuel Arredondo Morales
- Jonathan Raciel Medina Rivera
- Samuel Palomino Cruz
## Hardware
| ID | Componente             | Descripion            | Imagen   | Costo | Cantidad |
|----|------------------------|-----------------------|----------|-------|-----------
| 1  |Sensor de Fotoresistencia|Este sensor detecta la cantidad de luz ambiental y se utiliza comúnmente para activar o desactivar dispositivos en función de la iluminación en su entorno, como luces automáticas al anochecer.|![3](https://github.com/AlexAlonRo/PROYECTO-RASP/assets/97119823/87c5d7f8-2548-44eb-96b4-5f13165b1482)| $50 | 1        |
| 2  | Sensor de Gas           | |Detecta la presencia de gases en el aire y se utiliza para alertar sobre posibles fugas peligrosas, como fugas de gas natural o monóxido de carbono.| ![4](https://github.com/AlexAlonRo/PROYECTO-RASP/assets/97119823/c5c76b99-8083-45b9-b3e6-c879ca8b8263) |$70 | 1        |
| 3  | ESP32                   | |Un microcontrolador WiFi y Bluetooth de bajo costo que proporciona conectividad inalámbrica y capacidad de procesamiento para el sistema. Puede usarse para la comunicación y el control remoto.| ![5](https://github.com/AlexAlonRo/PROYECTO-RASP/assets/97119823/4dd19843-7f07-4007-9c4a-b843c400a87e)| $200 | 1        |
| 4  | HC-SR505                | |Este sensor de movimiento infrarrojo pasivo detecta el movimiento de objetos en su campo de visión y se utiliza comúnmente en sistemas de seguridad y automatización del hogar.| ![6](https://github.com/AlexAlonRo/PROYECTO-RASP/assets/97119823/271f7242-f660-49a7-8cc7-cf08072b64f6)| $57 | 1        |
| 5  | LED                     | |Una fuente de luz que se puede utilizar para indicar el estado del sistema, señalar eventos o proporcionar retroalimentación visual.| ![7](https://github.com/AlexAlonRo/PROYECTO-RASP/assets/97119823/1080ae6c-0ed3-4691-b5fc-c96f3bf4cf8c)| $7 | 2        |
| 6  | Módulo Pulso Cardiaco   | | Este módulo permite medir el ritmo cardíaco de una persona. Puede ser útil para verificar la salud o detectar situaciones de emergencia.| ![8](https://github.com/AlexAlonRo/PROYECTO-RASP/assets/97119823/33ddec7c-292d-4fea-83a9-5fd0a2e22eb7)| $77 | 1        |
| 7  | Módulo HC-SR04          | | Un sensor ultrasónico que mide la distancia al objeto más cercano utilizando ondas ultrasónicas. Puede ser útil para detectar la presencia de personas o objetos cercanos a la puerta.| ![9](https://github.com/AlexAlonRo/PROYECTO-RASP/assets/97119823/7738c7a2-d2e8-4361-9acf-2a3e9b81ad16)| $45 | 1        |
| 8  | Módulo DHT11            | |Este sensor de humedad y temperatura mide la temperatura y la humedad relativa en su entorno. Puede proporcionar información sobre las condiciones climáticas internas.| ![10](https://github.com/AlexAlonRo/PROYECTO-RASP/assets/97119823/cb57107a-f3ed-4797-995c-e3bb6c6f3bdc)| $55 | 1        |
| 9  | Pantalla Inteligente LVGL | |Una pantalla gráfica que se puede utilizar para mostrar información visual en tiempo real, como datos de sensores, alertas y más.| ![11](https://github.com/AlexAlonRo/PROYECTO-RASP/assets/97119823/59f063c1-92a7-43de-a9fe-600192e6b7a9)| $800 | 1        |
| 10 | Raspberry Pi 4          | |Una computadora de placa única con capacidad de procesamiento avanzada que actúa como el cerebro del sistema, gestionando la recopilación de datos y la comunicación con otros dispositivos.| ![12](https://github.com/AlexAlonRo/PROYECTO-RASP/assets/97119823/40bf83f4-a600-4e3c-bdfe-5b4e06589391)| $3,400 | 1        |
| 12 | Display LCD 128x64      | |Un sensor que mide la temperatura ambiente y puede usarse junto con el módulo DHT11 para obtener mediciones precisas.| ![1](https://github.com/AlexAlonRo/PROYECTO-RASP/assets/97119823/33c41a33-b83f-4e8f-85ce-34502f5caec4)| $90 | 1        |
| 13 | Buzzer                  | |Un dispositivo que emite sonidos audibles y se puede utilizar para alertar a los residentes sobre eventos importantes o situaciones de emergencia.| ![2](https://github.com/AlexAlonRo/PROYECTO-RASP/assets/97119823/2655740d-60d1-4008-a940-0f4c89e8d2ec)| $15 | 1        |
| 14 | Sensor de Movimiento    | |Además del HC-SR505, este componente se refiere a cualquier otro sensor de movimiento que pueda ser necesario para detectar la presencia de personas o movimientos en la entrada de la casa.| ![13](https://github.com/AlexAlonRo/PROYECTO-RASP/assets/97119823/513580f6-a423-4156-af56-72afce1f6f6b)| $67 | 1        |
