from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

DB_FILE = "wins.txt"

def get_wins():
    if not os.path.exists(DB_FILE):
        with open(DB_FILE, "w") as f:
            f.write("0")
        return 0
    try:
        with open(DB_FILE, "r") as f:
            content = f.read().strip()
            return int(content) if content else 0
    except ValueError:
        return 0

def save_wins(count):
    with open(DB_FILE, "w") as f:
        f.write(str(count))

@app.get("/api/wins")
async def get_total_wins():
    return {"value": get_wins()}

@app.post("/api/hit")
async def increment_wins():
    current = get_wins()
    new_count = current + 1
    save_wins(new_count)
    return {"value": new_count}

# VAŽNO: Provjeri postoji li mapa 'static' prije pokretanja da izbjegneš Error
if not os.path.exists("static"):
    os.makedirs("static")

app.mount("/", StaticFiles(directory="static", html=True), name="static")
