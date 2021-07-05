import hashlib

print("Enter a string to Enter a string to Hash:", end="")
str_input = input()
hash_1 = hashlib.md5(str_input.encode())
result_1 = hash_1.hexdigest()
hash_2 = hashlib.sha256(result_1.encode())
result_2 = hash_2.hexdigest()
hash_3 = hashlib.sha1(result_2.encode())
print("The hexadecimal result after hash using 3 algorithms: ", end="")
print(hash_3.hexdigest())
