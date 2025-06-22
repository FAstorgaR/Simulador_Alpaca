# estrategia_diaria.py
import datetime
from alpaca_trade_api.rest import REST
from config import API_KEY, API_SECRET, BASE_URL

api = REST(API_KEY, API_SECRET, BASE_URL)

# Lista de acciones baratas para probar (puedes mejorar esto con scrapers después)
acciones_prueba = ["CEI", "SYTA", "BBBYQ", "TELL", "GROM"]

for simbolo in acciones_prueba:
    bars = api.get_bars(simbolo, "5Min", limit=3).df
    if len(bars) < 3:
        continue

    precio_inicio = bars.iloc[0]["open"]
    precio_ahora = bars.iloc[-1]["close"]
    variacion = (precio_ahora - precio_inicio) / precio_inicio

    if variacion >= 0.03:
        print(f"Comprando {simbolo} (+{variacion*100:.2f}%)")
        orden = api.submit_order(
            symbol=simbolo,
            qty=1,
            side="buy",
            type="market",
            time_in_force="day"
        )
        with open("activo_actual.txt", "w") as f:
            f.write(f"{simbolo},{precio_ahora},{datetime.datetime.now()}")
        break
