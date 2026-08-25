print("")
print("")
print("\033[1;3;35m   Welcome to\033[0m \033[34;1;3mGuessing Game\033[0m")
print("")
print("")
print(" \033[36;1;4mRules:\033[0m \033[3mI will pick a number in my minde [1;100] and you will try to guess it.\033[0m")
print("\033[3mDo not worry i am going to help you,\033[0m")
print("\033[3mwhen you write a number i will tell you if my number is higher or lower.\033[0m")
print("")
import random
num = random.randint(1, 100)
while True:
   try:
      guess = float(input("Guess a number : "))
      break
   except ValueError:
      print("\033[31mPlease enter a valid number\033[0m")
i = 1
while guess != num:
    i = i + 1
    if guess < num:
      while True:
       try:
          guess = float(input(f"{round(guess)}\033[32m▲ \033[0m guess n°{i} : "))
          break
       except ValueError:
          print("\033[31mPlease enter a valid number\033[0m")
    elif guess > num:
      while True:
       try:
          guess = float(input(f"{round(guess)}\033[31m▼ \033[0m guess n°{i} : "))
          break
       except ValueError:
          print("\033[31mPlease enter a valid number\033[0m")
print("")
print(f"\033[34;1m   Good Job, you got it :\033[0m \033[32;1m{num}\033[0m")
print("")
print(f" \033[1;4mYour score\033[0m : \033[35;1m{i}\033[0m")