print("Welcome to the Love Calculator")
name1 = input("What is your name?\n")
name2 = input("What is their name? \n")

lower_name1 = name1.lower()
lower_name2 = name2.lower()

both_names = lower_name1 + lower_name2
tens = both_names.count("t") + both_names.count("r") + both_names.count("u") + both_names.count("e")
ones = both_names.count("l") + both_names.count("o") + both_names.count("v") + both_names.count("e")

love = str(tens) + str(ones)
love_int = int(love)

if love_int <= 10 or love_int >= 90:
    print(f"your score is {love}, you go together like coke and mentos")
elif love_int >= 40 and love_int <= 50:
    print(f"your score is {love}, you are alright together")
else:
    print(f"your score is {love}")
