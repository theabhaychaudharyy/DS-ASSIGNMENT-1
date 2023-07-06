def remove_vowels(string):
    vowels = 'aeiouAEIOU'
    new_string = ''
    for char in string:
        if char not in vowels:
            new_string += char
    return new_string
input_string = input("Enter a string: ")
string_without_vowels = remove_vowels(input_string)
print("String without vowels:", string_without_vowels)
