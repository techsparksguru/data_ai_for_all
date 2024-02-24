import glob, os, pandas as pd, pathlib, textract, time
from flair.data import Sentence
from flair.nn import Classifier
import streamlit as st
from io import StringIO
from PyPDF2 import PdfReader
import scrubadub, scrubadub_spacy, scrubadub_stanford, scrubadub_address

from lib.helpers import *



with st.sidebar:
    st.title("NER Tagging")
    st.markdown('''
    ## About
    Goal is to upload a document and identify PII data - PERSON, ORGANIZATION, EMAIL, PHONE etc.
    ''')

def submit (uploaded_resume):
    if uploaded_resume is not None:
        reader = PdfReader(uploaded_resume)
        text = ""
        for page in reader.pages:
            text = text + "\n" + page.extract_text()
        
        st.header("Named Entities Identified")
        
        scrubadub, spacy, stanford, bert, flair = st.tabs(["Scrubadub", "Spacy", "Stanford","Bert-base-NER","Flair"])
        
        with scrubadub:
            elapsed, output = scrubadub_entities(text)
            st.header("Scruadub NER")
            st.header(elapsed)
            with st.container():
                st.write(output)

        with spacy:
            elapsed, output = spacy_entities(text)
            st.header("Spacy")
            st.header(elapsed)
            with st.container():
                st.write(output)

        with stanford:
            elapsed, output = stanford_entities(text)
            st.header("Stanford")
            st.header(elapsed)                             
            with st.container():
                st.write(output)
        
        with bert:
            elapsed, output = bert_entities(text)
            st.header("Bert-base-NER")
            st.header(elapsed)  
            with st.container():
                st.write(output)
        
        with flair:
            elapsed, output = flair_ner_large_entities(text)
            st.header("Flair NER Large")
            st.header(elapsed)
            with st.container():
                st.write(output)
        

def main():
    st.header("Upload a document")

    form = st.form(key='some_form')
    uploaded_resume = st.file_uploader("Upload your document", type=("pdf"))
    form.form_submit_button("Run", on_click=submit(uploaded_resume=uploaded_resume))

if __name__ == '__main__':
    main()
