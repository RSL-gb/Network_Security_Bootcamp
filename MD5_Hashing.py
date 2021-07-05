import hashlib

print("Enter a string to Enter a string to MD5 Hash:", end ="")
str_input = input()
hashed_data = hashlib.md5(str_input.encode())
print("The hexadecimal equivalent of MD5 hash is : ", end ="")
print(hashed_data.hexdigest())
