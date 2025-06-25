# 🤖 RAG PDF Chatbot

Chat with large PDFs using Google's Gemini API, FAISS for retrieval, and Streamlit for an interactive chatbot interface. Built for fast, accurate, and contextual document question answering.

---

## 📁 Project Structure

```bash
rag-chatbot/
├── app/                        # All main source code lives here
│   ├── main.py                 # Streamlit chat app entry point
│   ├── pdf_parser.py           # PDF reading & chunking logic
│   ├── ner_topic.py            # Adds entity and topic metadata
│   ├── vector_store.py         # FAISS-based vector storage
│   └── rag_pipeline.py         # Query + context + answer logic
│
├── faiss_index/                # Saved FAISS vector store & metadata
│   ├── index.faiss
│   ├── metadata.json
│   └── texts.json
│
├── data/                       # Input data like PDF files
│   └── Insurance_Handbook.pdf
│
├── .env.example                # Sample environment file (DO NOT commit secrets!)
├── requirements.txt            # Python dependencies
├── Dockerfile                  # Docker image build instructions
├── .gitignore                  # Ignored files & folders
└── README.md                   # You're reading i

```
## 📁 setup instruction
clone repositry 
```bash
git clone https://github.com/sanskar133/week4project.git
```
then go to main folder
```bash
cd WEEK4PROJECT
```
## 2. Create and Activate a Virtual Environment
```bash
python -m venv env
#activate virtual enviroe=ment
source env/bin/activate
```
## 3. Install the Required Python Packages
```bash
pip install -r requirements.txt
```
## 4. run the following command
```bash
uvicorn app.main:app --reload
```
## 5. copy the link to hit fast api then there a go to swagger using by adding /docs

## 6 click chat endpoint there click try it out then  query write your query in str format then execute it