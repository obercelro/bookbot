import sys, os
from stats import count_words, count_chars, sort_char_dict

def get_book_text(filepath):
    with open(filepath) as f:
        text = f.read()
        return text

def print_char_dict(path, word_count, sorted_char_dict):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in sorted_char_dict:
        if item['char'].isalpha():
            print(f"{item['char']}: {item['num']}")
    print("============= END ===============")


if __name__ == "__main__":
    cwd = os.getcwd()
    if len(sys.argv) > 1:
        filepath = str(sys.argv[1])
        if filepath[0] != "/":
            filepath = os.path.join(cwd, filepath)
        get_book_text(filepath)
    else:
        filepath = os.path.join(cwd, "books/frankenstein.txt")
        book = get_book_text(filepath)
        wc = count_words(book)
        scd = sort_char_dict(count_chars(book))
        print_char_dict(filepath, wc, scd)

