import random
import string


pass_len = 8
char_value = string.ascii_letters + string.digits + string.punctuation


# List Comprehension

password = "".join ([random.choice(char_value) for i in range(pass_len)])

# password = ""
# for i in range(pass_len):
#     password += random.choice(char_value)





print("Your random password is : ",password)