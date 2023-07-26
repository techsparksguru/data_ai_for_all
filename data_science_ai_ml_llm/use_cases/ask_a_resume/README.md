# Ask Resume

Recruiters in HRTech industry / head hunters deal with enormouse amounts of data in job descriptions and resumes. Matching a job description with resume has many stages and predominantly recruiters gather keywords (their own understanding which can be limited) from job description, and hunt for those in job resumes to get to the next step of reaching out to candidates. Few noteworthy points
- The speed at which a recruiter works is a function of their domain knowledge, human  extraction of keywords / semantic forms (e.g. "java" is semantic to spring framework)
- There is generally 1000 to 10k resumes for some jobs and humanly applying the first filter (aka. first pass filter to potentially narrows down resumes) might take days to weeks even for the most experienced recruiter
- Any human can make errors when matching and their own biases come into play when applying the first filter (errors can be not matching "spring boot" to "java" OR filtering out the resume because they don't find "java" mentioned enough number of times etc.)
- Result can be loss of excellent talent, time delay = $ cost and many more  

<strong>For the first pass filter i.e </strong> <i>looking for a keyword in a resume in the form of question-answering</i> and augment the human search with LLM + AI semantic search</strong> seems a great start

- We will use my own resume from [linkedin](https://www.linkedin.com/in/pradeepmacharla/)
- Note: The pdf version is not available in this repo, instead use your own resume

# Technical
- Implements the same workflow model that [privateGPT](https://github.com/imartinez/privateGPT) has done and packaged into a nice python script (Path1: ingest documents > Tokenize > Embeddings/Vectors > VectorStore , Path2: Input Query > Embed and find similarity score using vecstore store > Pass this as context to LLM > Respond)
- privateGPT uses duckdb, we are using FAISS and pickling (very much like sqlite)
- <strong>Ubuntu 20.04 OS with no GPU is used for this</strong> on 8gb ram, 4 cpus
- Python 3.10.12 has been used as you can see in POC notebook (It doesn't matter whether you manage runtime with pyenv or conda - both should produce identical results)
- The below libraries and frameworks are used in this notebook and app.py  
- Most of the code is adopted from [blog](https://blog.streamlit.io/langchain-tutorial-4-build-an-ask-the-doc-app/)
- We did not use OPENAI though because most of them might not want to end up spending $ when doing POC for self or learning. 
- Huggingface account is needed as we download a model, however once downloaded we no longer need it
- There are many parameters and hyper parameter values that we chose (e.g. max_tokens) - Knowing which value to set is highly dependent on domain and use case

### Instructions

#### Clone Repo

```
git clone https://github.com/techsparksguru/data_ai_for_all.git
cd generative_ai/use_cases/ask_a_resume
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

### POC with notebook

Open the [notebook](./POC.ipynb)

#### Run The App

```
streamlit run app.py
```

# Thoughts
- As you can see , this is a very simple codebase demonstrating the power of chaining LLM capabilities with AI/ML models and creating solutions - that otherwise in the non-LLM world be a software development project, define requirement & rules, get a bunch of developers, kick off project, test etc.
- I am by no means saying we can eliminate all of the above, but building an entire pipeline to show success is far easier now
- Choosing right set of parameters, fine tuning the model with custom data, model versioning, data versioning and overall MLOps (dataops + modelops + devops) is definitely required for scaling and productionizing such apps  

Please reach out if you have questions, needs and consulting [email](pradeep@seleniumframework.com)
