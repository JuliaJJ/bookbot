import sys
from stats import get_num_words
from stats import get_char_count
from stats import sort_char_count

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        contents = f.read()
    return contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    path_to_file = sys.argv[1]
    contents = get_book_text(path_to_file)
    word_count = get_num_words(contents)
    char_count = get_char_count(contents)
    char_count_sorted = sort_char_count(char_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for entry in char_count_sorted:
        if entry["char"].isalpha():
            print(f"{entry['char']}: {entry['num']}")
    print("============= END ===============")

main()