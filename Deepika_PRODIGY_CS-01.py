""" Task-01 Implement Caesar Cipher Create a Python program that can encrypt and decrypt
 text using the Caesar Cipher algorithm. Allow users to input a message and a shift value
  to perform encryption and decryption."""

def encrypt_text(plaintext, n):
    ans = ""
    # iterate over the given text
    for i in range(len(plaintext)):
        ch = plaintext[i]

        # check if space is there then simply add space
        if ch == " ":
            ans += " "
        # check if a character is uppercase then encrypt it accordingly
        elif (ch.isupper()):
            ans += chr((ord(ch) + n - 65) % 26 + 65)
        # check if a character is lowercase then encrypt it accordingly

        else:
            ans += chr((ord(ch) + n - 97) % 26 + 97)

    return ans


plaintext =input()
n = int(input())
print("Plain Text is : " + plaintext)

print("Shift pattern is : " + str(n))

print("Cipher Text is : " + encrypt_text(plaintext, n))
