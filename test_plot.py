from src.utils import load_data_from_txt
from src.ga import genetic_algorithm
from visualization.plot_routes import plot_route

# Veriyi yükle
drones, deliveries, no_fly_zones = load_data_from_txt("data/veri_seti.txt")

# Örnek olarak ilk drone için en iyi rota
route = genetic_algorithm(drones[0], deliveries, no_fly_zones)

# Rota görselleştir
plot_route(drones[0], route, no_fly_zones)
