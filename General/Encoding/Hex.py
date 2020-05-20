from ASCII import intToASCII


def hexToInt(list):
	inte = []
	for i in range(0, len(list) - 1, 2):
		inte.append(str(int(list[i:i + 2], 16)))
	return inte


if __name__ == "__main__":
	flag = "63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d"
	print(intToASCII(hexToInt(flag)))
