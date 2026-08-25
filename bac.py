print(" ")
print(" ")
print("          " + "\033[1;35;3;4mWelcome to BAC calculator\033[0m")
print(" ")
print("\033[35;4mPut your marks to calculate your bac:\033[0m")
print(" ")
math = input("   • Mathematics:")
m1 = float(math)
phy = input("   • Physics:")
m2 = float(phy)
arb = input("   • Arabic:")
m3 = float(arb)
scn = input("   • Science:")
m4 = float(scn)
frn = input("   • French:")
m5 = float(frn)
eng = input("   • English:")
m6 = float(eng)
hist = input("   • History:")
m7 = float(hist)
tam = input("   • Tamazight:")
m8 = float(tam)
isl = input("   • Islamic:")
m9 = float(isl)
phi = input("   • Philosophy:")
m10 = float(phi)
spo = input("   • Sport:")
m11 = float(spo)
bac = round((m1 * 7 + m2 * 6 + m3 * 3 + (m4 + m5 + m6 + m7 + m8 + m9 + m10) * 2 + m11) / 31, 2)
print(" ")
print("Your result " + "\033[34mBAC : \033[0m" + "\033[34;7m" + str(bac) + "\033[0m")
print(" ")
print(" ")
print("The possibility of entering National School:")
print(" ")
w1 = (float(bac) * 2 + float(m1)) / 3
w2 = (float(bac) * 4 + float(m1)  + float(m2)) / 6
M1 = round(max(w1, bac), 2)
M2 = round(max(w2, bac), 2)
if M1 >= 18.44:
    print("\033[32m     ● AI: \033[0m" + "You got:    " + "\033[32m" + str(M1) + "\033[0m" + " > 18.59")
else:
    print("\033[31m     ● AI: \033[0m" + "You got:    " + "\033[31m" + str(M1) + "\033[0m" + " < 18.59")
if M1 >= 18.10:
    print("\033[32m     ● CS: \033[0m" + "You got:    " + "\033[32m" + str(M1) + "\033[0m" + " > 18.34")
else:
    print("\033[31m     ● CS: \033[0m" + "You got:    " + "\033[31m" + str(M1) + "\033[0m" + " < 18.34")
if M2 >= 18.06:
    print("\033[32m     ● SA: \033[0m" + "You got:    " + "\033[32m" + str(M2) + "\033[0m" + " > 18.21")
else:
    print("\033[31m     ● SA: \033[0m" + "You got:    " + "\033[31m" + str(M2) + "\033[0m" + " < 18.21")
if M2 >= 17.69:
    print("\033[32m     ● NS: \033[0m" + "You got:    " + "\033[32m" + str(M2) + "\033[0m" + " > 17.96")
else:
    print("\033[31m     ● NS: \033[0m" + "You got:    " + "\033[31m" + str(M2) + "\033[0m" + " < 17.96")
if M1 >= 17.43:
    print("\033[32m     ● MT: \033[0m" + "You got:    " + "\033[32m" + str(M1) + "\033[0m" + " > 17.43")
else:
    print("\033[31m     ● MT: \033[0m" + "You got:    " + "\033[31m" + str(M1) + "\033[0m" + " < 17.43")
print(" ")
print(" ")