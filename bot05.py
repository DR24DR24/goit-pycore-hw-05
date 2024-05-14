


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return("user is present already")

    return inner

def parse_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            print("cann't parse")
            return "",""

    return inner

def change_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "user absent"
            #return "no such user"
        except ValueError:
            return "please input <change user_name>"    
    return inner

def phone_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "no such user"
        except IndexError:
            return "please input phone + user name"

    return inner




@parse_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args
 
@input_error
def add_contact(args, contacts):
    name, phone = args
    if  (name in contacts):
        raise KeyError
    contacts[name] = phone
    return "Contact added."

@change_error
def change_contact(args, contacts):
    name, phone = args
    if not (name in contacts):
        raise KeyError
    contacts[name] = phone
    return "Contact changed"
    #except IndexError : 
        

@phone_error
def phone_contact(args, contacts):
    name = args[0]
    print(contacts[name])
    return "Print contact."
    #return "cann't find contact"

def all_contact(args, contacts):
    for user, phone in contacts.items():
        print(f"user: {user} phone: {phone}")
    return "that is аll contacts."
    #print("cann't print all contacts")


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
            print(phone_contact(args, contacts)) 
        elif command == "all":
            print(all_contact(args, contacts)) 
          
    
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
