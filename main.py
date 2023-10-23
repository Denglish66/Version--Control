# Dana English
def encode(password):
    encoded_password = ""
    for number in password:
        added_number = str((int(number) + 3) % 10)  # add each number by 3
        encoded_password += added_number
    return encoded_password


# Matthew Dam Decodes password
def decode(password):
    # Converts each char in the password string to a list
    password = list(password)
    # Loops through password list
    for i in range(len(password)):
        # If password - 3 is less than 0
        if int(password[i]) - 3 < 0:
            password[i] = str((int(password[i]) - 3) + 10)
        # Subtracts 3 from encoded_password otherwise
        else:
            password[i] = str(int(password[i]) - 3)
    # Returns joined password list as a string
    return "".join(password)


def main():
    # Looping until quit
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        print("")
        choice = input("Please enter an option: ")

        if choice == "1":
            password = input("Please enter your password to encode: ")
            encoded_password = encode(password)
            print("Your password has been encoded and stored!")
            print("")

        elif choice == "2":
            print(
                f"The encoded password is {encoded_password}, and the original password is {decode(encoded_password)}\n")
        elif choice == "3":
            break


if __name__ == '__main__':
    main()
