from stats import word_counter, character_counter, dict_to_sorted_list

def get_book_text(filepath: str):
    with open(filepath) as f:
        text = f.read()
        return text

def main():
    raw_text = get_book_text("./books/frankenstein.txt")
    if not raw_text:
        print("Error: text could not be read.")
    word_count = word_counter(raw_text)
    character_count = character_counter(raw_text)
    sorted_alpha_count = dict_to_sorted_list(character_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at /books/frankenstein.txt")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for alpha_and_count in sorted_alpha_count:
        for alpha, count in alpha_and_count.items():
            print(f"{alpha}: {count}")
    print("============= END ===============")
    
main()