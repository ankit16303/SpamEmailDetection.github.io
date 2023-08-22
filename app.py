from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import streamlit as st
import pickle
import string
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.probability import FreqDist
from nltk.tokenize.treebank import TreebankWordDetokenizer

ps = PorterStemmer()

# Function to transform and preprocess text


def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)


# Load the trained model and vectorizer
tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))

# TextRank-based extractive summarization


def summarize_text(text, num_sentences=3):
    sentences = sent_tokenize(text)
    words = word_tokenize(text)

    words = [word for word in words if word.lower(
    ) not in stopwords.words('english')]

    fdist = FreqDist(words)

    sentence_scores = {}
    for sentence in sentences:
        for word in word_tokenize(sentence.lower()):
            if word in fdist:
                if len(sentence.split()) < 30:
                    if sentence not in sentence_scores:
                        sentence_scores[sentence] = fdist[word]
                    else:
                        sentence_scores[sentence] += fdist[word]

    selected_sentences = sorted(
        sentence_scores, key=sentence_scores.get, reverse=True)[:num_sentences]
    summarized_text = TreebankWordDetokenizer().detokenize(selected_sentences)
    return summarized_text


st.title("Spam Shield : Email/SMS Spam Classifier")

input_sms = st.text_area("Enter the message")

if st.button('Predict'):
    transformed_sms = transform_text(input_sms)
    vector_input = tfidf.transform([transformed_sms])
    result = model.predict(vector_input)[0]
    if result == 1:
        st.header("Spam")
    else:
        st.header(" Not a Spam")

if st.button('Summarize'):
    if input_sms:
        summarized_text = summarize_text(input_sms)
        st.write("Summarized Text:")
        st.write(summarized_text)
