import heapq

class Node:
    def __init__(self, code, name, lat, lon):
        self.code = code
        self.name = name
        self.lat = lat
        self.lon = lon
        self.routes = {}

    def add_route(self, destination_code, weight):
        self.routes[destination_code] = weight

class Graph:
    def __init__(self):
        self.nodes = {}

    def add_airport(self, node):
        self.nodes[node.code] = node

    def add_route(self, from_code, to_code, weight):
        self.nodes[from_code].add_route(to_code, weight)

    def dijkstra(self, start_code, end_code):
        distances = {code: float('inf') for code in self.nodes}
        distances[start_code] = 0
        previous = {}
        queue = [(0, start_code)]

        while queue:
            current_dist, current_code = heapq.heappop(queue)

            if current_code == end_code:
                break

            for neighbor, weight in self.nodes[current_code].routes.items():
                distance = current_dist + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous[neighbor] = current_code
                    heapq.heappush(queue, (distance, neighbor))

        path, current = [], end_code
        while current in previous:
            path.append(current)
            current = previous[current]
        if path:
            path.append(start_code)
            path.reverse()
        return path
