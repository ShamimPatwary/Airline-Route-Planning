from .models import Airport, Route
from .graph import Graph, Node

class RoutePlanner:
    def __init__(self):
        self.graph = Graph()
        self._load_graph()

    def _load_graph(self):
        # Load all airports from the database and add to the graph
        for airport in Airport.objects.all():
            node = Node(
                code=airport.code,
                name=airport.name,
                lat=airport.latitude,
                lon=airport.longitude
            )
            self.graph.add_airport(node)

        # Load all routes and connect them in the graph
        for route in Route.objects.all():
            self.graph.add_route(
                from_code=route.origin.code,
                to_code=route.destination.code,
                weight=route.distance
            )

    def get_path(self, from_code, to_code):
        """
        Uses Dijkstra's algorithm to find the shortest path.
        Returns a list of airport codes representing the path.
        """
        return self.graph.dijkstra(from_code, to_code)
