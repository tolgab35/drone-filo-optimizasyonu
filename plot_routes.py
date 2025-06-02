import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import os
from datetime import datetime

def plot_route_and_save(drone, route, no_fly_zones=None, filename_prefix="drone_rota"):
    x = [drone.start_pos[0]] + [d.pos[0] for d in route]
    y = [drone.start_pos[1]] + [d.pos[1] for d in route]

    plt.figure()
    plt.plot(x, y, marker='o', label=f"Drone {drone.id}")
    plt.scatter(*drone.start_pos, color='green', label='Başlangıç')

    for d in route:
        plt.scatter(*d.pos, color='blue')
        plt.text(d.pos[0]+0.5, d.pos[1]+0.5, f"{d.id}", fontsize=8)

    if no_fly_zones:
        for zone in no_fly_zones:
            poly = Polygon(zone.coordinates, closed=True, color='red', alpha=0.3)
            plt.gca().add_patch(poly)

    plt.title(f"Drone {drone.id} Rota Haritası")
    plt.xlabel("X Koordinatı")
    plt.ylabel("Y Koordinatı")
    plt.grid(True)
    plt.legend()
    plt.axis("equal")

    # 📁 Klasör oluştur (yoksa)
    folder = "sonuclar"
    os.makedirs(folder, exist_ok=True)

    # 🕒 Zaman damgalı dosya ismi
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{filename_prefix}_drone{drone.id}_{timestamp}.png"
    filepath = os.path.join(folder, filename)

    # 💾 Görseli kaydet
    plt.savefig(filepath, dpi=300)
    plt.close()
