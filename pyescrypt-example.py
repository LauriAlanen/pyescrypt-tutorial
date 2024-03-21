from pyescrypt import Yescrypt, Mode
 
hasher = Yescrypt(n=4096, r=32, p=1, mode=Mode.MCF)

password = input("Enter password: ").encode()
salt = input("Enter salt: ").encode()

hashed = hasher.digest(password=password, salt=salt)

try:
    hasher.compare(password, hashed)
    print("Generating Hash in Modular Crypt Format (MCF)")
except WrongPasswordConfiguration:
    print("Passwords have different configurations.")
except WrongPassword:
    print("Passwords don't match.")

print(f"\nGenerated hash : {hashed.decode()}")
