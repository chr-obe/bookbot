def main():
    # Setup
    BOOK_PATH = "books/frankenstein.txt"
    text = get_book_text(BOOK_PATH)
    word_count = get_num_words(text)
    print("--- Begin report ---")
    print(f"{word_count} words found in the document.")
    print(" ")
    letter_count = get_num_letters(text)
    print(f"Raw letter count: {letter_count}")
    formatted_count = get_formatted_letters(letter_count)
    print(" ")
    print_letter_report(formatted_count)
    print("--- End report ---")

def get_num_letters(text):
    lower_text = text.lower()
    letter_count = {}
    for letter in lower_text:
        if letter not in letter_count:
            letter_count[letter] = 1
        else:
            letter_count[letter] += 1
    return letter_count

def get_formatted_letters(dict):
    formatted_counts = []
    for key in dict:
        if key.isalpha():
            temp_dict = {}
            temp_dict["name"] = key
            temp_dict["count"] = dict[key]
            formatted_counts.append(temp_dict)
    return formatted_counts

def print_letter_report(letters):
    letters.sort(reverse=True, key=sort_on)
    for letter in letters:
        print(f"The '{letter["name"]}' character was found {letter["count"]} times!")

def sort_on(dict):
    return dict["count"]

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()