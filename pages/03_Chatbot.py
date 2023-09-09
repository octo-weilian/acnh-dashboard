from src import *
from src.model import question_to_nsql

def toggle():
    if st.session_state.button:
        st.session_state.button = False
    else:
        st.session_state.button = True

#create chat history container
if "button" not in st.session_state:
    st.session_state.button = True

#create chat history container
if "api_key" not in st.session_state:
    st.session_state.api_key = None

with st.expander("",expanded=st.session_state.button):
    
    left_col,right_col =st.columns(2,gap='large')

    image_url = "https://media.tenor.com/v6yJvSgxAUAAAAAC/isabelle-animal-crossing.gif"
    image_html = f'''
    <p align="center">
    <img width=100% style=" margin-top:5%;border-radius:2%;box-shadow: rgba(149, 157, 165, 0.3) 0px 8px 24px" src="{image_url}">
    </p>
    '''

    model_options = ['NumbersStation/nsql-350M','NumbersStation/nsql-2B']

    with right_col:
        st.markdown(image_html, unsafe_allow_html=True)
    
    with left_col:
        st.header("Chatbot")
        username = st.text_input(label="Username", placeholder="Enter your name")
        st.session_state.api_key = st.text_input('Hugging Face API Token', type='password', placeholder="Starts with 'hf_'")
        model = st.selectbox("Model", options=model_options)
        submit = st.button("Enter",on_click=toggle)

if not st.session_state.button:

    avatars = {"user01":"https://ssb.wiki.gallery/images/thumb/e/eb/Villager_SSB4.png/250px-Villager_SSB4.png",
           'ai':"https://acnhcdn.com/latest/NpcIcon/brd02.png"}


    #create chat history container
    if "messages" not in st.session_state:
        st.session_state.messages = []

    with st.chat_message("ai",avatar=avatars['ai']):
        response = "Hey! Ask me anything about the catalog. I'll try to give a response in SQL."
        st.success(f'**AI** says:\n\n{response}\n\n*{get_ts()}*')

    #show chat history
    for message in st.session_state.messages:
        with st.chat_message(name=message["role"],avatar=avatars[message["role"]]):
            if message["role"] == "user01":
                st.info(message["content"])
            elif message["role"] == 'ai':
                st.success(message["content"])

    if prompt:=st.chat_input('Ask a question'):

        #show user chat
        with st.chat_message(name="user01",avatar=avatars["user01"]):
            user_msg = f'**{username}** says:\n\n{prompt}\n\n*{get_ts()}*'
            st.info(user_msg)
            st.session_state.messages.append({"role": "user01", "content": user_msg})
            
        #get ai response
        response = question_to_nsql(question=prompt,engine=alchemy_engine,hf_api_key=st.session_state.api_key)
        with st.chat_message("ai",avatar=avatars['ai']):
            ai_msg = f'**AI** says:\n\n{response}\n\n*{get_ts()}*'
            st.success(ai_msg)
            if type(response)==str:
                st.dataframe(get_data(response))

            st.session_state.messages.append({"role": "ai", "content": ai_msg})



      
    

    

    