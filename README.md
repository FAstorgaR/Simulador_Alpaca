# 🤖 Automatización de Trading con Alpaca (Python 🇨🇱)

Este proyecto permite automatizar una estrategia de trading básica usando la API de [Alpaca](https://alpaca.markets/) desde Chile, con Python.  
Incluye una estrategia de compra/venta, un monitor que revisa el mercado cada 5 minutos y un sistema de registro diario en CSV.

---

## 📁 Estructura del Proyecto

```
.
├── estrategia.py         # Aplica la estrategia de inversión (ej. compra o venta según condiciones)
├── monitor.py            # Verifica el precio cada 5 minutos y guarda datos en memoria
├── registro_diario.py    # Al final del día, guarda los datos acumulados en un archivo CSV
├── config.py             # Contiene las llaves de API y configuración general
├── requirements.txt      # Lista de dependencias
└── README.md             # Este documento
```

---

## ⚙️ Requisitos

- Python 3.9 o superior
- Cuenta en [Alpaca Markets](https://alpaca.markets/)
- Claves API (Paper Trading)
- Librerías necesarias:

```bash
pip install -r requirements.txt
```

---

## 🔐 Configuración (config.py)

Crea un archivo `config.py` con este contenido:

```python
API_KEY = "TU_API_KEY"
SECRET_KEY = "TU_SECRET_KEY"
BASE_URL = "https://paper-api.alpaca.markets"
SYMBOL = "AAPL"  # Puedes cambiarlo por otro como "TSLA", "GLD", etc.
```

> ⚠️ Asegúrate de **agregar `config.py` al `.gitignore`** para no subir tus llaves a GitHub.

---

## 🚦 Scripts y Uso

### `estrategia.py`

Ejecuta una lógica simple de trading (por ejemplo: compra si el precio baja un 2%, vende si sube un 3%).

**Uso:**

```bash
python estrategia.py
```

**Frecuencia sugerida:**  
- 1 a 2 veces al día (por ejemplo: apertura y cierre del mercado)

---

### `monitor.py`

Revisa el precio del activo cada 5 minutos y guarda los datos en una lista temporal para luego analizarlos o exportarlos.

**Uso:**

```bash
python monitor.py
```

**Frecuencia sugerida:**  
- Loop continuo durante el horario del mercado (9:30 a 16:00 hora NY)

---

### `registro_diario.py`

Guarda un resumen diario en un archivo `.csv`, incluyendo precios observados, decisiones tomadas y resultados.

**Uso:**

```bash
python registro_diario.py
```

**Frecuencia sugerida:**  
- 1 vez al día, después del cierre del mercado (ej: 16:30 NY / 17:30 CL)

---

## 📅 Ejecución Diaria Recomendada

| Script              | Frecuencia     | Horario sugerido        |
|---------------------|----------------|--------------------------|
| estrategia.py       | 1-2 veces/día  | Mañana y/o tarde         |
| monitor.py          | Continuo       | 9:30 a 16:00 (NY)        |
| registro_diario.py  | 1 vez/día      | 16:30 (NY) / 17:30 (CL)  |

---

## 💡 Recomendaciones

- Usa la cuenta de **Paper Trading** para pruebas.
- Automatiza con `cron`, `Task Scheduler`, o servicios en la nube.
- Protege tus claves API y evita subirlas a GitHub.

---

## 📊 Resultados

Los registros diarios se almacenan como `registro_YYYY-MM-DD.csv` y pueden analizarse con Excel, Python o Jupyter.

---

## 📝 Licencia

MIT License.

---

## 📬 Contacto

Este proyecto fue creado como base para automatizar inversiones desde Chile usando Python. Puedes crear un issue o pull request en GitHub si tienes sugerencias.
