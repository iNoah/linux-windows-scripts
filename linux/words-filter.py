import argparse
import re
import enchant
#from nltk.corpus import words
#from nltk.stem import WordNetLemmatizer
from pattern.en import lemma
#from nltk.tokenize import sent_tokenize, word_tokenize
from stop_words import get_stop_words

#stop_words = get_stop_words('en')
stop_words = get_stop_words('english')
dict_en = enchant.Dict("en_US")

#ps = PorterStemmer()
#lemmatizer = WordNetLemmatizer()
parser = argparse.ArgumentParser(description='Filter words from subtitle file.')
parser.add_argument('-i', "--input", help='input')
parser.add_argument('-w', "--known", help='known words')
parser.add_argument('-f', "--format", help='format')

args = parser.parse_args()

in_filename = args.input
known_filename = args.known

def is_english_word(word):
    return dict_en.check(word)

def get_words_from_sub(filename):
    with open(filename, 'r') as f:
        file_content = f.read()
        #return sorted(set(re.findall(re.compile('[A-z]+', text.lower()))))
        words = set(re.findall(r"[A-z]+", file_content.lower()))
        lemmatized_set = set()
        for word in words:
            if is_english_word(word):
            #stem = lemmatizer.lemmatize(word)
                #le = lemma(word)
                lemmatized_set.add(lemma(word))
    return lemmatized_set

def get_words_from_known_list(filename):
    return set(line.strip() for line in open(filename))

def create_new_words_file(new_words_set):
    with open('new_words.txt', 'w') as f:
        for word in new_words_set:
            f.write("%s\n" % word)


words_in_sub = get_words_from_sub(in_filename)
words_in_known_list_list = get_words_from_known_list(known_filename)

new_words_set = words_in_sub - words_in_known_list_list

create_new_words_file(sorted(new_words_set))