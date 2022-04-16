import math
import argparse

parser = argparse.ArgumentParser(description="Calculate veolume of a cylinder")
parser.add_argument('radius', type =int)
parser.add_argument('height', type =int)
args = parser.parse_args()
                                

def cylinder_volume(radius, height):
    vol = (math.pi) * (radius ** 2) * (height)
    return vol

if __name__ == '__main__':
    volume = cylinder_volume(args.radius, args.height)
    print(volume)
