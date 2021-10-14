# better method then sys module
import argparse as arg
parser = arg.ArgumentParser()
parser.add_argument('arg1', help='Enter a number', type=float)
parser.add_argument('arg2', help='Enter another', type=float)
args = parser.parse_args()  # it parses the arguments
print('sum of these argment is: ', args.arg1+args.arg2)
# get the arguments out
print(f'these were the argumnets you entered {args.arg1} and {args.arg2}')
# convert in dictionary by vars
print('dictionary is: ', vars(args))
