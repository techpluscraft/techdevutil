def add_numbers(num1,num2):
    return num1 + num2

def subtract_numbers(num1,num2):
    return num1 - num2

def multiply_numbers(num1,num2):
    return num1 * num2

def divide_numbers(num1,num2):
    return num1 / num2

def palindrome(word):
    wordlength = len(word)
    reversedword=word[wordlength::-1]
    if word == reversedword:
        return(f"{word} is a palindrome")
    else:
        return(f"{word} is not a palindrome")

def remove_spaces(field):
    return(field.split( ))