"""Small CLI to XOR a label's characters with integer 13 and print as crypto{...}.

Usage:
	python3 main.py [label]

If no label is given, a placeholder 'label' is used.
"""

import sys


def manual_xor_label(label: str, key: int = 13) -> str:
	"""Manually XOR each character's Unicode code point with `key` and return the new string."""
	out = []
	for ch in label:
		out.append(chr(ord(ch) ^ key))
	return ''.join(out)


def main():
	label = sys.argv[1] if len(sys.argv) > 1 else 'label'
	print(f"crypto{{{manual_xor_label(label, 13)}}}")


if __name__ == '__main__':
	main()

