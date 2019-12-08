class OrbitDefinition:
    def __init__(self, orbit_txt):
        self.object = orbit_txt.split(")")[1]
        self.orbits_around = orbit_txt.split(")")[0]


class MapNode:
    def __init__(self):
        self.orbit = ""
        self.orbits_around = []
        self.neighbours = []
        self.visited = False


class Map:
    def __init__(self):
        self.nodes = []
        self.you = None
        self.san = None

    def add_orbit(self, orbit):
        node = self.find_orbit(orbit.object)
        node_around = self.find_orbit(orbit.orbits_around)
        node.orbits_around.append(node_around)
        node.neighbours.append(node_around)
        node_around.neighbours.append(node)
        if node.orbit == "YOU":
            self.you = node
            self.you.visited = True
        if node.orbit == "SAN":
            self.san = node

    def find_orbit(self, orbit):
        for node in self.nodes:
            if node.orbit == orbit:
                return node

        new_node = MapNode()
        new_node.orbit = orbit
        self.nodes.append(new_node)
        return new_node


def get_orbits_list():
    with open("input.txt") as f:
        raw_map = f.read().split('\n')

    orbit_list = []
    for line in raw_map:
        orbit = OrbitDefinition(line)
        orbit_list.append(orbit)

    return orbit_list


def count_orbits(node):
    orbit_count = len(node.orbits_around)
    for n in node.orbits_around:
        orbit_count += count_orbits(n)

    return orbit_count


def part_one():
    orbits = get_orbits_list()
    sky_map = Map()
    for orbit in orbits:
        sky_map.add_orbit(orbit)

    orbit_count = 0
    for node in sky_map.nodes:
        orbit_count += count_orbits(node)

    print(orbit_count)


def visit_node(node, san, san_distance):
    san_distance += 1
    node.visited = True
    for n in node.neighbours:
        if n.visited:
            continue
        visit_node(n, san, san_distance)

    if node is not san:
        san_distance -= 1
    else:
        print(san_distance - 2)


def part_two():
    orbits = get_orbits_list()
    sky_map = Map()
    for orbit in orbits:
        sky_map.add_orbit(orbit)

    san_distance = 0
    for node in sky_map.you.neighbours:
        visit_node(node, sky_map.san, san_distance)


part_one()
part_two()
