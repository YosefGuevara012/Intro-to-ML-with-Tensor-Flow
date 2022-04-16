import math
import argparse

parser = argparse.ArgumentParser(description="Calculate veolume of a cylinder")
parser.add_argument("-r" ,'--radius', type = int, metavar = "", required = True, help = 'Radius of the cylinder')
parser.add_argument("-H" ,'--height', type = int, metavar = "", required = True, help = 'Height of the cylinder')
group = parser.add_mutually_exclusive_group()
group.add_argument("-q","--quiet", action = 'store_true', help = 'print quiet')
group.add_argument("-v","--verbose", action = 'store_true', help = 'print verbose')
args = parser.parse_args()
                                

def cylinder_volume(radius, height):
    vol = (math.pi) * (radius ** 2) * (height)
    return vol

if __name__ == '__main__':
    volume = cylinder_volume(args.radius, args.height)

    if args.quiet:
        print (volume)
    elif args.verbose:
        print("Volume of the Cylynder wih a radius {0} and height {1} is {2}".format(args.radius, args.height, volume))
    else:
        print("Volume of the Cylynder is {}".format(volume))
