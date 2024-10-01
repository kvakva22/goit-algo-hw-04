def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    try:
        name, phone = args
        contacts[name] = phone
        return "Contact added."
    except ValueError:
        return f"Введені дані '{' '.join(args)}' не відповідають формату: Ім'я номер "

def change_contact(args, contacts):
    name, new_phone = args 
    contacts[name] = new_phone
    return "Contact updated"

def show_phone(args, contacts):
    try:
        name = args[0]
        phone = contacts.get(name)
        if phone: 
            return phone
        else: 
            return "Ім'я не знайдено"
    except IndexError:
        return f"Ви не ввели ім'я "

def show_all(contacts):
    result = []
    for key, value in contacts.items():
        result.append(f"{key}: {value}")
    return '\n'.join(result)
    
def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
