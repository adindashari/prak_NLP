import re # modul regular expression
import requests # untuk library mengirim permintaan HTTP
from nltk.corpus import stopwords #untuk mengahapus kata umum
from nltk.tokenize import word_tokenize, sent_tokenize #penggunaan case folding
from bs4 import BeautifulSoup # Library yang digunakan untuk melakukan ekstraksi file dengan format XML atau HTML


# 1
headers = {
    'User-Agent': 'Chrome/39.0.2171.95 (Windows NT 10.0; WOW64; rv:55.0) Gecko/20100101 Firefox/55.0',
}
req = requests.get(
    'https://www.liputan6.com/tekno/read/4548651/serangan-ransomware-di-rumah-sakit-antara-hidup-dan-mati', headers=headers)
soup = BeautifulSoup(req.content, "html.parser")

# 2
par_soup_title = soup.find('h1').text

# 3
baris = 0
teks = ""
for par_soup_body in soup.find_all('p'):
    if baris > 0:
        teks += par_soup_body.get_text()
    baris += 1
stopwords = set(stopwords.words("indonesian"))

# 4
words = word_tokenize(teks)

# 5
freqTable = dict()
for word in words:
    word = word.lower()
    if word in stopwords:
        continue
    if word in freqTable:
        freqTable[word] += 1
    else:
        freqTable[word] = 1


# 6
sentences = sent_tokenize(teks)
sentenceValue = dict() # membuat variabel kamus kosongan

# 7
for sentence in sentences:
    for word, freq in freqTable.items():
        if word in sentence.lower():
            if sentence in sentenceValue:
                sentenceValue[sentence] += freq
            else:
                sentenceValue[sentence] = freq

# 8
sumValues = 0
for sentence in sentenceValue:
    sumValues += sentenceValue[sentence]

# 9
average = int(sumValues / len(sentenceValue))

# 10
summary = ''
for sentence in sentences:
    if(sentence in sentenceValue) and (sentenceValue[sentence] > (1.2 * average)):
        summary += " " + sentence

# 11
summary = re.sub('[^a-zA-Z0-9 \n\.\,]', '', summary)

# 12
print(par_soup_title)
print("\n")
print(summary)
