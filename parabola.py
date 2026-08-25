print("")
print("   HI!")
print("")
print("  If you want to know the direct function that touches two points, unter the coordination of the two points:")
print("")
print("The first point is " + "\033[34;1mA(Xa;Ya)\033[0m" + " and the second point is " + "\033[34;1mB(Xb;Yb)\033[0m")
print("")
print("")
print("\033[34;1m A(Xa;Ya):\033[0m")
Xa = float(input("  Unter " + "\033[34;1mXa : \033[0m"))
Ya = float(input("  Unter " + "\033[34;1mYa : \033[0m"))
print("\033[34;1m B(Xb;Yb):\033[0m")
Xb = float(input("  Unter " + "\033[34;1mXb : \033[0m"))
Yb = float(input("  Unter " + "\033[34;1mYb : \033[0m"))
if Xa == Xb and Ya == Yb:
 print("")
 print("")
 print("  The two points are the same, You have to enter two different points.")
 print("")
 print("")
 print("")
else:
 a0 = (Yb - Ya) / (Xb - Xa)
 b0 = Ya - a0 * Xa
 a = round(a0, 1)
 b = round(b0, 1)
 print("")
 print("")
 if a != 0 and b != 0:
  if a == 1:
    print("The direct function is: " + "\033[32;1m y = x + " + str(b) + "\033[0m")
  else:
     print("The direct function is: " + "\033[32;1m y = " + str(a) + "x + " + str(b) + "\033[0m") 
 elif a != 0 and b == 0:
  if a == 1:
    print("The direct function is: " + "\033[32;1m y = x\033[0m")
  else:
    print("The direct function is: " + "\033[32;1m y = " + str(a) + "x\033[0m")
 elif a == 0 and b != 0:
  print("The direct function is: " + "\033[32;1m y = " + str(b) + "\033[0m")
 else:
  print("The direct function is: " + "\033[32;1m y = 0\033[0m")
  print("")
  print("")
  print("")
