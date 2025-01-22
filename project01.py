def main():
    print("welcome to hardware and software")
    print("this program is designed find out if anyone is interested and wants to learn about programming" )
    print("what is your name")
    name = input()
    print("We want to know if you like programming!")
    print()
    print("Do you like programming {}?".format(name))
    answer = input()
    if answer == "yes":
        print("we can't wait to teach you some Python")
    elif answer == "no":
        print("Hmm... You said{}?".format(answer))
    print("what college are you attending?")
    answer1 = input()
    print("what high school did you attend?")
    answer2 = input()
    print("which do you like the best?")
    answer3 = input()
    print("Wow, now we know you attended {}".format(answer1))
    print("we know you attended {}".format(answer2))
    print("and you said that {} was the best".format(answer3))
if __name__ == "__main__":
    main()
