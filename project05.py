def get_valid_input(prompt):
    while True:
        user_input = input(prompt)
        if user_input.lower() == "exit":
            exit()
        if is_valid_integer(user_input):
            return user_input
        else:
            print("Invalid input. Please try again.")
def is_valid_integer(user_input):
    try:
        int(user_input)
        return True
    except ValueError:
        return False
def main():
  print("We are going to be adding Two whole numbers")
  print("type 'exit' to stop")
  calc1()
def calc1():
  x = get_valid_input("Enter first whole number: ")
  y = get_valid_input("Enter second whole number: ")
  sum = int(x) + int(y)
  print("{} + {} = {}". format(x, y, sum))
  calc1()
def exit():
    print("You stopped the equation!")
    quit()
if __name__ == "__main__":
    main()
