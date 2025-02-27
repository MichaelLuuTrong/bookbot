from stats import word_counter, character_counter, dict_to_sorted_list
import sys

def get_book_text(filepath: str):
    with open(filepath) as f:
        text = f.read()
        return text

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        return
    raw_text = get_book_text(sys.argv[1])
    if not raw_text:
        print("Error: text could not be read.")
    word_count = word_counter(raw_text)
    character_count = character_counter(raw_text)
    sorted_alpha_count = dict_to_sorted_list(character_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for alpha_and_count in sorted_alpha_count:
        for alpha, count in alpha_and_count.items():
            print(f"{alpha}: {count}")
    print("============= END ===============")

main()