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
    for letter, count in letter_count.items():
        print(f"The letter '{letter}' appears {count} times.")
    

def main():
    text = get_content()
    print(text)
    # word count
    num_words = word_count()
    print(num_words)
    char_count()

if __name__ == '__main__':
    main()
