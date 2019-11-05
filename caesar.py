import argparse
from cypher import Caesar

## set up arguments --
parser = argparse.ArgumentParser()

#parser.add_argument('--example', nargs='?', const=1, type=int)
# cypher argument
parser.add_argument('-c', '-cypher', action='store_true', help='Cypher input message.')

# decypher argument
parser.add_argument('-d', '-decypher', action='store_true', help='Decypher input message.')

# shift value
parser.add_argument('-s', '-shift', type=int, default=0, help='Shift value for cypher.')
# input message
parser.add_argument('-m', '-message', type=str, help="Input message for cypher.")

args = parser.parse_args()


def main():
	if args.s <= 0:
		print('Must provide shift integer.')
		return

	# initialize ceasar cypher
	caesar = Caesar()
	# determine whether to encrypt or decrypt
	if args.c is True:
		output = caesar.cypher(args.m, args.s, keep_caps=False)
	elif args.d is True:
		output = caesar.decypher(args.m, args.s, keep_caps=False)
	else:
		print('Must flag whether to cypher or decypher input message.')
		return
	
	print('Shift: {}'.format(args.s))
	print('Output Message: {}'.format(output))
	return

if __name__ == '__main__':
	main()