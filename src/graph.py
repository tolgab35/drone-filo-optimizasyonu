# Graf yapısı ve maliyet hesaplama

import math

def euclidean_distance(pos1, pos2):
    return math.sqrt((pos1[0] - pos2[0])**2 + (pos1[1] - pos2[1])**2)

def calculate_cost(drone, delivery):
    distance = euclidean_distance(drone.start_pos, delivery.pos)
    cost = distance * delivery.weight + (delivery.priority * 100)
    return cost

def build_graph(drones, deliveries):
    graph = {}

    for drone in drones:
        graph[drone.id] = []

        for delivery in deliveries:
            if delivery.weight <= drone.max_weight:
                cost = calculate_cost(drone, delivery)
                graph[drone.id].append({
                    'delivery_id': delivery.id,
                    'cost': cost,
                    'delivery_pos': delivery.pos
                })

    return graph
