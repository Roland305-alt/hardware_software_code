def greeting():
    print("Welcome to my program")
    print("This program is designed to have a conversation with the user by asking numerouse of questions")
    print("I will keep asking until you type'exit'" )
    print("What is your name?")
    name = input()
    if name == "exit":
        exit()
    print("What is your favorite movie?")
    answer = input()
    if answer == "exit":
        exit()
    print("what is your favorite tv show?")
    answer = input()
    if answer == "exit":
        exit()
    print("What is your family from?")
    answer = input()
    if answer == "exit":
        exit()
    greeting()

def main():
    greeting()
def exit():
    print("Thanks for chating with me Roly Salcedo")
    quit()

if __name__== "__main__":
    main()
