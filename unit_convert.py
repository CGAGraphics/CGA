#this program is ment to not output any interface
def unit_converter_weight_edition():
	def in_pro():
		In3 = input("number please ")
		N20 = int(In3)
		return(N20)
	In1 = input("what kind of units will be converted? ")
	if In1==("kilo-pounds"):
		In2 = input("kilo-pound [k-p] or pound-kilo [p-k] ")
		if In2 == ("p-k"):
			N20 = in_pro()
			O1 = eval(str(N20) + "/" + "2.205")
			print(O1)
			exit()
		elif In2 == ("k-p"):
			N20 = in_pro()
			O1 = eval(str(N20) + "*" + "2.205")
			print(O1)
			exit()
		else:
			exit()
	elif In1==("pounds-ounces"):
		In4 = input("pounds-ounces [p-o] or ounces-pounds [o-p] ")
		if In4 == ("p-o"):
			N20 = in_pro()
			O1 = eval(str(N20) + "*" + "16")
			print(O1)
			exit()
		elif In4 == ("o-p"):
			N20 = in_pro()
			O1 = eval(str(N20) + "/" + "16")
			print(O1)
			exit()
		else:
			exit()
	elif In1==("pound-grams"):
		In5 = input("pounds-grams [p-g] or grams-pounds [g-p] ")
		if In5 == ("p-g"):
			N20 = in_pro()
			O1 = eval(str(N20) + "*" + "453.6")
			print(O1)
			exit()
		elif In5 == ("g-p"):
			N20 = in_pro()
			O1 = eval(str(N20) + "/" + "453.6")
			print(O1)
			exit()
		else:
			exit()
	elif In1==("pound-milligrams"):
		In5 = input("pounds-milligrams [p-m] or milligrams-pounds [m-p] ")
		if In5 == ("p-m"):
			N20 = in_pro()
			O1 = eval(str(N20) + "*" + "453600")
			print(O1)
			exit()
		elif In5 == ("m-p"):
			N20 = in_pro()
			O1 = eval(str(N20) + "/" + "453600")
			print(O1)
			exit()
		else:
			exit()
	elif In1==("pound-tons"):
		In5 = input("pounds-tons [p-t] or tons-pounds [t-p] ")
		if In5 == ("p-t"):
			N20 = in_pro()
			O1 = eval(str(N20) + "*" + "2000")
			print(O1)
			exit()
		elif In5 == ("t-p"):
			N20 = in_pro()
			O1 = eval(str(N20) + "/" + "2000")
			print(O1)
			exit()
		else:
			exit()
	elif In1==("kilo-ounces"):
		In5 = input("kilo-ounces [k-o] or ounces-kilos [o-k] ")
		if In5 == ("k-o"):
			N20 = in_pro()
			O1 = eval(str(N20) + "*" + "35.274")
			print(O1)
			exit()
		elif In5 == ("o-k"):
			N20 = in_pro()
			O1 = eval(str(N20) + "/" + "35.274")
			print(O1)
			exit()
		else:
			exit()
	elif In1==("kilo-milligrams"):
		In5 = input("kilo-milligrams [k-m] or milligrams-kilos [m-k] ")
		if In5 == ("k-m"):
			N20 = in_pro()
			O1 = eval(str(N20) + "*" + "1000000")
			print(O1)
			exit()
		elif In5 == ("m-k"):
			N20 = in_pro()
			O1 = eval(str(N20) + "/" + "1000000")
			print(O1)
			exit()
		else:
			exit()
	elif In1==("kilo-tons"):
		In5 = input("kilo-tons [k-t] or tons-kilos [t-k] ")
		if In5 == ("k-t"):
			N20 = in_pro()
			O1 = eval(str(N20) + "*" + "907.2")
			print(O1)
			exit()
		elif In5 == ("t-k"):
			N20 = in_pro()
			O1 = eval(str(N20) + "/" + "907.2")
			print(O1)
			exit()
		else:
			exit()
	elif In1==("grams-milligrams"):
		In5 = input("grams-milligrams [g-m] or milligrams-grams [m-g] ")
		if In5 == ("g-m"):
			N20 = in_pro()
			O1 = eval(str(N20) + "*" + "1000")
			print(O1)
			exit()
		elif In5 == ("m-g"):
			N20 = in_pro()
			O1 = eval(str(N20) + "/" + "1000")
			print(O1)
			exit()
		else:
			exit()
	elif In1==("grams-tons"):
		In5 = input("grams-tons [g-t] or tons-grams [t-g] ")
		if In5 == ("g-t"):
			N20 = in_pro()
			O1 = eval(str(N20) + "/" + "907200")
			print(O1)
			exit()
		elif In5 == ("t-g"):
			N20 = in_pro()
			O1 = eval(str(N20) + "*" + "907200")
			print(O1)
			exit()
		else:
			exit()
	elif In1==("grams-ounces"):
		In5 = input("grams-ounces [g-o] or ounces-grams [o-g] ")
		if In5 == ("g-o"):
			N20 = in_pro()
			O1 = eval(str(N20) + "/" + "28.35")
			print(O1)
			exit()
		elif In5 == ("o-g"):
			N20 = in_pro()
			O1 = eval(str(N20) + "*" + "28.35")
			print(O1)
			exit()
		else:
			exit()
	else:
		print("if there is a convertion not covered by the program inform us or go to google like a monkey")
		exit()