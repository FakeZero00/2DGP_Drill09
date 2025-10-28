#world[0] : background layer
#world[1] : default layer
world = [[], []]

def add_object(o, depth = 1):
    world[depth].append(o)

def remove_object(o):
    for layer in world:
        if o in layer:
            layer.remove(o)
            print("Object removed.")
            return
    print("Object not found.")


def update():
    for layer in world:
        for o in layer:
            o.update()

def render():
    for layer in world:
        for o in layer:
            o.draw()