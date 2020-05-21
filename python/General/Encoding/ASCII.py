def intToASCII(list):
	ASCII = ""
	for num in list:
		ASCII += str(chr(int(num)))
	return ASCII


if __name__ == "__main__":
	flag = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]
	print(intToASCII(flag))
