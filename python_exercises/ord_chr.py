# py_str="Python"

# ucp=[ord(char) for char in py_str]

# print(ucp)

caesar_characters=[]

words=input("Enter a word: ")
ucp_word=[ord(char) for char in words]

for n in ucp_word:
    n+=3
    caesar_characters.append(n)
    print(n)

ucp_char=[chr(num) for num in caesar_characters]

print("Your inputted word in caesar cipher is... ")
print(ucp_char)