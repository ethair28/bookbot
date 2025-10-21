from stats import word_counter, character_counter, sort_on, dict_to_sort_list, dis_clean_data 

def get_book_txt(path_to_text: str) ->str:
    with open(path_to_text) as f:
        return f.read()
    
def main(path_to_text: str):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_text}...")
    print("----------- Word Count ----------")
    book_txt = get_book_txt(path_to_text)
    num_words = word_counter(book_txt)
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    num_chars_dict = character_counter(book_txt)
    sorted_list = dict_to_sort_list(num_chars_dict)
    dis_clean_data(sorted_list)
    print("============= END ===============")
    return None


main('books/frankenstein.txt')       