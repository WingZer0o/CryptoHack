from operator import xor


def xor_label(label: str, key: int = 13) -> str:
	"""XOR each character in `label` with integer `key` and return the resulting string.

	This converts each character to its Unicode code point (ord), XORs with `key`,
	and converts back to characters with chr. If pwntools is available, the
	pwntools.xor helper for bytes is used when possible.
	"""
	# Fast path: operate on bytes using pwntools.xor then produce characters
	try:
		b = label.encode('utf-8')
		kb = bytes([key]) * len(b)
		xb = xor(b, kb)
		return ''.join(chr(c) for c in xb)
	except Exception:
		# Fallback: per-character ordinal XOR (handles wide codepoints)
		out_chars = []
		for ch in label:
			out_chars.append(chr(ord(ch) ^ key))
		return ''.join(out_chars)


if __name__ == '__main__':
	# Demo placeholder label. Replace this with the challenge label when known.
	demo_label = 'label'
	transformed = xor_label(demo_label, 13)
	print(f"crypto{{{transformed}}}")


