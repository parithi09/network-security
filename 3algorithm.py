#program 1 (md5 hashing)
import hashlib
input1=input("enter the string to be hashed :")
result=hashlib.md5(input1.encode())
print("the md5 hash of {} is {}".format(input1,result.hexdigest()))

#program 2 (3 algorithm)
import hashlib
input1=input("enter the string to be hashed :")
result1=hashlib.md5(input1.encode())
result2=hashlib.sha1(input1.encode())
result3=hashlib.sha224(input1.encode())
print("the md5 hash of {} is {}".format(input1,result1.hexdigest()))
print("the md5 hash of {} is {}".format(input1,result2.hexdigest()))
print("the md5 hash of {} is {}".format(input1,result3.hexdigest()))

#program 3 (salt and iteration)
import hashlib
import string
import random  
S = 5       
u_password=input("enter the password:")
for i in range(0,5):
    ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k = S))
    salt1=str(ran)+u_password
    u_password=salt1
print(u_password)
hashed=hashlib.md5(u_password.encode())
print("salted hash",hashed.hexdigest())

    
