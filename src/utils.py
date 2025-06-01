# Yardımcı fonksiyonlar (mesafe, zaman vs.)

import ast
from src.models import Drone, Delivery, NoFlyZone

def load_data_from_txt(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    # drones, deliveries, no_fly_zones ifadelerini güvenli şekilde parse et
    namespace = {}
    exec(content, {}, namespace)

    drones_raw = namespace.get("drones", [])
    deliveries_raw = namespace.get("deliveries", [])
    no_fly_zones_raw = namespace.get("no_fly_zones", [])

    # Nesneye çevir
    drones = [Drone(**d) for d in drones_raw]
    deliveries = [Delivery(**d) for d in deliveries_raw]
    no_fly_zones = [NoFlyZone(**z) for z in no_fly_zones_raw]

    return drones, deliveries, no_fly_zones
