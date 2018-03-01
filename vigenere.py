def alphabet_position(letter):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    alpha_upper = alpha.upper()
    alpha_index = ""

    for char in letter:
        if char == " ":
            alpha_index = alpha_index + " "
        elif char not in alpha and char not in alpha_upper:
            alpha_index = alpha_index + char
        else:
            if char in alpha:
                alpha_index = alpha.index(char)
            else:
                alpha_index = alpha_upper.index(char)



    return alpha_index

def rotate_character(char, rot):
    alpha_index = alphabet_position(char)
    rotated = rot
    alpha = "abcdefghijklmnopqrstuvwxyz"
    alpha_upper = alpha.upper()
    encrypted = ""

    for i in char:
        if i == " ":
            encrypted = encrypted + " "
        elif i not in alpha and i not in alpha_upper:
            encrypted = encrypted + i

        else:
            rotated_index = alpha_index + rotated
            if rotated_index < 26 and i in alpha:
                encrypted = encrypted + alpha[rotated_index]
            elif rotated_index < 26 and i in alpha_upper:
                encrypted = encrypted + alpha_upper[rotated_index]
            elif i in alpha:
                encrypted = encrypted + alpha[rotated_index % 26]
            else:
                encrypted = encrypted + alpha_upper[rotated_index % 26]


    return encrypted

def encrypt(text, rot):
    rotated_index = 0
    final_encrypt = ""

    for i in rot:
        rotated_index = alphabet_position(i)
    for char in text:
        final_encrypt = final_encrypt + rotate_character(char, rotated_index)


    return rotated_index

def main():
    #message = input("Type a message:")
    #rotate = input("Rotate by:")
    print(encrypt("The crow flies at midnight!", "boom"))

if __name__ == "__main__":
    main()