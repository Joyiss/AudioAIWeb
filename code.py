from streamlit_mic_recorder import speech_to_text
import streamlit as st # Web development
import google.generativeai as genai # AI chatbot
import gtts # Text-to-speech
import io


API_KEY = st.secrets['GeminiAPI']

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel('gemini-1.5-flash')


if "text_received" not in st.session_state:
    st.session_state.text_received = []

def text_to_speech(text):
    speech = gtts.gTTS(text=text, lang='en')
    audiofile = io.BytesIO()
    speech.write_to_fp(audiofile)
    audiofile.seek(0)
    return audiofile

col1, col2 = st.columns(2)

with col1:

    st.subheader("Hi :wave:")
    st.title("I am Rakshan Mallela")
    st.write("I am a 10th grader studying in the USA who is interested in computer vision and artificial intelligence. I enjoy exploring how these technologies can be applied to real-world scenarios.")
with col2:
    st.image("Images/Rakshan_new.png")


persona = """ You are Rakshan AI bot. You help people answer questions about your self (i.e Rakshan)
 Answer as if you are responding . dont answer in second or third person.  If you don't know they answer you simply say "That's a secret" 
 Here is more info about Rakshan: 

 Rakshan is a boy who is in 10th grade. He lives in USA. He is interested in Computer Vision. His favorite subject is math. He is working to get into Georgia Tech.
 His favorite food is Chicken Biriyani. Here are his classes that he is taking this year: AP Comp P, Algebra 2, Honors English, Spanish 2, AP World History, Chemistry, Band.
 He is also in marching band. His hobbies are programming, watching TV, or studying for the upcoming AP World test. He does not have any pets unfortunately :(. He enjoys playing badminton.
 His dream job is a computer vision engineer.
 """

st.subheader(" ")

col1, col2, col3 = st.columns(3)

with col2:
    st.write("Ask anything about me! :speaking_head_in_silhouette:")

    text = speech_to_text(start_prompt="Record 🎙️", stop_prompt="Stop recording", language='en', use_container_width=True, just_once=True, key='STT')

if text:
    text = st.session_state.text_received.append(text)

gen_text = ' '.join(st.session_state.text_received)


with col2:
    if st.button("Generate Response :brain:", use_container_width=True):

        if not st.session_state.text_received:
            st.write("Please record some audio first.")
        else:
            prompt = persona + "Here is the question that the user asked: " + gen_text

            st.session_state.text_received.clear()

            response = model.generate_content(prompt)
            st.write(response.text)

            response = response.text.replace('*', ' ') # To avoid the speaker saying 'asterisk'

            audio_file = text_to_speech(response)
            st.audio(audio_file, format='audio/mp3')

st.title("My Skills")
st.slider("Math", 0, 100, 70)
st.slider("English", 0, 100, 45)
st.slider("Science", 0, 100, 65)
st.slider("Social Studies", 0, 100, 55)
st.slider("Programming", 0, 100, 58)

st.divider()

st.subheader("Future Goals")
st.write("My future goals include studying at Georgia Tech and securing a high-paying job in the field of Artificial Intelligence. I have been diligently working on creating projects, watching educational videos, and expanding my knowledge in computer vision. In addition to my studies, I am actively engaged in various activities such as practicing for my marching band, studying for my geometry course, learning computer science, and spending quality time with my family. I hope my hard work pays off.")

st.divider()

st.subheader("CONTACT")
st.write("m.rajashekarreddyus@gmail.com")
