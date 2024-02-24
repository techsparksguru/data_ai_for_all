# NER extraction

In the age of GDPR, CCPA and especially with the advent of transformer-based AI solutions out there, personal identifiable information (and hence identity as a fundamental construct) and privacy take center stage. Some solutions that once required large teams, coordination, planning and testing - are **now solved with AI training** (with right labeling + RHLF) and the models learn the rules based on context and large-enough examples.  

## What is NER
A named entity is a "real-world object" that's assigned a name more importantly, a collection of objects given a common name like person, organization, location and so on. For e.g.

- Pradeep Kumar is a PERSON/NAME
- 1234 xyz street, NY, USA is a LOCATION
- Nvidia Corporation is an ORGANIZATION
- Kellogs Cereals is a PRODUCT

You can create your [own definitions](https://flairnlp.github.io/docs/tutorial-training/how-to-train-sequence-tagger) of named-entities within your data corpus and context - however there needs to be a purpose to recognize named entities. In our app, it is to identify PII and subsequently take some action (eithe redact or replace with fakes)

## Our use case 
We are trying to address concerns of sharing data with external, however PII removed/replaced

- Name of the person should be redacted or subsitited with another fake name
- Email address, phone numbers, SSN and Driver License to be removed fully
- Location / Address to be substitued with fake addresses
- The documents can be in any of doc, docx, pdf, rtf, ppt formats 
- We will use my own resume from [John Doe Resume](./john_doe.pdf)
- **Note:** I have used various other resumes and documents for batch / bulk evaluation and wrapped the same functionality into pyspark
- **Performance Metrics:** [Precision, Recall, Accuracy, F1 Score](https://developers.google.com/machine-learning/crash-course/classification/precision-and-recall) - If you are into ML , these should be no-brainer metrics for any model that you develop, consume, test in terms of performance KPIs. Before going to production, all these KPIs should be healthy.  

# Technical
- We are using Python Client libraries to solve the use case
- Execution environment is either single machine (VM/container/baremetal/cloud) , python runtime >= 3.6
- Frameworks include (not limited to) pyspark, django, fastapi, streamlit etc.
- Python libraries include (not limited to) scrubadub, scrubadub-spacy, scrubadub-stanford, transformers, flair
- You might need to get an API key from hugging face when downloading pytorch models (this repo only uses inferencing. If you are interested in building your own named entities, [reach out](pradeep@seleniumframework.com) on how we fine-tuned our own models). 

A high level opinionated results matrix below  

~[Comparisons](./comparisons.jpg)


### Instructions

#### Clone Repo

```
git clone https://github.com/techsparksguru/data_ai_for_all.git
cd generative_ai/use_cases/anonymize_piii
```

#### Create And Activate Virtual Environemnt

```
cd venv
python3 -m venv venv
source venv/bin/activate
```

#### Install Dependencies

```
pip3 install -r requirements.txt
```

#### Run The App

```
streamlit run app.py
```

# Thoughts
- Within Flair, there are many [models](https://pypi.org/project/flair/)
- Explicitly had to `del tagger` & `del scrubber` (see helpers.py file) to help with memory usage.
- Converting tokens to original input string words in transformers model is relatively easy, but I will leave that as an exercise (if you really came to that point of execution)

Please reach out if you have questions, needs and consulting [email](pradeep@seleniumframework.com)
