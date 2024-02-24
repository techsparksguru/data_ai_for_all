import glob, os, pandas as pd, pathlib, textract, time
from flair.data import Sentence
from flair.nn import Classifier
import streamlit as st
from io import StringIO
from PyPDF2 import PdfReader
import scrubadub, scrubadub_spacy, scrubadub_stanford, scrubadub_address

from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline


def flair_ner_large_entities(document):
    START = time.time()
    tagger = Classifier.load('ner-large') 
    sentence = Sentence(document)
    tagger.predict(sentence)

    person_entities = map(lambda x: x.unlabeled_identifier.split(":")[-1].replace("\"","").replace("'","").strip() if x.value =="PER" else None, sentence.get_labels())
    person_entities = [i for i in person_entities if i is not None]

    loc_entities = map(lambda x: x.unlabeled_identifier.split(":")[-1].replace("\"","").replace("'","").strip() if x.value =="LOC" else None, sentence.get_labels())
    loc_entities = [i for i in loc_entities if i is not None]

    org_entities = map(lambda x: x.unlabeled_identifier.split(":")[-1].replace("\"","").replace("'","").strip() if x.value =="ORG" else None, sentence.get_labels())
    org_entities = [i for i in org_entities if i is not None]

    output_dict = {}
    output_dict["PER"] = list(set(person_entities))
    output_dict["LOC"] = list(set(loc_entities))
    output_dict["ORG"] = list(set(org_entities))
    del tagger
    END = time.time()
    return END-START, output_dict

def scrubadub_entities(document):
    START = time.time()
    scrubber = scrubadub.Scrubber()
    output = scrubber.clean(document)
    del scrubber
    END = time.time()
    return END-START, output

def spacy_entities(document):
    START = time.time()
    scrubber = scrubadub.Scrubber()
    scrubber.add_detector(scrubadub_spacy.detectors.SpacyEntityDetector)
    output = scrubber.clean(document)
    del scrubber
    END = time.time()
    return END-START, output

def stanford_entities(document):
    START = time.time()
    scrubber = scrubadub.Scrubber()
    scrubber.add_detector(scrubadub_stanford.detectors.StanfordEntityDetector())
    output = scrubber.clean(document)
    del scrubber
    END = time.time()
    return END-START, output


def bert_entities(document):
    START = time.time()
    tokenizer = AutoTokenizer.from_pretrained("dslim/bert-base-NER")
    model = AutoModelForTokenClassification.from_pretrained("dslim/bert-base-NER")

    nlp = pipeline("ner", model=model, tokenizer=tokenizer)
    ner_results = nlp(document)
    
    person_entities = map(lambda x: x["word"] if x["entity"] in(["B-PER","I-PER"]) else None, ner_results)
    person_entities = [i for i in person_entities if i is not None]
    
    org_entities = map(lambda x: x["word"] if x["entity"] in(["B-ORG","I-ORG"]) else None, ner_results)
    org_entities = [i for i in org_entities if i is not None]
    
    loc_entities = map(lambda x: x["word"] if x["entity"] in(["B-LOC","I-LOC"]) else None, ner_results)
    loc_entities = [i for i in loc_entities if i is not None]
    
    output_dict = {}
    output_dict["PER"] = list(set(person_entities))
    output_dict["LOC"] = list(set(loc_entities))
    output_dict["ORG"] = list(set(org_entities))
    
    del model
    
    END = time.time()
    return END-START, output_dict
    