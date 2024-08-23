def main(): 
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(f'Words:\n {count_words(text)}\n')
    print(f'Chars:\n {char_dict(text)}\n')
    print("Thank you for using BookBot")

def char_dict(text):
    low_text = text.lower()
    char_dict = dict()
    for char in low_text:
        try:
            char_dict[char] += 1
        except:
            char_dict[char] = 1
    return char_dict

def count_words(text):
   return len(text.split())

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()