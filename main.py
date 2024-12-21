# getting book text
def book_text(book):
    with open(book) as b:
        return b.read()
    

# getting text word count
def text_word_count(text):
    splitted_str = text.split()
    return len(splitted_str)

    
# getting text char count as dictionary
def text_char_count(text):
    char_dict = {}

    for char in text.lower():
        if char in char_dict:
            char_dict[char] += 1
        else:   
            char_dict[char] = 1

    return char_dict


# removing non alphabetical characters and sorting count decreasingly
def sort_dict(char_count):
    new_dict = {}
    for key, value in char_count.items():
        if key.isalpha():
            new_dict[key] = value
    new_dict = dict(sorted(new_dict.items(), key=lambda item: item[1], reverse=True))
    
    return new_dict




def main():
    book="books/frankenstein.txt"
    
    text = book_text(book)
    word_count = text_word_count(text)
    char_count = text_char_count(text)
    sorted_dict = sort_dict(char_count)


    print(f"--- Here is the report for {book} ---")
    print(f"{word_count} words found in the book.")
    print(f"\n")
    for char, count in sorted_dict.items():
        print(f"Found '{char}' {count} times")
    print(f"\n")
    print(f"--- Have a nice day ---")


main()