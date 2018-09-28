import Preprocessing as pre
import TermWeighting as termW

source = open("source.txt", "r")
source = source.read()

documents = pre.tokenization(source)

documents = pre.filtering(documents)

documents = pre.stemming(documents)

terms = pre.termFromDocuments(documents)

logWeight = termW.logTermWeighting(terms, documents)

df = termW.documentFrequency(terms, documents)

idf = termW.inverseDocumentFrequency(df, documents)

pre.printDocs(termW.tf_idf(logWeight, idf))
