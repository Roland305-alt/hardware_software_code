def greeting():
    print("Welcome to my program conversation")
    print("This program is designed to have a conversation with the user by asking numerouse of questions")
    print("I will keep asking questions until you type 'exit'")

    print("what is your name?")
    name = input()
    if name == "exit":
      exit()
    print("what is your favorite movie?")
    answer = input()
    if answer == "exit":
      exit()
    print("what is your favorite tv show?")
    answer = input()
    if answer == "exit":
      exit()
    print("what is your family from?")
    answer = input()
    if answer == "exit":
        exit()
    greeting()
def main():
  count = 0
greeting()
def exit():
    print("Thanks for chatting with me Roly Salcedo")
    quit()
if __name__== "__main__":
    main()
