from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import bahasa
news_txt = "Data pribadi dan informasi penting merupakan sasaran empuk bagi para hacker. Pasalnya, hacker akan memanfaatkan celah keamanan untuk mencuri data dan memanfaatkannya untuk hal-hal yang merugikan Anda. Tak heran jika keamanan data menjadi perhatian khusus bagi para pelaku bisnis dan usaha, sehingga mereka bersedia untuk melakukan berbagai hal demi mengamankannya. Salah satunya saja seperti IBM Storage Server Indonesia, yang bisa membantu Anda untuk meningkatkan sekuritas data penting dari tangan-tangan tak bertanggung jawab." \
           "Nah, untuk Anda yang ingin mengamankan data digital dari serangan hacker, beberapa hal ini bisa dilakukan:" \


stopwords = set(stopwords.words(bahasa))
words = word_tokenize(news_txt)

freqTable = dict()

for word in words:
    word = word.lower()
    if word in stopWords:
        continue
        if word in freqTable:
            freqTable[word] += 1
        else:
            freqTable[word] = 1


sentences = sent_tokenize(news_txt)
sentenceValue = dict()
for sentence in sentences:
    for word, freq in freqTable.items():
        if word in sentence.lower():
            if sentence in sentenceValue:
                sentenceValue[sentence] += freq
            else:
                sentenceValue[sentence] = freq

sumValues = 0
for sentence in sentenceValue:
    sumValues += sentenceValue[sentence]


average = int(sumValues / len(sentenceValue))

summary = ''
for sentence in sentences:
    if (sentence in sentenceValue) and (sentenceValue[sentence] > (1.2 * average)):
        summary += "" + sentence


print(summary)