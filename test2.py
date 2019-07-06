response = 0
answer = "Sulaiman"
while(response <= 3):
    print("Who is Mr.Thuuss?")
    tries = raw_input()
    if (response == "Sulaiman"):
        print("That's the right answer")
    elif (response == 3):
        print("Sorry. The correct answers is Sulaiman.")
    else:
        print("Sorry wrong answer.")