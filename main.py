import sys
from stats import get_num_words, get_num_chars, sort_chars

def main():
    if len(sys.argv) != 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    chars = get_num_chars(sys.argv[1])
    sorted_chars = sort_chars(chars)
    print('============ BOOKBOT ============')
    print('Analyzing book found at books/frankenstein.txt...')
    print('----------- Word Count ----------')
    get_num_words(sys.argv[1])
    print('--------- Character Count -------')
    for dict in sorted_chars:
        if dict['char'].isalpha():
            print(f'{dict['char']}: {dict['num']}')
    print('============= END ===============')

main()
