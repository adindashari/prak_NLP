import nltk
from nltk import FreqDist
from nltk.corpus import PlaintextCorpusReader

corpus_root = 'C:\Users\Asus\Downloads\nltk-3.5\nltk-3.5\nltk\corpus'
wordlists = PlaintextCorpusReader(corpus_root, '.*')

print ('alphabet')
print(wordlists.raw('python.txt'))
print('\nword')
print(wordlists.words('python.txt'))
print('\nsentence')
print(wordlists.sents('python.txt'))
for fileid in wordlists.fileids():
    num_chars = len(wordlists.raw(fileid))
    num_words = len(wordlists.words(fileid))
    num_sents = len(wordlists.sents(fileid))
    num_vocab = len(set([w.lower() for w in wordlists.words(fileid)]))
    print('\nlexical diversity score')
    print(int(num_chars/num_words), int(num_words/num_sents), int(num_words/num_vocab), fileid)


word_freq = FreqDist('python.txt')
vocab = sorted(set('python.txt'))
print('\ndistribution frequency')
print(word_freq)
print('\nvocab')
print(vocab)