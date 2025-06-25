import streamlit as st
from pdf_parser import parse_and_chunk
from ner_topic import enrich_chunks
from vector_store import store_enriched_chunks
from rag_pipeline import answer_query,load_db

def setup_rag():
    chunk = parse_and_chunk("/home/sanskar/week4project/Insurance_Handbook_20103.pdf")
    enriched = enrich_chunks(chunk)
    store_enriched_chunks(enriched)
    return load_db()
indices,texts,metadata = setup_rag()

st.set_page_config(page_title = "pdf_chatbot",layout = "centered")
st.title("insurance handbook chatbot")
if "messages" not in st.session_state:
    st.session_state.messages = []
for msg in st.session_state.message:
    with st.chat_message(msg['role']):
        st.markdown(msg['content'])
query = st.chat_input("ask about handbook")
if query:
    st.chat_message("user").markdown(query)
    st.session_state.messages.append({"role": "user", "content": query})
    with st.spinner("thinking:"):
        answer = answer_query(query, indices, texts, metadata)
    
    st.chat_message("assistant").markdown(answer)
    st.session_state.messages.append({"role": "assistant", "content": answer})

