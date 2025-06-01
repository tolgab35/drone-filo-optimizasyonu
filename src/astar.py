# A* algoritması

import heapq
import math
from src.graph import euclidean_distance


def a_star(drone, delivery, no_fly_zones, current_time=0):
    start = drone.start_pos
    goal = delivery.pos

    open_list = []
    heapq.heappush(open_list, (0, start))
    came_from = {}
    g_score = {start: 0}

    while open_list:
        _, current = heapq.heappop(open_list)

        if current == goal:
            # Yol bulundu, geriye doğru inşa et
            path = [current]
            while current in came_from:
                current = came_from[current]
                path.append(current)
            path.reverse()
            return path, g_score[goal]

        for neighbor in get_neighbors(current):
            # Sınır kontrolü: koordinatlar negatif olmasın
            if neighbor[0] < 0 or neighbor[1] < 0:
                continue

            tentative_g = g_score[current] + euclidean_distance(current, neighbor)

            if neighbor not in g_score or tentative_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g

                h = heuristic(neighbor, goal, no_fly_zones, current_time)
                f = tentative_g + h
                heapq.heappush(open_list, (f, neighbor))

    return None, float('inf')  # Yol bulunamadı


def get_neighbors(pos):
    x, y = pos
    step = 1  # adım büyüklüğü (hassasiyet)
    return [
        (x + step, y), (x - step, y),
        (x, y + step), (x, y - step),
        (x + step, y + step), (x - step, y - step),
        (x + step, y - step), (x - step, y + step)
    ]


def heuristic(pos, goal, no_fly_zones, current_time):
    distance = euclidean_distance(pos, goal)
    penalty = 0

    for zone in no_fly_zones:
        if zone.active_time[0] <= current_time <= zone.active_time[1]:
            if is_inside_polygon(pos, zone.coordinates):
                penalty += 1000  # ceza puanı

    return distance + penalty


def is_inside_polygon(point, polygon):
    try:
        from matplotlib.path import Path
        return Path(polygon).contains_point(point)
    except ImportError:
        print("matplotlib modülü eksik. Lütfen yükleyin: pip install matplotlib")
        return False
