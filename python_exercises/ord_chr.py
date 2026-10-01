# september 30, 2026 | it is only a caesar cipher encryption
# print(ucp)
# X = 88, A = 65 | x = 120, a = 97
# Y = 89, B = 66 | y = 121, b = 98
# Z = 90, C = 67 | z = 122, c = 99

caesar_characters=[]
xyz= {88:65,
      89:66,
      90:67,
      120:97,
      121:98,
      122:99}

words=input("Enter a word: ")
ucp_word=[ord(char) for char in words]

for n in ucp_word:
    if n in xyz:
        n=xyz[n]
        caesar_characters.append(n)
        continue
    n+=3
    caesar_characters.append(n)
    print(n)

ucp_char=[chr(num) for num in caesar_characters]

print("Your inputted word in caesar cipher is... ")
print(ucp_char)