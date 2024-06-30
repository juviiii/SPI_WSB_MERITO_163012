from string import ascii_letters


def get_name():
    name = input("What is your name? ").strip().title()
    while not all(letter in ascii_letters + " -" for letter in name):
        name = input("Please enter a valid name: ").strip().title()
    return name

def main():
    name = get_name()
    age = input("What is your age? ")
    #print(f"Hi, my name is {name}, and I am {age} years old.")
    print(f"Your new login is: {name}_{age}")

if __name__ == "__main__":
    main()
