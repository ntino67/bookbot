import sys
from stats import count_words
from stats import count_characters
from stats import print_report
from stats import sort_dict


def get_book_text(filepath):
    file_contents = ""
    with open(filepath) as f:
        file_contents = f.read()

    return file_contents


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_text = get_book_text(sys.argv[1])
    num_words = count_words(book_text)
    # print(f"{num_words} words found in the document")
    char_count = count_characters(book_text)
    sorted = sort_dict(char_count)
    print_report(num_words, sorted, sys.argv[1])


main()
