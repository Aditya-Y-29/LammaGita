import timeit
from src.utils import setup_dbqa
from streamlit_chat import message
import streamlit as st
import os
from dotenv import load_dotenv

os.environ['TOKENIZERS_PARALLELISM'] = 'true'

st.set_page_config(page_title="LLAMA GITA", page_icon=":robot_face:")
st.markdown("<h2 style='text-align: center;'> LLAMA GITA 🚀</h2>", unsafe_allow_html=True)

if 'past' not in st.session_state:
    st.session_state['past'] = []
if 'generated' not in st.session_state:
    st.session_state['generated'] = []
if 'references' not in st.session_state:
    st.session_state['references'] = []
if 'messages' not in st.session_state:
    st.session_state['messages'] = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]

    
def inference_model(prompt):
    dbqa = setup_dbqa()
    query = prompt
    start = timeit.default_timer()
    response = dbqa({'query': query})
    end = timeit.default_timer()
    answer=response["result"]
    index = answer.find("\section")
    if index != -1:
        answer = answer[:index]
        answer = answer[:-8]
    print(f'\nAnswer: {answer}')
    print(f"Time to retrieve response: {end - start}")
    print('='*50)

    # Process source documents
    source_docs = response['source_documents']
    for i, doc in enumerate(source_docs):
        print(f'\nSource Document {i+1}\n')
        print(f'Source Text: {doc.page_content}')
    
    return answer,"Reference---->\n"+doc.page_content

def generate_response(prompt):
    st.session_state['messages'].append({"role": "user", "content": prompt})
    completion,references=inference_model(prompt)
    response = completion
    st.session_state['messages'].append({"role": "assistant", "content": response})
    st.session_state['messages'].append({"role": "assistant", "content": references})
    return response,references

response_container = st.container()
container = st.container()

with container:
    with st.form(key='my_form', clear_on_submit=True):
        user_input = st.text_area("You:", key='input', height=100)
        submit_button = st.form_submit_button(label='Send')

    if submit_button and user_input:
        output,references = generate_response(user_input)
        st.session_state['past'].append(user_input)
        st.session_state['generated'].append(output)
        st.session_state['references'].append(references)

if st.session_state['generated']:
    with response_container:
        for i in range(len(st.session_state['generated'])):
            message(st.session_state["past"][i], is_user=True, key=str(i) + '_user')
            message(st.session_state["generated"][i], key=str(i))
            message(st.session_state["references"][i], key=str(i)+'_reference')

col1, col2 = st.columns([9, 10])
clear_button = st.button("Clear")
with col2:
    if clear_button:
        st.session_state['generated'] = []
        st.session_state['past'] = []
        st.session_state['references'] = []
        st.session_state['messages'] = [
            {"role": "system", "content": "You are a helpful assistant."}
        ]
    


