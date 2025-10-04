from streamlit.testing.v1 import AppTest

def test_chatbot_loads():
    at = AppTest.from_file("Chatbot.py").run()
    assert not at.exception

    # Simulate user typing a question
    at.chat_input[0].set_value("What is the best investment strategy?").run()
    print(at)

    # Can't test GPT4All output (runs locally), but we can check the chat system works
    assert not at.exception

