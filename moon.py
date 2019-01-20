import random
import math
from PIL import Image

def sample(x, y, num_of_sample_directions=64):
    s = 0.0
    for _ in range(num_of_sample_directions):
        random_rad = 2 * math.pi * random.uniform(0.0, 1.0)
        s += trace(x, y, math.cos(random_rad), math.sin(random_rad))
    return s / num_of_sample_directions # * 2 * math.pi

def trace(ox, oy, dx, dy):
    t = 0.0
    i = 0
    while (i < 10) and (t < 2.0):
        i += 1
        sd = circleSDF(ox + dx * t, oy + dy * t, 0.5, 0.5, 0.1)
        if sd < 1e-6: return 2.0
        t += sd
    return 0.0

def circleSDF(x, y, cx, cy, cr):
    """Return: 
    negative if (x, y) is inside the circle;
    positive if (x, y) is outside the circle;
    zero if (x, y) is on the circle
    """
    return math.sqrt((x - cx) * (x - cx) + (y - cy) * (y - cy)) - cr

def main():
    width, height = 512, 512
    img = Image.new('L', (width, height))
    pixels = img.load()
    for h in range(height):
        for w in range(width):
            pixels[h, w] = int(min(sample(h / float(height), w / float(width)) * 255.0, 255.0))
    img.save("moon1.png")


if __name__ == '__main__':
    main()
