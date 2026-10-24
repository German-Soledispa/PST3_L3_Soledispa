from . import store
from .schemas import LecturaEntrada, ComandoLED

def guardar_lectura(datos: LecturaEntrada) -> dict:
    lectura = datos.model_dump()
    store.lecturas.append(lectura)
    # Conservamos como máximo las últimas 100 lecturas recibidas.
    del store.lecturas[:-100]
    return {"lectura": lectura, "led": store.estado_led["color"]}

def listar_lecturas() -> list[dict]:
    return store.lecturas

def consultar_led() -> dict:
    return store.estado_led

def cambiar_led(comando: ComandoLED) -> dict:
    store.estado_led["color"] = comando.color
    return store.estado_led

def promedio(n: int = 3) -> dict:
    suma_temp = sum(lectura["temperatura"] for lectura in store.lecturas[-n:])
    promedio_temp= round(suma_temp / len(store.lecturas[-n:]), 2)
    suma_hum = sum(lectura["humedad"] for lectura in store.lecturas[-n:])
    promedio_hum= round(suma_hum / len(store.lecturas[-n:]), 2)
    return {"promedio temperatura": promedio_temp, "promedio humedad": promedio_hum}
