"""Small CLI to XOR a label's characters with integer 13 and print as crypto{...}.

Usage:
	python3 main.py [label]

If no label is given, a placeholder 'label' is used.
"""
import sys
from tool import xor_label


def main():
	label = sys.argv[1] if len(sys.argv) > 1 else 'label'
	print(f"crypto{{{xor_label(label, 13)}}}")


if __name__ == '__main__':
	main()

