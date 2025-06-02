# Genetik algoritma

import random
from src.csp import is_valid_route
from src.graph import euclidean_distance


def calculate_fitness(drone, route, no_fly_zones):
    if not is_valid_route(drone, route, no_fly_zones):
        return 0

    total_distance = 0
    current_pos = drone.start_pos

    for delivery in route:
        total_distance += euclidean_distance(current_pos, delivery.pos)
        current_pos = delivery.pos

    # 🔋 BATARYA KONTROLÜ (tek başına güvenlik için tekrar)
    estimated_energy = total_distance * 10
    if estimated_energy > drone.battery:
        return 0

    completed = len(route)
    energy_penalty = total_distance * 0.5

    return completed * 10 - energy_penalty



def generate_random_route(drone, deliveries, no_fly_zones, max_len=5):
    valid_route = []
    candidates = deliveries.copy()
    random.shuffle(candidates)

    for delivery in candidates:
        if delivery.weight > drone.max_weight:
            continue

        trial_route = valid_route + [delivery]
        if is_valid_route(drone, trial_route, no_fly_zones):
            valid_route = trial_route

        if len(valid_route) >= max_len:
            break

    return valid_route


def crossover(route1, route2):
    cut = min(len(route1), len(route2)) // 2
    child = route1[:cut] + route2[cut:]

    # Aynı teslimat tekrar etmesin
    seen = set()
    unique_child = []
    for d in child:
        if d.id not in seen:
            unique_child.append(d)
            seen.add(d.id)

    return unique_child


def mutate(route, deliveries, mutation_rate=0.2):
    if random.random() < mutation_rate and route:
        index = random.randint(0, len(route) - 1)
        replacement = random.choice(deliveries)
        if replacement.id not in [d.id for d in route]:
            route[index] = replacement
    return route


def genetic_algorithm(drone, deliveries, no_fly_zones, generations=30, pop_size=10):
    population = [generate_random_route(drone, deliveries, no_fly_zones) for _ in range(pop_size)]

    for _ in range(generations):
        population.sort(key=lambda route: calculate_fitness(drone, route, no_fly_zones), reverse=True)
        new_population = population[:2]  # En iyi 2 rota korunur (elitizm)

        while len(new_population) < pop_size:
            parent1, parent2 = random.sample(population[:5], 2)  # En iyi 5 rotadan seç
            child = crossover(parent1, parent2)
            child = mutate(child, deliveries)
            if is_valid_route(drone, child, no_fly_zones):
                new_population.append(child)

        population = new_population

    best_route = max(population, key=lambda route: calculate_fitness(drone, route, no_fly_zones))
    return best_route
