def main():
    book_path = "books/frankenstein.txt"
    report(book_path)

def get_book_text(path):
    with open(path) as f:
        text = f.read()
        return text

def word_count(text):
    words = text.split()
    return len(words)

def number_of_letters(text):
    letter_dic = {}
    words = text.lower()
    for char in words:
        if char in letter_dic:
            letter_dic[char] += 1
        else:
            letter_dic[char] = 1
    return letter_dic

def sort_on(dict):
    return dict[1]
        

def report(path):
    text = get_book_text(path)
    letter_dic =  number_of_letters(text)
    sort_dic = dict(sorted(letter_dic.items(), key=sort_on, reverse=True))
    print(f"--- Begin report of {path} ---")
    print(f"{word_count(text)} words found in the document\n")
    for letter in sort_dic:
        if letter.isalpha():
            print(f"The charaacter '{letter}' was found {letter_dic[letter]} times")
    
    print("--- End report ---")
            
            

main()