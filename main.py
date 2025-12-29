from stats import get_num_words
from stats import get_unique_characters
from stats import sorted_characters
import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()
    
def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path_to_book = sys.argv[1]

    book_text = get_book_text(path_to_book)
    num_words = get_num_words(book_text)
    char_count = sorted_characters(get_unique_characters(book_text))
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_book}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in char_count:
        ch = item["char"]
        num = item["num"]
        if ch.isalpha():
            print(f"{ch}: {num}")
    print("============= END ===============")

main()