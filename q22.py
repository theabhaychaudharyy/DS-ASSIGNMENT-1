def find_first_non_repeating_char(string):
    char_count = {}
    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    for char in string:
        if char_count[char] == 1:
            return char
    return None
input_string = input("Enter a string: ")
first_non_repeating_char = find_first_non_repeating_char(input_string)
if first_non_repeating_char is None:
    print("There is no non-repeating character in the string.")
else:
    print("First non-repeating character:", first_non_repeating_char)
