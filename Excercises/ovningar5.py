def practice_one():
    user_word = input("Please enter a word, and i will count how long it is.")
    print(f"The word is {len(user_word)} letters long")

    uppercase = 0
    lowercase = 0
    
    for letters in user_word:
        if  letters.isupper():
            uppercase += 1
        if letters.islower():
            lowercase += 1              

    print(f"We can see {uppercase} capital letters and {lowercase} lower case letters.")

def practice_two():
    sentence = "A picture says more than a thousand words, a matematical formula says more than a thousant pictures."
    print(f"{len(sentence.split())}")

def practice_three():
    user_word = input("This is a palindrome checker, please enter a word to see if it's a palindrome: ").lower()
    if user_word == user_word[::-1]:
        print(f"{user_word} is a palindrome!")
    else:
        print(f"{user_word} was not a palindrome")

def practice_four():
    vowels = ["a","e","i","o","u","y","å","ä","ö"]
    sentence = "Pure mathematics is, in its way , the poetry of logical ideas"          
    number_of_vowels = 0

    for letters in sentence.lower():
        if letters in vowels:
            number_of_vowels += 1    

    print(f"We found {number_of_vowels} vowels.")

def shift_character(char, alfabet, shift_value, mode):
        
        if mode == "encryption":
            shift = +shift_value
        elif mode == "decryption":
            shift = -shift_value    

        original_position = alfabet.index(char)
        new_position = (original_position + shift) % len(alfabet)
        shifted_char = alfabet[new_position]
        return shifted_char


def practice_five():
    alfabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖ"
    alfabet_lower = "abcdefghijklmnopqrstuvwxyzåäö"
    user_mode = input("Do you want to encrypt or decrypt? (e/d))")
    if user_mode == "e":
        mode = "encryption"
    elif user_mode == "d":
        mode = "decryption"
    user_shift = int(input("Enter shift value (integer)"))        
    user_string = input("Please enter a text to decrypt: ")
    new_string = ""

    for i in range(len(user_string)):
        char = user_string[i]

        if char in alfabet_upper:
            new_string += shift_character(char, alfabet_upper,user_shift, mode)
        elif char in alfabet_lower:
            new_string += shift_character(char, alfabet_lower,user_shift, mode)
        else:
            new_string += char        

    print(f"Din nya sträng är {new_string}")
            


if __name__ == "__main__":
    practice_five()
