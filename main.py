def main():
    BOOK_PATH = "books/frankenstein.txt"
    text = get_book_text(BOOK_PATH)
    word_count = get_num_words(text)
    print(f"{word_count} words found in the document.")
    
def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()
main()