alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

should_continue = True

while should_continue:
    print("Welcome to the world of encryption and decryption created by LJ")
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift % 26
    def caeser(plain_text, shift_amount):
        new_word = ""
        if direction == "encode":
            for letter in plain_text:
                if letter in alphabet:
                    prev_index = alphabet.index(letter)
                    new_index = prev_index + shift_amount
                    new_letter = alphabet[new_index]
                    new_word += new_letter  
                else:
                    new_word += letter
            print(f"The encoded text is {new_word}")
        elif direction == "decode":
            for letter_1 in plain_text:
                if letter_1 in alphabet:
                    prev_index_1 = alphabet.index(letter_1)
                    new_index_1 =  prev_index_1 - shift_amount
                    new_letter_1 = alphabet[new_index_1]
                    new_word += new_letter_1  
                else:
                    new_word += letter_1
            print(f"The decoded text is {new_word}")
        else:
            print("Invalid input. Try again")


    caeser(plain_text=text,shift_amount=shift)

    user_input = input(print("Do you want to use it again? Type Y for yes or N for no"))
    if user_input == "Y":
        should_continue = True
    else:
        should_continue = False