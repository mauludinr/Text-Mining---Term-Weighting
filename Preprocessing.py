from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

stemmer = StemmerFactory().create_stemmer()


def tokenization(source):
    source = source.lower()
    source = source[:-2]
    source = source.replace(",", "")
    source = source.split(". ")

    documents = []
    for document in source:
        documents.append(document.split(" "))

    return documents


def filtering(documents):
    stopwords = open("stopword-list", "r")
    stopwords = stopwords.read()
    stopwords = stopwords.split("\n")

    filtered = []

    for document in documents:
        filtered.append([word for word in document if word not in stopwords])

    return filtered


def stemming(documentss):
    stemmed = []
    for document in documents:
        words = []
        for word in document:
            words.append(stemmer.stem(word))
        stemmed.append(words)

    return stemmed


def printDocs(documents):
    for document in documents:
        print(document)


def termFromDocuments(documents):
    terms = []
    for document in documents:
        terms += document

    return terms


source = open("source", "r")
source = source.read()

# for document in source:
#     print(document)
#
# for i in range(0, len(source)):
#     source[i] = stemmer.stem(source[i])
#
# print()

documents = tokenization(source)

documents = filtering(documents)

documents = stemming(documents)

terms = termFromDocuments(documents)
print(terms, len(terms))
terms = set(terms)
terms = list(terms)
print(terms, len(terms))
print()
printDocs(documents)
