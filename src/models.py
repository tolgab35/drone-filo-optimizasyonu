# Veri sınıfları (Drone, Delivery, NoFlyZone)

class Drone:
    def __init__(self, id, max_weight, battery, speed, start_pos):
        self.id = id
        self.max_weight = max_weight
        self.battery = battery
        self.speed = speed
        self.start_pos = start_pos

    def __repr__(self):
        return f"Drone(id={self.id}, max_weight={self.max_weight}, battery={self.battery}, speed={self.speed}, start_pos={self.start_pos})"


class Delivery:
    def __init__(self, id, pos, weight, priority, time_window):
        self.id = id
        self.pos = pos
        self.weight = weight
        self.priority = priority
        self.time_window = time_window

    def __repr__(self):
        return f"Delivery(id={self.id}, pos={self.pos}, weight={self.weight}, priority={self.priority}, time_window={self.time_window})"


class NoFlyZone:
    def __init__(self, id, coordinates, active_time):
        self.id = id
        self.coordinates = coordinates
        self.active_time = active_time

    def __repr__(self):
        return f"NoFlyZone(id={self.id}, coordinates={self.coordinates}, active_time={self.active_time})"
