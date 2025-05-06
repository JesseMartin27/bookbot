
def num_words(text):
    words = text.split()
    return len(words)
    ##print len(words)

def count_chars(text):
    lowercase = text.lower()
    char_count = {}

    for char in lowercase:
        if char in char_count:
        # character already in dictionary then add count
            char_count[char] += 1
        else:
            char_count[char] = 1

    
    return char_count
   # return len(words)

##def sort_on(x):
    x = sorted(count_chars)
    return x

def sort_on(dict):
    return dict["num"]

def chars_to_sorted_list(char_count):
    char_list = [
        {"char": c, "num": n}
        for c, n in char_count.items()
        if c.isalpha()
    ]
    # sort using the helper function
    char_list.sort(reverse=True, key=sort_on)
    return char_list
