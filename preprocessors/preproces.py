from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
import nltk
from nltk.tokenize import word_tokenize
import re
import string

class Preprocessor:
  def caseFolding(self, text):
    lowerCase = text.lower()
    numRemoved = re.sub(r"\d+", "", lowerCase)
    puncRemoved = numRemoved.translate(str.maketrans("", "", string.punctuation))
    return puncRemoved.strip()

  def stopWordRemoving(self, text):
    stopwordList = StopWordRemoverFactory().get_stop_words()
    result = list()
    tokens = word_tokenize(text)
    for token in tokens:
      if token not in stopwordList:
        result.append(token)
    return ' '.join(result)

  def stemming(self, text):
    stemmer = StemmerFactory().create_stemmer()
    return stemmer.stem(text)

  def filtering(self, text):
    text = self.stemming(self.caseFolding(text))
    text = text.replace('sy', '')
    text = text.replace('tp', 'tapi')
    text = text.replace('tdk', 'tidak')
    text = text.replace('tll', 'terlalu')
    text = text.replace('tidak bagus', 'jelek')
    text = text.replace('tidak jelek', 'bagus')
    text = text.replace('tidak kecewa', 'suka')
    text = text.replace('tidak suka', 'kecewa')
    text = text.replace('muas', 'puas')
    text = text.replace('tidak puas', 'kecewa')
    text = text.replace('tidak senang', 'kecewa')
    text = text.replace('tidak enak', 'kecewa')
    text = text.replace('tidak buruk', 'bagus')

    return text