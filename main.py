from stats import get_word_count, create_character_statistics
import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def report(path_to_file):
    text = get_book_text(path_to_file)

    print("============ BOOKBOT ============")
    print("Analyzing book found at", path_to_file)

    word_count = get_word_count(text)
    print("----------- Word Count ----------")
    print("Found", get_word_count(text), "total words")

    formatted_stats =  create_character_statistics(text)
    print("--------- Character Count -------")
    for stat in formatted_stats:
        if stat["character"].isalpha():
            print(stat["character"], stat["num"], sep=": ")


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
    else:
        report(sys.argv[1])

main()
