from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
import nltk
import string
from nltk.tokenize import word_tokenize
factory = StopWordRemoverFactory()
stopword = factory.create_stop_word_remover()
sentences = "Laskar pelangi bercerita tentang kehidupan beberapa anak di Belitong" \
          "Kisah miris dunia pendidikan di Indonesia dimana sebuah sekolah yang kekurangan murid hendak ditutup" \
          "Sekolah tersebut adalah SD Muhammadiyah di Gantung Belitung Timur." \
          "Namun, karena murid yang terdaftar genap 10, sekolah dengan bangunan seadanya tersebut tetap diijinkan beraktifitas seperti biasanya." \
          "Ke-sepuluh murid tersebut adalah para laskar pelangi."\
          "Nama yang diberikan guru mereka bernama Bu Mus, oleh karena kegemaran mereka terhadap pelangi."
sentences = sentences.translate(str.maketrans('','',string.punctuation)).lower()
stop = stopword.remove(sentences)
tokens = nltk.tokenize.word_tokenize(stop)
print(tokens)
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
factory = StemmerFactory()
stemmer = factory.create_stemmer()
words = "['laskar', 'pelangi', 'bercerita', 'tentang', 'kehidupan', 'beberapa', 'anak', 'belitong', 'kisah', 'miris', 'dunia', 'pendidikan', 'indonesia', 'dimana', 'sebuah', 'sekolah', 'kekurangan', 'murid', 'hendak', 'ditutup', 'sekolah', 'tersebut', 'adalah', 'muhammadiyah', 'gantung', 'belitung', 'timur', 'karena', 'murid', 'terdaftar', 'genap', 'sekolah', 'dengan', 'bangunan', 'seadanya', 'tetap', 'dijalankan', 'beraktifitas', 'seperti', 'biasa', 'sepuluh', 'murid', 'adalah', 'para', 'laskar', 'pelangi', 'nama', 'diberikan', 'guru', 'mereka', 'bernama', 'bu', 'mus', 'karena', 'kegemaran', 'mereka', 'terhadap', 'pelangi']"
print(words)