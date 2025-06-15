def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents


def get_num_words(txt):
    book = get_book_text(txt)
    num_words = len(book.split())
    print(f'Found {num_words} total words')

def get_num_chars(txt):
    chars = {}
    book = get_book_text(txt).lower()
    for char in book:
        if char not in chars:
            chars[char] = 1
        else:
            chars[char] += 1
    return chars

def sort_chars(dict):
    listed_dicts = []
    for key in dict:
        new_pairs = {}
        new_pairs['char'] = key
        new_pairs['num']  = dict[key]
        listed_dicts.append(new_pairs)
    
    def sort_on(dict):
        return dict["num"]
    listed_dicts.sort(reverse=True, key=sort_on)    
    return listed_dicts
