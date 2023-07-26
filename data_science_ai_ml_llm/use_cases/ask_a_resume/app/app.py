import streamlit as st
from PyPDF2 import PdfReader
import pickle
import os
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain import HuggingFaceHub

from langchain.embeddings import HuggingFaceEmbeddings, SentenceTransformerEmbeddings
from langchain.embeddings.spacy_embeddings import SpacyEmbeddings
from langchain.embeddings import GPT4AllEmbeddings

from langchain.llms import GPT4All


with st.sidebar:
    st.title("Resume Search")
    st.markdown('''
    ## About
    Goal is to ask a natural language question and get a response from input document (resume in this case)
    ''')

def submit (uploaded_resume, query):

    if uploaded_resume:

        #Pdf Text Extraction
        pdf_reader = PdfReader(uploaded_resume)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
        
        #Text Splittting
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len
        )
        chunks = text_splitter.split_text(text=text)

        #Compute Embeddings and Vector Store 
        store_name = "myvector_store"
        if os.path.exists(f"{store_name}.pkl"):
                with open(f"{store_name}.pkl", "rb") as f:
                    vector_store = pickle.load(f)
        else:
            # embeddings = OpenAIEmbeddings(openai_api_key=api_key)
            # embedder = SpacyEmbeddings()
            embeddings = HuggingFaceEmbeddings()
            vector_store = FAISS.from_texts(chunks, embedding=embeddings)
            with open(f"{store_name}.pkl", "wb") as f:
                pickle.dump(vector_store, f)
        
        if query:
            #Accept User Queries
            docs = vector_store.similarity_search(query=query, k=2)
            # llm=HuggingFaceHub(repo_id="declare-lab/flan-alpaca-large", model_kwargs={"temperature":0, "max_length":512})
            llm = GPT4All(model="/home/ubuntu/Downloads/orca-mini-3b.ggmlv3.q4_0.bin",max_tokens=2048)
            chain = load_qa_chain(llm, chain_type="stuff")

            response = chain.run(input_documents=docs,question=query)
            st.header("AI Response")
            st.write(response)

def main():
    st.header("Ask any question on resume")

    form = st.form(key='some_form')
    uploaded_resume = form.file_uploader("Upload your resume", type=("pdf"))
    query = form.text_area(
                "Ask a question on the resume",
                placeholder="What is the email address?",
                key="question"
            )
    form.form_submit_button("Run", on_click=submit(uploaded_resume=uploaded_resume, query=query))

if __name__ == '__main__':
    main()
