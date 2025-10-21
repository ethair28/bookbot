from stats import word_counter, character_counter 

def get_book_txt(path_to_text: str) ->str:
    with open(path_to_text) as f:
        return f.read()
    
def main(path_to_text: str):
    book_txt = get_book_txt(path_to_text)
    num_words = word_counter(book_txt)
    num_chars_dict = character_counter(book_txt)
    print(f"Found {num_words} total words")
    print(num_chars_dict)
    return None


main('books/frankenstein.txt')       