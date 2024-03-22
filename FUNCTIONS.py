def keyboard_compare():
	N6=input("Number please ")
	N7 = int(N6) 
	N8 = input("op plz ")
	if N8== ("+"):
		N9 = ("+")
	elif N8== ("-"):
		N9 = ("-")
	elif N8== ("x"):
		N9 = ("x")
	elif N15== ("*"):
		N16 = ("*")
	elif N8== ("/"):
		N9 = ("/")
	else:
		exit()
	N10 = input("nuber plz ")
	N11 = int(N10)
	N12 = eval( str(N7) + N9 + str(N11))

	N13=input("Number please ")
	N14 = int(N13) 
	N15 = input("op plz ")
	if N15== ("+"):
		N16 = ("+")
	elif N15== ("-"):
		N16 = ("-")
	elif N15== ("x"):
		N16 = ("x")
	elif N15== ("*"):
		N16 = ("*")
	elif N15== ("/"):
		N16 = ("/")
	else:
		exit()
	N17 = input("nuber plz ")
	N18 = int(N17)
	N19 = eval(str(N14) + N16 + str(N18))

	if N12 < N19:
		print(str(N12) + " less than " + str(N19))
		print(str(N12) + " < " + str(N19)) 
	elif N12 > N19:
		print(str(N12) + " greater than " + str(N19))
		print(str(N12) + " > " + str(N19))
	elif N12 == N19:
		print(str(N12) + " equal to " + str(N19))
		print(str(N12) + " == " + str(N19))	 
	else:
		exit()
def numpad_compare():
	N6=input("Number please ")
	N7 = int(N6) 
	N8 = input("op plz ")
	if N8== ("+"):
		N9 = ("+")
	elif N8== ("-"):
		N9 = ("-")
	elif N8== ("*"):
		N9 = ("*")
	elif N8== ("/"):
		N9 = ("/")
	else:
		exit()
	N10 = input("nuber plz ")
	N11 = int(N10)
	N12 = eval( str(N7) + N9 + str(N11))
	
	N13=input("Number please ")
	N14 = int(N13) 
	N15 = input("op plz ")
	if N15== ("+"):
		N16 = ("+")
	elif N15== ("-"):
		N16 = ("-")
	elif N15== ("*"):
		N16 = ("*")
	elif N15== ("/"):
		N16 = ("/")
	else:
		exit()
	N17 = input("nuber plz ")
	N18 = int(N17)
	N19 = eval(str(N14) + N16 + str(N18))

	if N12 < N19:
		print(str(N12) + " less than " + str(N19))
		print(str(N12) + " < " + str(N19)) 
	elif N12 > N19:
		print(str(N12) + " greater than"  + str(N19))
		print(str(N12) + " > " + str(N19))
	elif N12 == N19:
		print(str(N12) + " equal to " + str(N19))
		print(str(N12) + " == " + str(N19))	 
	else:
		exit()		
