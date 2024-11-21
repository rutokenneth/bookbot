content = None
def get_content():
    '''
    This function reads the content of the frankenstein.txt file
    '''
    with open('books/frankenstein.txt', 'r') as f:
        content = f.read()
        return content
        
def word_count():
    text = get_content()
    words = text.split()
    return len(words)

def char_count():
    letter_count = {}
    book_text = get_content()
    for char in book_text:
        char = char.lower()
        if char.isalpha():
            letter_count[char] = letter_count.get(char, 0) + 1
        # print(letter_count)#debug line
    for letter, count in letter_count.items():
        print(f"The letter '{letter}' appears {count} times.")
    return letter_count
    
def generate_report():
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"77986 words found in the document\n")
    sorted_val = dict(sorted(char_count().items(), key= lambda item: item[1], reverse=True))
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"77986 words found in the document")
    
    for k, v in sorted_val.items():
        print(f"The '{k}' character was found {v} times")
    print("\n--- End report ---")

def main():
    text = get_content()
    print(text)
    # word count
    num_words = word_count()
    print(num_words)
    # number of occurence of individual characters
    char_count()
    generate_report()

if __name__ == '__main__':
    main()
