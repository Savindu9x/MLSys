import streamlit as st

def write_response(txt):
  output_str = "Your resolution for:" + str(txt)
  return output_str

st.set_page_config(page_title="Custom knowledge Base Bot", page_icon=":bar_chart:",layout="wide")
st.title(" 	:bar_chart: DevOps AI Assistant")
st.markdown('<style>div.block-container{padding-top:1rem;}</style>',unsafe_allow_html=True)

input_query = st.text_area('Enter Your Incident Below (maximum 300 words):', key="user_query_state", height=100)

col1, col2 = st.columns([1,12])
with col1:
    st.button('Generate', on_click=on_submit_click)
with col2:
    st.button('Clear', on_click=on_clear_click)

