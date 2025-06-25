from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter

def parse_and_chunk(pdf_path):
    reader = PdfReader(pdf_path)
    text = "\n".join([page.extract_text() for page in reader.pages])
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_text(text)
    return chunks

