from cryptography.fernet import Fernet
key = Fernet.generate_key()
with open('key.key', 'wb') as f:
    f.write(key)
fernet = Fernet(key)
with open ('Python.png','rb') as f:
    Photo = f.read()
    
lock = fernet.encrypt(Photo) 
with open('Python.png', 'wb') as lock_Photo:
    lock_Photo.write(lock)
print('Your Photo is Locked!') 
    
    