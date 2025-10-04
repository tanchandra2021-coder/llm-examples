from streamlit.testing.v1 import AppTest

def test_chatbot_component():
    # Load the chatbot app
    at = AppTest.from_file("Chatbot.py").run()
    assert not at.exception

    # Simulate typing a question
    at.components_v1_html[0].set_value("Do you know any jokes?").run()
    print(at)

    # Since Puter.js runs in the browser, we can't test the real AI response here.
    # But we can assert the HTML component exists and no exceptions were thrown
    assert not at.exception

