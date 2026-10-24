# Lab 3 Estructura de un backend

Código base del curso para leer, ejecutar y modificar a mano, sin IA.
Hardware de referencia: NodeMCU ESP8266, DHT11 y LED RGB de cátodo común.
Este proyecto es una propuesta de material base para acompañar la guía.

## Backend en Windows
Desde backend, en una terminal Command Prompt de VS Code:
```
py -m venv .venv
.venv\Scripts\python.exe -m pip install -r requirements.txt
.venv\Scripts\python.exe -m uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```
Swagger: http://127.0.0.1:8000/docs
En macOS/Linux: python3 -m venv .venv y usar .venv/bin/python.
Los cinco endpoints base están en app/routes.py. La lista guarda como máximo
100 lecturas en memoria y se pierde al reiniciar. Ejecutar un solo proceso.
POST /lecturas retorna HTTP 201 con {"lectura": {...}, "led": "apagado"}.
PUT /led acepta rojo, verde, azul o apagado. No hay autenticación:
utilizar únicamente en la red de laboratorio autorizada.

## Firmware
Abrir firmware con PlatformIO IDE en VS Code. Copiar include/config.example.h
a include/config.h y completar WiFi, URL con IPv4 del PC e identificador.
Build, Upload y Monitor a 115200 baudios. El ESP envía cada 5 segundos y aplica
el color devuelto por POST /lecturas; PUT /led se refleja en el próximo envío.
Conexiones y pruebas: ver guía. Las dependencias se descargan la primera vez.
No publicar config.h, contraseñas ni tokens.

## Reto
Implementar GET /lecturas/promedio?n=3 a mano; no se incluye la solución.
Devolver cantidad, temperatura_promedio y humedad_promedio (dos decimales).
Validar n de 1 a 100; sin lecturas responder 404; si hay menos de n, usar todas.

## Antes de la sesión
El docente debe probar el firmware en el hardware real y la red del aula,
precargar las herramientas y validar las dependencias en los equipos.
La guía destina 105 minutos a trabajar con el entorno ya preparado.

## Registro de datos del reto
?n=3, 200, temperatura promedio: 24, humedad promedio: 50
?n=2, 200, temperatura promedio: 26, humedad promedio: 55
?n=5, 200, temperatura promedio: 24, humedad promedio: 50
?n=0, 422, "El parámetro n debe estar entre 1 y 100."
?n=101, 422, "El parámetro n debe estar entre 1 y 100."
?n=n, temperatura promedio: 24, humedad promedio: 50

## Enalce de proyecto wokwi
https://wokwi.com/projects/478331463965868033

## Registro de German Soledispa
Pregunta 1: ¿Qué función recibe el JSON y cuál lo guarda?
La función que recibe el JSON es post_lecturas(), aquí fast API va aconvertir el JSON en un objeto de LecturaEntrada y lo va a validar antes de ejecutar una función de guardado. Posteriormente se ejecuta la función guardar_lecturas(), la cual lo convierte en un diccionario para luego agregarlo a lista de lecturas.
Pregunta 2: ¿Qué archivo cambiarías para añadir una URL?
En la parte de rutas (routes.py) para añadir una URL con decoradores con una nueva función y en la parte de servicios (services.py) para darle la lógica que hay detrás de ser necesario.
Pregunta 3: ¿Qué ocurre con las lecturas y el color cuando se reinicia la API? ¿Por qué?
Al reiniciar la API, así simple viste parece que se mantiene igual, pero lo que ocurre es que vuelven a sus valores por defecto o de inicio.
Pregunta 4: ¿Por qué una petición con JSON bien escrito puede devolver 422? Indica qué archivo define esa validación.
El mensaje de 422 sale cuando los valores que deben cumplir con ciertas reglas y precisamente el valor ingresado no las cumple. Como se puede ver pide un valor menor o igual a 100, este es mayor, por ende, da un error 422.
Pregunta 5: Explica el recorrido completo de una lectura: ESP32 simulado, túnel de VS Code, ruta, modelo, servicio, almacenamiento y respuesta. ¿En qué momento cambia el LED?
Por medio de la ESP32 que se simulo en wokwi, lo que hace es leer el sensor cada 5 segundos, formando un archivo JSON, lo envía por post a la url pública y por medio del túnel que se creó por el puerto 8000, también con el archivo main.py se enruta con la parte de post lectura en nuestra route.py, una vez que está ahí el post, nuestra lectura de entrada se vincula con la parte de validación, en caso de fallar responde con la parte de 422, luego de eso guarda nuestra lectura en la parte de store lecturas en service.py con un máximo de 100 lecturas, por último el ESP32 lee la respuesta del campo led y actualiza el color de led.

