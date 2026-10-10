# a simple caesar cipher encryption/decryption with shift of 3
def encrypt():
    words=input("Enter a word to encrypt: ")
    ucp_word=[ord(char) for char in words]
    caesar_characters=[]
    xyz= {88:65,
        89:66,
        90:67,
        120:97,
        121:98,
        122:99}
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


def decrypt():
    words=input("Enter a word to encrypt: ")
    ucp_word=[ord(char) for char in words]
    caesar_characters=[]
    abc= {97:120,
          98:121,
          99:122,
          65:88,
          66:89,
          67:90
    }
    for n in ucp_word:
        if n in abc:
            n=abc[n]
            caesar_characters.append(n)
            continue
        n-=3
        caesar_characters.append(n)
        print(n)

    ucp_char=[chr(num) for num in caesar_characters]

    print("Your inputted word in caesar cipher is... ")
    print(ucp_char)

while True:
    choice=input("Would you like to encrypt or decrypt a string? (1 for encrypt, 2 for decrypt, 0 for exit): ")
    match choice:
        case "1":
            encrypt()
        case "2":
            decrypt()
        case "0":
            print("Thank you. Exiting program...")
            break
        case _:
            print("Invalid please try again.")