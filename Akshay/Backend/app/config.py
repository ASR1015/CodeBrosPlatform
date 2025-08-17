import os
from pathlib import Path

DATA_DIR = Path(os.getenv("DATA_DIR", "./data"))
CATALOG_DB = os.getenv("CATALOG_DB", "./data/catalog.sqlite")
MARKET_TZ = os.getenv("MARKET_TZ", "Asia/Kolkata")