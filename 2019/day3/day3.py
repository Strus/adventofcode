class Move:
    direction = ""
    distance = 0


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


class Line:
    def __init__(self, start=Point(), end=Point()):
        self.start = start
        self.end = end

    def get_length(self):
        if self.is_horizontal():
            return abs(self.end.x - self.start.x)
        else:
            return abs(self.end.y - self.start.y)

    def is_horizontal(self):
        return self.start.y == self.end.y


def get_moves_lists():
    with open("input.txt") as f:
        moves_txt = f.read()

    moves_lines = moves_txt.split('\n')
    moves = []
    for line in moves_lines:
        moves_for_line = []
        for move_instruction in line.split(','):
            m = Move()
            m.direction = move_instruction[0]
            m.distance = int(move_instruction[1:])
            moves_for_line.append(m)
        moves.append(moves_for_line)

    return moves


def get_point_coords(start, move):
    point = Point(start.x, start.y)
    if move.direction == 'U':
        point.y += move.distance
    elif move.direction == 'D':
        point.y -= move.distance
    elif move.direction == 'R':
        point.x += move.distance
    elif move.direction == 'L':
        point.x -= move.distance

    return point


def intersect_horizontal(horizontal, vertical):
    if horizontal.start.x <= vertical.start.x <= horizontal.end.x \
            or horizontal.end.x <= vertical.start.x <= horizontal.start.x:
        if vertical.start.y <= horizontal.start.y <= vertical.end.y \
                or vertical.end.y <= horizontal.start.y <= vertical.start.y:
            return abs(horizontal.start.y) + abs(vertical.start.x)

    return 0


def get_intersect_distance(line1, line2):
    if (line1.is_horizontal() and line2.is_horizontal()) \
            or (not line1.is_horizontal() and not line2.is_horizontal()):
        return 0

    if line1.is_horizontal():
        return intersect_horizontal(line1, line2)
    else:
        return intersect_horizontal(line2, line1)


def create_path(start_point, moves):
    path = []
    previous_end = start_point
    for move in moves:
        line = Line(previous_end, get_point_coords(previous_end, move))
        path.append(line)
        previous_end = line.end

    return path


def part_one():
    moves = get_moves_lists()
    start = Point(0, 0)
    paths = [create_path(start, moves[0]), create_path(start, moves[1])]

    intersections = []
    for line1 in paths[0]:
        for line2 in paths[1]:
            distance = get_intersect_distance(line1, line2)
            if distance > 0:
                intersections.append(distance)

    intersections.sort()
    print(intersections[0])


def get_intersect_horizontal_steps(horizontal, vertical):
    if horizontal.start.x <= vertical.start.x <= horizontal.end.x \
            or horizontal.end.x <= vertical.start.x <= horizontal.start.x:
        if vertical.start.y <= horizontal.start.y <= vertical.end.y \
                or vertical.end.y <= horizontal.start.y <= vertical.start.y:
            intersection = Point(vertical.start.x, horizontal.start.y)
            return abs(horizontal.start.x - intersection.x) + \
                abs(vertical.start.y - intersection.y)

    return 0


def get_intersect_steps(line1, line2):
    if (line1.is_horizontal() and line2.is_horizontal()) \
            or (not line1.is_horizontal() and not line2.is_horizontal()):
        return 0

    if line1.is_horizontal():
        return get_intersect_horizontal_steps(line1, line2)
    else:
        return get_intersect_horizontal_steps(line2, line1)


def part_two():
    moves = get_moves_lists()
    start = Point(0, 0)
    paths = [create_path(start, moves[0]), create_path(start, moves[1])]

    intersections = []
    total_steps = 0
    for line1 in paths[0]:
        steps_before = total_steps
        for line2 in paths[1]:
            steps = get_intersect_steps(line1, line2)
            if steps > 0:
                total_steps += steps
                intersections.append(total_steps)
                total_steps -= steps
            else:
                line2_length = line2.get_length()
                total_steps += line2_length
        total_steps = steps_before
        line1_length = line1.get_length()
        total_steps += line1_length

    intersections.sort()
    print(intersections[0])


part_one()
part_two()
