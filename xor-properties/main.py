from operator import xor


def hex_xor(a: str, b: str) -> str:
	"""XOR two hex strings and return hex string without 0x prefix."""
	ai = int(a, 16)
	bi = int(b, 16)
	xr = ai ^ bi
	# keep leading zeros by using length of the longer input
	width = max(len(a), len(b))
	return format(xr, '0{}x'.format(width))


def main():
	KEY1 = 'a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313'
	KEY2_xor_KEY1 = '37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e'
	KEY2_xor_KEY3 = 'c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1'
	FLAG_xor_KEY1_xor_KEY3_xor_KEY2 = '04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf'

	# Recover KEY2 = (KEY2 ^ KEY1) ^ KEY1
	KEY2 = hex_xor(KEY2_xor_KEY1, KEY1)

	# Recover KEY3 = KEY2 ^ (KEY2 ^ KEY3)
	KEY3 = hex_xor(KEY2, KEY2_xor_KEY3)

	# Now FLAG = (FLAG ^ K1 ^ K3 ^ K2) ^ K1 ^ K3 ^ K2 (XORing same keys cancels)
	# So just xor the provided chain with KEY1, KEY3, KEY2 in any order
	temp = int(FLAG_xor_KEY1_xor_KEY3_xor_KEY2, 16)
	temp ^= int(KEY1, 16)
	temp ^= int(KEY3, 16)
	temp ^= int(KEY2, 16)

	# Convert to bytes and try to decode
	hexflag = format(temp, 'x')
	# Ensure even length
	if len(hexflag) % 2:
		hexflag = '0' + hexflag
	flag_bytes = bytes.fromhex(hexflag)
	try:
		print(flag_bytes.decode('utf-8'))
	except Exception:
		print(flag_bytes)


if __name__ == '__main__':
	main()

