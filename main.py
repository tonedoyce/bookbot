def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    words = file_contents.split()
    print(len(words))

    lowered_file = file_contents.lower()

    charcount = dict()
    for char in lowered_file:
    
        try:
            charcount[char] += 1
        except:
            charcount[char] = 1
    
    print(charcount)
        


main()

