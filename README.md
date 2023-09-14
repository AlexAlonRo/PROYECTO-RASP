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
| 2  | Sensor de Gas           | Detecta la presencia de gases en el aire y se utiliza para alertar sobre posibles fugas peligrosas, como fugas de gas natural o monóxido de carbono.| ![4](https://github.com/AlexAlonRo/PROYECTO-RASP/assets/97119823/c5c76b99-8083-45b9-b3e6-c879ca8b8263) |$70 | 1        |
| 3  | ESP32                   | Un microcontrolador WiFi y Bluetooth de bajo costo que proporciona conectividad inalámbrica y capacidad de procesamiento para el sistema. Puede usarse para la comunicación y el control remoto.| ![5](https://github.com/AlexAlonRo/PROYECTO-RASP/assets/97119823/4dd19843-7f07-4007-9c4a-b843c400a87e)| $200 | 1        |
| 4  | HC-SR505                | Este sensor de movimiento infrarrojo pasivo detecta el movimiento de objetos en su campo de visión y se utiliza comúnmente en sistemas de seguridad y automatización del hogar.| ![6](https://github.com/AlexAlonRo/PROYECTO-RASP/assets/97119823/271f7242-f660-49a7-8cc7-cf08072b64f6)| $57 | 1        |
| 5  | LED                     | Una fuente de luz que se puede utilizar para indicar el estado del sistema, señalar eventos o proporcionar retroalimentación visual.| ![7](https://github.com/AlexAlonRo/PROYECTO-RASP/assets/97119823/1080ae6c-0ed3-4691-b5fc-c96f3bf4cf8c)| $7 | 2        |
| 6  | Módulo Pulso Cardiaco   |  Este módulo permite medir el ritmo cardíaco de una persona. Puede ser útil para verificar la salud o detectar situaciones de emergencia.| ![8](https://github.com/AlexAlonRo/PROYECTO-RASP/assets/97119823/33ddec7c-292d-4fea-83a9-5fd0a2e22eb7)| $77 | 1        |
| 7  | Módulo HC-SR04          |  Un sensor ultrasónico que mide la distancia al objeto más cercano utilizando ondas ultrasónicas. Puede ser útil para detectar la presencia de personas o objetos cercanos a la puerta.| ![9](https://github.com/AlexAlonRo/PROYECTO-RASP/assets/97119823/7738c7a2-d2e8-4361-9acf-2a3e9b81ad16)| $45 | 1        |
| 8  | Módulo DHT11            | Este sensor de humedad y temperatura mide la temperatura y la humedad relativa en su entorno. Puede proporcionar información sobre las condiciones climáticas internas.| ![10](https://github.com/AlexAlonRo/PROYECTO-RASP/assets/97119823/cb57107a-f3ed-4797-995c-e3bb6c6f3bdc)| $55 | 1        |
| 9  | Pantalla Inteligente LVGL | Una pantalla gráfica que se puede utilizar para mostrar información visual en tiempo real, como datos de sensores, alertas y más.| ![11](https://github.com/AlexAlonRo/PROYECTO-RASP/assets/97119823/59f063c1-92a7-43de-a9fe-600192e6b7a9)| $800 | 1        |
| 10 | Raspberry Pi 4          | Una computadora de placa única con capacidad de procesamiento avanzada que actúa como el cerebro del sistema, gestionando la recopilación de datos y la comunicación con otros dispositivos.| ![12](https://github.com/AlexAlonRo/PROYECTO-RASP/assets/97119823/40bf83f4-a600-4e3c-bdfe-5b4e06589391)| $3,400 | 1        |

## Software
| ID | Nombre del Software | Versión    | Descripción                                      |
|----|---------------------|------------|--------------------------------------------------|
| 1  | Node-Red            | 3.0.2      | Plataforma de programación visual basada en JavaScript para desarrollar aplicaciones IoT. |
| 2  | MicroPython         | 3.11.3     | Un intérprete de Python eficiente diseñado para microcontroladores y sistemas embebidos. |
| 3  | MariaDB             | 9.0.2      | Un sistema de gestión de bases de datos relacional de código abierto, derivado de MySQL. |
| 4  | Raspberry Pi OS     | 11         | Sistema operativo basado en Linux diseñado para la Raspberry Pi, utilizado como plataforma de desarrollo. |
| 5  | MQTT                | 5.0        | Protocolo de mensajería ligero utilizado para la comunicación entre dispositivos IoT. |
| 6  | Arduino             | 2.1.1      | Plataforma de desarrollo de código abierto para microcontroladores que utiliza lenguaje C/C++. |

## Historias de Usuario
| Número de Historia | Descripción de la Historia                                        | Prioridad | Estimación (días) | Cómo Probarlo               | Responsable        |
|-------------------|-----------------------------------------------------------------|-----------|--------------------|-----------------------------|---------------------|
| HU-01             | Como usuario, quiero que el sensor de fotoresistencia detecte cambios de luz para encender automáticamente el LED. | Debe      | 1                  | Verificar si el LED se enciende cuando oscurece. | Alexander Alonso   |
| HU-02             | Como usuario, quiero que el sensor de gas detecte posibles fugas de gas y emita una alarma. | Debe      | 2                  | Comprobar si la alarma suena cuando se detecta gas. | Alexander Alonso   |
| HU-03             | Como usuario, quiero que el sensor de movimiento active una alarma cuando detecte movimiento en la entrada de la casa. | Debe      | 1                  | Verificar si la alarma se activa cuando alguien se acerca a la puerta. | Alexander Alonso   |
| HU-04             | Como usuario, quiero que el ESP32 envíe notificaciones por correo electrónico cuando se detecten problemas. | Puede     | 2                  | Recibir un correo de prueba cuando se activa una alarma. | Andres Arredondo   |
| HU-05             | Como usuario, quiero que la Raspberry Pi 4 almacene registros de eventos de seguridad en una base de datos. | Puede     | 2                  | Comprobar que la base de datos se actualiza con eventos de seguridad. | Andres Arredondo   |
| HU-06             | Como usuario, quiero que la pantalla inteligente LVGL muestre información en tiempo real sobre los sensores. | Puede     | 1                  | Verificar que la información se muestra correctamente en la pantalla. | Andres Arredondo   |
| HU-07             | Como usuario, quiero que el módulo de pulso cardíaco registre y muestre mis niveles de pulso. | Puede     | 2                  | Comprobar que el pulso se muestra en la pantalla. | Jonatan Raciel   |
| HU-08             | Como usuario, quiero que el sensor ultrasónico (HC-SR04) mida la distancia a la puerta. | Quizás    | 1                  | Verificar que la distancia se muestra en la pantalla. | Jonatan Raciel     |
| HU-09             | Como usuario, quiero que el sensor de humedad y temperatura (DHT11) mida las condiciones climáticas internas. | Quizás    | 1                  | Verificar que la temperatura y la humedad se muestran en la pantalla. | Jonatan Raciel    |
| HU-10             | Como usuario, quiero que el buzzer emita un sonido de advertencia cuando se detecten problemas. | Quizás    | 1                  | Comprobar que el buzzer suena durante una alarma. | Samuel Palomino    |
| HU-11             | Como usuario, quiero que el sensor de movimiento adicional se integre al sistema de seguridad. | Quizás    | 1                  | Verificar que el sensor adicional activa la alarma. | Samuel Palomino|
| HU-12             | Como usuario, quiero que el sensor de temperatura controle automáticamente la calefacción en función de la temperatura. | Quizás    | 3                  | Verificar que la calefacción se enciende y apaga según la temperatura. | Samuel Palomino    |
