import json, time, uuid, random
from pathlib import Path
from datetime import datetime

BASE = Path("data/input")
BASE.mkdir(parents=True, exist_ok=True)

drinks = [
    ("Espresso", 2.20),
    ("Americano", 2.80),
    ("Cappuccino", 3.20),
    ("Latte", 3.40),
    ("Flat White", 3.60),
    ("Mocha", 3.80),
    ("Macchiato", 2.60),
    ("Cold Brew", 3.90),
    ("Iced Latte", 3.60),
]

def price_with_size(base, size):
    mult = 1.0 if size=="S" else (1.3 if size=="M" else 1.6)
    return round(base * mult, 2)

while True:
    rows = []
    for _ in range(random.randint(5, 10)):
        drink, base = random.choice(drinks)
        size = random.choice(["S", "M", "L"])
        qty = random.randint(1, 2)
        rows.append({
            "order_id": str(uuid.uuid4()),
            "drink": drink,
            "size": size,
            "quantity": qty,
            "unit_price": price_with_size(base, size),
            "event_time": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")  # UTC
        })
    out = BASE / f"batch_{int(time.time())}.json"
    with out.open("w", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    print(f"Wrote {out} ({len(rows)} orders)")
    time.sleep(3)
