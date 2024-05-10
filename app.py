import random
import streamlit as st

st.title('🔢 Guess the Number')
picture, head = st.columns([0.5, 1])
picture.image("./images/image1.jpg", width=200, )
head.write('This is a number guessing game. You have to guess a number between 1 and the maximum range you set.' 
           ' You will be given a score based on the number of tries you take to guess the number. The maximum score is 100. Good luck!')
st.write("---")  

def get_number(length: int) -> int:
    return random.randint(1, length)

def init(length: int = 100, post_init=False):
    if not post_init:
        st.session_state.input = 0
        st.session_state.win = 0
    st.session_state.number = get_number(length)
    st.session_state.score = 100
    st.session_state.tries = 0
    st.session_state.over = False

def restart():
    init(st.session_state.length, post_init=True)
    st.session_state.input += 1


def number_guesser():

    if 'number' not in st.session_state:
       init()
    
    reset, victory, set_range = st.columns([0.39, 1, 1])

    reset.button('New game', on_click=restart)

    with set_range.expander('Settings'):
        st.slider('Set max range', min_value=10, max_value=1000, value=
                        100, key='length', on_change=restart)
    
    placeholder, result = st.empty(), st.empty()
    user_guess = placeholder.number_input(f'Enter your guess from 1 - {st.session_state.length}', key=st.session_state.input, min_value=0,
            max_value=st.session_state.length)
    
    if user_guess:
        st.session_state.tries += 1
        st.session_state.score -= 1
        if user_guess < st.session_state.number:
            result.warning(f'{user_guess} is too low!', icon="⚠️")
        elif user_guess > st.session_state.number:
            result.warning(f'{user_guess} is too high!', icon="⚠️")
        else:
            result.success(f'Good job! You guessed it right, it took you {st.session_state.tries} tries 👏! Your score is {st.session_state.score}!👏')
            st.balloons()
            st.session_state.over = True
            st.session_state.win += 1
            placeholder.empty()

    victory.button(f'🏆{st.session_state.win}')


if __name__ == '__main__':
    number_guesser()
