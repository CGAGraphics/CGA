#Calc++
import unit_convert
import math
import FUNCTIONS
import Manual
def Calc_main_program1():
	In1=input("#/⊗ ")
	INNP=(In1.isdigit())
	if INNP==False:
		if In1==str("SER"):
			Manual.SERMANUAL()
			return
		elif In1==str("PT"):
			IN1=input("A ")
			IN2=input("B ")
			ITN1=eval(str(IN1)+"*"+str(IN1))
			ITN2=eval(str(IN2)+"*"+str(IN2))
			ITN3=eval(str(ITN1)+"+"+str(ITN2))
			print(math.sqrt(ITN3))
			return
		elif In1==("%"):
			IN1=input("Per ")
			IN2=input("of ")
			ITN1=eval(str(IN1)+"*"+str(IN2))
			ITN2=eval(str(ITN1)+"/"+"100")
			print(str(ITN2)+" is "+str(IN1)+"% of "+str(IN2))
			return
		elif In1==str("^"):
			In2=input("Number please ")
			In3 = input("exponant ")
			O1 = In2 ** In3
			print(str(O1))
			return
		elif In1==str("%-."):
			In2=int(input("percentage "))
			In3=int(input("percentage of... "))
			print(eval(str(In2) +"/"+ str(In3)))
			return
		elif In1==str("FS"):
			from fractions import Fraction
			fraction_value = Fraction(numerator,denominator)
			print(fraction_value)
			return
		elif In1==("fr-de"):
			In2=int(input("numerator "))
			In3=int(input("denominator "))
			print(eval(str(In1) + "/" + str(In2)))
			return
		elif In1==("<numpad>"):
			FUNCTIONS.numpad_compare()
			return
		elif In1==str("UCWE"):
			unit_convert.unit_converter_weight_edition()
			return
		elif In1==str("P"):
			def IDB(int,div):
				if int==div:
					return False
				remainder = int % div
				if remainder ==0:
					return True
				else:
					return False
				print("One no work do no use one it is both")
			S1 = input("Numbrt now ")
			N2 = int(S1)
			DIVS = [2]
			DIVS = DIVS + list(range(3,N2,2))
			for Repetor in range(1,N2+1):
				isNotPrime = False
				for DIV in DIVS:
					if IDB(Repetor,DIV):
						isNotPrime = True
						print(Repetor)
						break
				if isNotPrime == False:
					print(str(Repetor) + " is prime")
			return
		elif In1==str("Quit"):
			exit()
		input("hit enter to continue")
		return
	IN2=input("⊗ ")
	if IN2==str("!"):
		print(math.factorial(int(In1)))
		return
	elif IN2==str("|"):
		print(math.sqrt(int(In1)))
		return
	elif IN2==str("#"):
			INP1=(eval(str(In1)+ "-" + "2"))
			print(eval(str(INP1)+"*"+"180"))
			return
	IN3=input("# ")
	if INNP==True:
		print(eval(str(In1) + IN2 + str(IN3)))
	else:
		 print("Sorry currently not supported.")
		 return

while(True):
	Calc_main_program1()