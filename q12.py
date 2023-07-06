def is_anagram(str1, str2):
    if len(str1) != len(str2):
        return False
    char_count = {}
    for char in str1:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    for char in str2:
        if char in char_count:
            char_count[char] -= 1
        else:
            return False
    for count in char_count.values():
        if count != 0:
            return False
    return True
input_str1 = input("Enter the first string: ")
input_str2 = input("Enter the second string: ")

if is_anagram(input_str1, input_str2):
    print("The two strings are anagrams.")
else:
    print("The two strings are not anagrams.")
