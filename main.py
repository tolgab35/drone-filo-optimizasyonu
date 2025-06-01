# Ana çalıştırılabilir dosya

from src.utils import load_data_from_txt
from src.astar import a_star
from src.ga import genetic_algorithm
from src.csp import is_valid_route


def run_astar(drones, deliveries, no_fly_zones):
    print("\n--- A* ALGORİTMASI ---")
    for drone in drones:
        for delivery in deliveries:
            path, cost = a_star(drone, delivery, no_fly_zones, current_time=10)
            if path and is_valid_route(drone, [delivery], no_fly_zones, start_time=10):
                print(f"\nDrone {drone.id} → Teslimat {delivery.id}")
                print(f"  Maliyet: {cost:.2f}")
                print(f"  Rota: {path}")
                break


def run_ga(drones, deliveries, no_fly_zones):
    print("\n--- GENETİK ALGORİTMA ---")
    for drone in drones:
        best_route = genetic_algorithm(drone, deliveries, no_fly_zones)
        print(f"\nDrone {drone.id} için en iyi rota:")
        for d in best_route:
            print(f"  Teslimat ID: {d.id} - Konum: {d.pos} - Öncelik: {d.priority}")


def main():
    drones, deliveries, no_fly_zones = load_data_from_txt("data/veri_seti.txt")

    print("Hangi algoritmayı çalıştırmak istersin?")
    print("1. A* Algoritması")
    print("2. Genetik Algoritma")
    choice = input("Seçimin (1/2): ")

    if choice == "1":
        run_astar(drones, deliveries, no_fly_zones)
    elif choice == "2":
        run_ga(drones, deliveries, no_fly_zones)
    else:
        print("Geçersiz seçim.")


if __name__ == "__main__":
    main()
