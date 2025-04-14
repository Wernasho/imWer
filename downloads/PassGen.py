import random

def pass_generator():
    while True:
        characters = list("abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        xtra_chars = list("!#$%&/()=?¡'¿¡-_+*^.[]{}:;.,\\")
        history = []

        multi = input("multi-generate? (Yes/no): ").lower() 
        if multi not in ["yes", "no"]:
            print("error: Invalid input.")
            continue

        if multi == "yes":
            try:
                multi_num = int(input("Amount of passwords you wanna generate: "))
            except ValueError:
                print("Invalid number input. Retry.")
                continue

        command = input("Special characters? (#, !, =, *, etc...) (Yes/no): ").lower()
        if command not in ["yes", "no"]:
            print("Invalid. Retry")
            continue
        if command == "yes":
            characters.extend(xtra_chars)  

        try:
            length = int(input("password length (8 or higher): "))
        except ValueError:
            print("Invalid number input. Retry.")
            continue
        
        if length < 8:
            print("8 is the minimum character limit.")
            continue

        if multi == "yes":
            for _ in range(multi_num):
                password = "".join(random.choices(characters, k=length))
                print("Generated password: ", password)
                history.append(password)
        else:
            password = "".join(random.choices(characters, k=length))
            with open("passwords.txt", 'a') as p:
                p.write(f"{password}, \n")

        history_input = input("See history? (yes/no): ").lower()
        if history_input not in ["yes", "no"]:
            print("Invalid input. Retry.")
            continue
        elif history_input == "yes":
            with open("passwords.txt", 'r') as p:
                print(f"History: \n {p.read()}")
            break
        else:
            return
pass_generator()