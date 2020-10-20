def is_palidrom(word):
    return word.lower == word[::-1].lower
print(is_palidrom('a'))