
def main():
    book_path = "books/frankenstein.txt"

    book_report(book_path)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(book):
    words = book.split()
    count = len(words)
    return count

def count_letters(book):
    lowered = book.lower()
    letters = {}
    for i in lowered:
        if i.isalpha():
            letters[i] = letters.get(i,0)+1
    return letters

def book_report(path):
    print(f"--- Begin report of {path} ---");
    
    text = get_book_text(path)

    word_count = count_words(text)
    print(f"{word_count} words found in the document\n")

    letter_count = count_letters(text)
    letter_count = dict(sorted(letter_count.items(), key=lambda x:x[1], reverse=True))

    for key, value in letter_count.items():
        print(f"The '{key}' character was found {value} times")

    print("--- End report ---")

main()

