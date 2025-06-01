# matplotlib ile rota çizimi

import matplotlib.pyplot as plt
from matplotlib.patches import Polygon


def plot_route(drone, route, no_fly_zones=None):
    # Rota çizimi
    x = [drone.start_pos[0]] + [d.pos[0] for d in route]
    y = [drone.start_pos[1]] + [d.pos[1] for d in route]

    plt.plot(x, y, marker='o', label=f"Drone {drone.id}")

    # Başlangıç noktası
    plt.scatter(*drone.start_pos, color='green', label='Başlangıç')

    # Teslimat noktaları
    for d in route:
        plt.scatter(*d.pos, color='blue')
        plt.text(d.pos[0]+0.5, d.pos[1]+0.5, f"{d.id}", fontsize=8)

    # No-fly zone çizimi
    if no_fly_zones:
        for zone in no_fly_zones:
            poly = Polygon(zone.coordinates, closed=True, color='red', alpha=0.3, label='No-Fly Zone')
            plt.gca().add_patch(poly)

    plt.title(f"Drone {drone.id} Rota Haritası")
    plt.xlabel("X Koordinatı")
    plt.ylabel("Y Koordinatı")
    plt.grid(True)
    plt.legend()
    plt.axis("equal")
    plt.show()
