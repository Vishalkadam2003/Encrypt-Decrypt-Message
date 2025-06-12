alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n',
         'o','p','q','r','s','t','u','v','w','x','y','z']
"""print(" CAESER CYPHER")
text = input("Enter the Messege : ").lower()
shift = int(input("Enter the shifting value : "))
direction = input("Type the 'encode' to encrypt and 'decode' to decrypt:\n").lower()
number = [1,2,3,4,5,6,7,8,9,0]
symbols = ['!','@','#','$','%','^','&','*','(',')','-','_','+','=']"""
def cypher(original_text, shift_amount, encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1
    for letter in original_text:
        if letter == number:
            output_text += letter
        if letter == symbols:
            output_text += letter
        if letter in alpha:  # Only shift if letter is in alphabet
            position = alpha.index(letter)
            new_position = (position + shift_amount) % len(alpha)
            output_text += alpha[new_position]
        else:
            output_text += letter  # Keep symbols, spaces unchanged
    print(f"Here is your {encode_or_decode}d result: {output_text}")


should_continue = True
while should_continue:
    print(" CAESER CYPHER")
    text = input("Enter the Messege : ").lower()
    shift = int(input("Enter the shifting value : "))
    direction = input("Type the 'encode' to encrypt and 'decode' to decrypt:\n").lower()
    number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=']

    cypher(text,shift,direction)
    a = input("Type again if you want to do again,else no \n").lower()
    if a == "no":
        should_continue = False
        print("Goodbye")
