#we will need to try and implement this in our python storage tracker rewritten
import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('integers', metavar='N', type=int, nargs='+',help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate',action='store_const',const=sum,default=max, help='sum the ints (default: find the max)')

args = parser.parse_args()
print(args.accumulate(args.integers))