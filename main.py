def get_book_text(filepath: str):
    with open(filepath) as f:
        text = f.read()
        return text

def word_counter(text: str):
    individual_words = text.split()
    word_count = 0
    for word in individual_words:
        word_count += 1
    print(individual_words)
    return word_count

def main():
    raw_text = get_book_text("./books/frankenstein.txt")
    word_count = word_counter(raw_text)
    print(f"{word_count} words found in the document")
    



main()