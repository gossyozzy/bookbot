def get_num_words(text):
    words = text.split()
    return len(words)

def get_unique_characters(text):
    char_dict = {}
    chars = text.lower()
    for char in chars:
        char_dict[char] = char_dict.get(char, 0) + 1
    return char_dict

def sort_on(item):
    return item["num"]

def sorted_characters(dict):
    char_list = []
    for char, count in dict.items():
        char_list.append({"char": char, "num": count})
    char_list.sort(key=sort_on, reverse=True)
    return char_list