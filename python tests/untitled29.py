#! /bin/python3

# A smarter way of finding the roots of a quadratic equation

a = float(input("Enter A: "))
if a == 0: # Not a quadratic equation
	print("\nIt is not a quadratic equation!"

else :  # A quadratic equation ### Burda neden hata veriyor ??????
b = float(input("Enter B: "))
c = float(input("Enter C: "))
	
	# Calculating delta
	d = b**2 - 4*a*c
	
	# Calculating the roots
	if d < 0: # No real roots
		print("\nNo real roots!")
	elif d == 0: # 1 real root
		print("\nOnly one real root.")
		print("The root is", -b/(2*a))
	else: # 2 real roots
		print("\nTwo real roots.")
		r1 = (-b + d**0.5)/(2*a)
		r2 = (-b - d**0.5)/(2*a)
		print("The roots are", r1, "and", r2)
