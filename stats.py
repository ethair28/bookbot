# this function takes in a string, splits the string into a list of words and returns the length on the list (number of words)
def word_counter(book_txt:str):
    num_of_words = len(book_txt.split())
    return num_of_words
# turns any upercase into lowercase, counts the number of charecters and returns a dict with the number of tims each catacter showed up 
def character_counter(book_txt: str) ->dict:
    txt_lowercase = book_txt.lower()
    char_count_dict = {}
    for char in txt_lowercase:
        if char in char_count_dict:
            char_count_dict[char] += 1
        else:
            char_count_dict[char] = 1
    return char_count_dict            

