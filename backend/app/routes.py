from fastapi import APIRouter, HTTPException, Query
from .schemas import LecturaEntrada, ComandoLED
from . import services, store

router = APIRouter()

@router.get("/salud")
def salud():
    return {"estado": "ok", "laboratorio":3}

@router.get("/lecturas")
def get_lecturas():
    return services.listar_lecturas()

@router.get("/lecturas/promedio", status_code = 200)
def get_promedio(n:int = Query(3)):
    if n < 1 or n > 100:
        raise HTTPException(status_code = 422, detail = "El parámetro n debe estar entre 1 y 100.")
    if not store.lecturas:
        raise HTTPException(status_code = 404, detail = "No hay lecturas registradas para calcular el promedio.")
    return services.promedio(n)

@router.post("/lecturas", status_code=201)
def post_lectura(datos: LecturaEntrada):
    return services.guardar_lectura(datos)

@router.get("/led")
def get_led():
    return services.consultar_led()

@router.put("/led")
def put_led(comando: ComandoLED):
    return services.cambiar_led(comando)
