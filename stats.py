def get_num_words(contents):
    words = contents.split()
    word_count = len(words)
    return word_count

def get_char_count(contents):
    char_count = {}
    contents_lower = contents.lower()
    for char in contents_lower:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sort_char_count(char_count):
    char_count_sorted = []
    def char_value(item):
        return item[1]
    
    char_count_list = list(char_count.items())
    char_count_list.sort(key=char_value, reverse=True)

    for pair in char_count_list:
        built_pair = {"char": pair[0], "num": pair[1]}
        char_count_sorted.append(built_pair)
    return char_count_sorted