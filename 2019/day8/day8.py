class Layer:
    def __init__(self):
        self.data = ""
        self.zeros = 0
        self.ones = 0
        self.twos = 0

    def __eq__(self, other):
        return self.zeros == other.zeros

    def __lt__(self, other):
        return self.zeros < other.zeros

    def set_data(self, data):
        self.data = data
        for n in data:
            if n == "0":
                self.zeros += 1
            elif n == "1":
                self.ones += 1
            elif n == "2":
                self.twos += 1


class Image:
    def __init__(self, width, height):
        self.layers = []
        self.width = width
        self.height = height

    def add_layer(self, layer):
        self.layers.append(layer)

    def get_checksum(self):
        layers_sorted = self.layers.copy()
        layers_sorted.sort()
        print(layers_sorted[0].ones * layers_sorted[0].twos)

    def get_color_from_layer(self, index, n):
        if self.layers[index].data[n] == "2":
            return self.get_color_from_layer(index + 1, n)
        else:
            return list(self.layers[index].data)[n]

    def render(self):
        first_layer = self.layers[0]
        rendered = Layer()
        rendered.data = first_layer.data
        for n in range(len(rendered.data)):
            d = list(rendered.data)
            if d[n] == "2":
                d[n] = self.get_color_from_layer(1, n)
            if d[n] == "0":
                d[n] = "."
            rendered.data = "".join(d)
        for i in range(0, len(rendered.data), self.width):
            print(rendered.data[i:i+self.width])


def load_image():
    with open("input.txt") as f:
        data = f.read()

    image = Image(25, 6)
    layer_size = image.width * image.height
    for i in range(0, len(data) - layer_size, layer_size):
        layer = Layer()
        layer.set_data(data[i:i+layer_size])
        image.add_layer(layer)

    return image


def part_one():
    image = load_image()
    image.get_checksum()


def part_two():
    image = load_image()
    image.render()


part_one()
part_two()
