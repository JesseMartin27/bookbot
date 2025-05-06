from stats import count_chars, chars_to_sorted_list, num_words
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    # check if a book path was provided
    if len(sys.argv)< 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

# Use the command-line argument as the book path
    path = sys.argv[1]
    
    full_text = get_book_text(path)
    word_count = num_words(full_text)
    char_count = count_chars(full_text)
    sorted_order = chars_to_sorted_list(char_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")


     # Print each character and its count
    for char_dict in sorted_order:
        print(f"{char_dict['char']}: {char_dict['num']}")
    
    # Print the footer
    print("============= END ===============")





main()