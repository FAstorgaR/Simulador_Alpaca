# verificador_precio.py
import time
import csv
import datetime
from alpaca_trade_api.rest import REST
from config import API_KEY, API_SECRET, BASE_URL, OBJETIVO_GANANCIA, STOP_LOSS, ARCHIVO_REGISTRO

api = REST(API_KEY, API_SECRET, BASE_URL)

try:
    with open("activo_actual.txt", "r") as f:
        simbolo, precio_compra, hora = f.read().strip().split(",")
        precio_compra = float(precio_compra)
except FileNotFoundError:
    print("⚠️ No se encontró archivo de activo actual.")
    exit()

orden_abierta = api.get_position(simbolo)

if not orden_abierta:
    print("No hay posición activa.")
    exit()

precio_actual = float(api.get_last_trade(simbolo).price)
variacion = (precio_actual - precio_compra) / precio_compra

print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] {simbolo}: {precio_actual:.2f} ({variacion*100:.2f}%)")

motivo = None

if variacion >= OBJETIVO_GANANCIA:
    motivo = "objetivo"
elif variacion <= STOP_LOSS:
    motivo = "stop_loss"

if motivo:
    print(f"💰 Vendiendo {simbolo} por {motivo}")
    api.submit_order(
        symbol=simbolo,
        qty=1,
        side="sell",
        type="market",
        time_in_force="day"
    )
    with open(ARCHIVO_REGISTRO, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([datetime.date.today(), simbolo, precio_compra, precio_actual, f"{variacion*100:.2f}%", motivo])
    import os
    os.remove("activo_actual.txt")
