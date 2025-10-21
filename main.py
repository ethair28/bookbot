def get_book_txt(path_to_text):
    with open(path_to_text) as f:
        return f.read()

def word_counter(book_txt):
    num_of_words = len(book_txt.split())
    return num_of_words

def main(path_to_text):
    book_txt = get_book_txt(path_to_text)
    num_words = word_counter(book_txt)
    print(f"Found {num_words} total words")
    return None


main('books/frankenstein.txt')       