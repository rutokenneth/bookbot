content = None
def get_content():
    '''
    This function reads the content of the frankenstein.txt file
    '''
    with open('books/frankenstein.txt', 'r') as f:
        content = f.read()
        return content
        

def main():
    text = get_content()
    print(text)

if __name__ == '__main__':
    main()
