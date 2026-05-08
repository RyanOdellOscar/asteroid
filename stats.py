def get_num_words(text):
    words = text.split()
    return len(words)

def count_character_appearances(text):
    char_count = {}
    for char in text:
        if char.isalpha():  # Consider only alphabetic characters
            char = char.lower()
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sort_on(items):
    return items["num"]

def get_char_list(char_dictionary):
    char_list = []
    for key in char_dictionary:
        char_list.append({"char": key, "num": char_dictionary[key]})
    char_list.sort(key=sort_on, reverse=True)
    return char_list