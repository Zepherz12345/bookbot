from stats import num_words, char_count, sort_count
import sys


def main():
    if len(sys.argv) != 2:
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    words_count = num_words(text)
    letter_count = char_count(text)
    sorted = sort_count(letter_count)
    print(f"============ BOOKBOT ============\nAnalyzing book found at {book_path}...")
    print(f"----------- Word Count ----------\nFound {words_count} total words")
    print("--------- Character Count -------")
    report(sorted)
    print("============= END ===============")
    
    

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def report(sorted):
    for key in sorted:
        if key.isalpha():
            print(f"{key}: {sorted[key]}")




    
main()