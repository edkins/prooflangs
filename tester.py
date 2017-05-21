import sys
from antlr4 import *
from HelloLexer import HelloLexer
from HelloParser import HelloParser
from HelloListener import HelloListener

def print_parse_tree(tree, indent):
	if hasattr(tree, 'symbol'):
		print('%s%s' % (indent, tree.symbol))
	else:
		print('%s.' % (indent,))
	if hasattr( tree, 'children'):
		for child in tree.children:
			print_parse_tree(child, indent + ' ')

def main(argv):
	input = FileStream(argv[1])
	lexer = HelloLexer(input)
	stream = CommonTokenStream(lexer)
	parser = HelloParser(stream)
	tree = parser.r()
	print_parse_tree(tree, '')
 
if __name__ == '__main__':
	main(sys.argv)
