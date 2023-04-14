import nltk
import gensim
import matplotlib.pyplot as plt

s=' I am student. I study UrSU.'

sentences=[]
for sent in nltk.sent_tokenize(s):
    sentence=[]
    for w in nltk.word_tokenize(sent):
        if(w.isalpha()):
            sentence.append(w.lower())
    sentences.append(sentence)

print(sentences)

model=gensim.models.word2vec.Word2Vec(sentences, min_count=1, vector_size=2)

x=[]
y=[]
for sent in sentences:
    for word in sent:
        print(word,' : ',model.wv[word])
        x.append(model.wv[word][0])
        y.append(model.wv[word][1])


plt.scatter(x,y)
plt.show()

#plt.scatter(point)
#plt.show()

#print(model.wv['i'])


