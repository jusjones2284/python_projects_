from cryptography.fernet import Fernet



# def write_key():
#     key = Fernet.generate_key()
#     with open("key.key", "wb") as key_file:
#         key_file.write(key)

# write_key()

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

master_pwd = input("What is the master password? ")
key = load_key() + master_pwd.encode()
fer = Fernet(key)

def view():
    with open('password.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("userName:", user,", password:", fer.decrypt(passw.encode()).decode())
    

def add():
    name = input("Account Name: ")
    pwd =  input("Password: ")  
    ## w is to write over existing file that already exists
    ## r is read mode
    ## a is append mode <- add something to the end of the file or create file if one doesnt exist
    with open('password.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode().decode()))
    
    # file = open("passwords.txt, 'a")
    # file.close()

while True:
    mode = input("Woud you like to add a new password or view existing ones? (view, add? "+
                 "Press q to quit.")
    if mode ==  "q":
        exit()
    
    if mode == "view":
        view()
        quit()
    elif mode == "add": 
        add()
    else:
        print("Invalid mode. ")
        continue

