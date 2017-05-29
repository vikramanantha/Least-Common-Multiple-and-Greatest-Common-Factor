factors = []

def gf(num1, num2):
	num11 = num1 + 1
	for i in range(1, num11):
		if num1 % i == 0 and num2 % i == 0:
			factors.append(i)

def lm(num1, num2):
	gf(num1, num2);
	mult12 = num1*num2
	result = mult12/max(factors)
	result = int(result)

lcf = input("LCM or GCF (Least Common Multiple, or Greatest Common Factor)?")
num1 = input("What is the first Number?")
num1 = int(num1)
num2 = input("What is the second Number?")
num2 = int(num2)

if lcf == 'lcm' or lcf == 'LCM':
	lm(num1, num2)
	input(result)

elif lcf == "gcf" or lcf == "GCF":
	gf(num1, num2);	
	input(max(factors))

else:
	input("Something went wrong.")

input("Thank you. Goodbye")