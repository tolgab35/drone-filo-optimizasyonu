# Kısıt çözümleyici

from src.graph import euclidean_distance
from src.astar import is_inside_polygon
from shapely.geometry import LineString, Polygon


def is_valid_delivery(drone, delivery, no_fly_zones, current_time):
    if delivery.weight > drone.max_weight:
        return False

    start_time, end_time = delivery.time_window
    if not (start_time <= current_time <= end_time):
        return False

    for zone in no_fly_zones:
        z_start, z_end = zone.active_time
        if z_start <= current_time <= z_end:
            if is_inside_polygon(delivery.pos, zone.coordinates):
                return False

    return True


def violates_no_fly_zone_path(start, end, no_fly_zones, current_time):
    flight_path = LineString([start, end])
    for zone in no_fly_zones:
        z_start, z_end = zone.active_time
        if z_start <= current_time <= z_end:
            zone_polygon = Polygon(zone.coordinates)
            if flight_path.intersects(zone_polygon):
                return True
    return False


def is_valid_route(drone, delivery_list, no_fly_zones, start_time=0):
    current_time = start_time
    current_pos = drone.start_pos
    total_distance = 0

    for delivery in delivery_list:
        distance = euclidean_distance(current_pos, delivery.pos)
        total_distance += distance
        travel_time = distance / drone.speed
        arrival_time = current_time + travel_time

        # ✳️ YENİ: Uçuş çizgisi yasak bölgeyi kesiyor mu?
        if violates_no_fly_zone_path(current_pos, delivery.pos, no_fly_zones, arrival_time):
            return False

        if not is_valid_delivery(drone, delivery, no_fly_zones, arrival_time):
            return False

        current_pos = delivery.pos
        current_time = arrival_time

    # 🔋 BATARYA KONTROLÜ
    estimated_energy_usage = total_distance * 10  # 10 birim = 1 mAh örneği
    if estimated_energy_usage > drone.battery:
        return False

    return True
