from stats import word_counter

def get_book_text(filepath: str):
    with open(filepath) as f:
        text = f.read()
        return text

def main():
    raw_text = get_book_text("./books/frankenstein.txt")
    if not raw_text:
        print("Error: text could not be read.")
    word_count = word_counter(raw_text)
    print(f"{word_count} words found in the document")
    
main()