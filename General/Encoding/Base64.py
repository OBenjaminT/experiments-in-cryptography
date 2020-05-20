import base64

def hexToBin(list):
	bina = []
	for i in range(0, len(list) - 1):
		bina.append(str(bin(int(list[i], 16))).zfill(8).replace("b", "0"))
	return bina


def binToB64(list):
	bsf = []
	for item in list:
		bsf.append(base64.b64encode(item))
	return bsf


if __name__ == "__main__":
	flag = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
	print(hexToBin(flag))
	print([int(p, 2) for p in hexToBin(flag)])
	print(binToB64(bytes(str([int(p, 2) for p in hexToBin(flag)]), "utf-8")))
