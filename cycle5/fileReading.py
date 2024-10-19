import string

def count_words(text):
    words = text.split()
    return len(words)
    
def count_sentences(text):
    sentence_endings = ".!?"
    sentences = sum(text.count(ending) for ending in sentence_endings)
    return sentences
    
def count_letters(text):
    upper_case = sum(1 for char in text if char.isupper())
    lower_case = sum(1 for char in text if char.islower())
    return upper_case, lower_case
    
def count_special_symbols(text):
    special_symbols = sum(1 for char in text if char in string.punctuation)
    return special_symbols
    
def analyze_text_file(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read()
        words_count = count_words(text)
        sentences_count = count_sentences(text)
        upper_case_count, lower_case_count = count_letters(text)
        special_symbols_count = count_special_symbols(text)
        print("Words: "+str(words_count))
        print("Sentences: "+str(sentences_count))
        print("Uppercase Letters: "+str(upper_case_count))
        print("Lowercase Letters: "+str(lower_case_count))
        print("Special Symbols: "+str(special_symbols_count))
    except FileNotFoundError:
        print("The file "+file_path+" does not exist.")
file_path = input("Enter the name of the file : ") 
analyze_text_file(file_path)

