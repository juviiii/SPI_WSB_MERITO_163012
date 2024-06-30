from string import ascii_letters


def get_name():
    name = input("What is your name? ").strip().title()
    while not all(letter in ascii_letters + " -" for letter in name):
        name = input("Please enter a valid name: ").strip().title()
    return name

def get_surname():
    surname = input("What is your last name? ").strip().title()
    while not all(letter in ascii_letters + " -" for letter in surname):
        surname = input("Please enter a valid last name: ").strip().title()
    return surname

def main():
    name = get_name()
    surname = get_surname()
    age = input("What is your age? ")
    #print(f"Hi, my name is {name}, and I am {age} years old.")
    print(f"Your new login is: {name}_{age}_{surname}")

if __name__ == "__main__":
    main()
