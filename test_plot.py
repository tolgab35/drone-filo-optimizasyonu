from src.utils import load_data_from_txt
from src.ga import genetic_algorithm
from src.astar import a_star
from visualization.plot_routes import plot_route_and_save

# Veriyi yükle
drones, deliveries, no_fly_zones = load_data_from_txt("data/veri_seti.txt")

# GA ile rota üret ve kaydet
ga_route = genetic_algorithm(drones[0], deliveries, no_fly_zones)
plot_route_and_save(drones[0], ga_route, no_fly_zones, filename_prefix="ga")

# A* ile rota üret ve kaydet
path, _ = a_star(drones[0], deliveries[1], no_fly_zones)
plot_route_and_save(drones[0], [deliveries[1]], no_fly_zones, filename_prefix="astar")
