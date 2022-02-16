# Sending the credentials to env
import google.cloud.dialogflow_v2 as dialogflow
import dotenv
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "client.json"

# Import dotenv for creds
dotenv.load_dotenv()

#import dialogflow
dialogflow_session_client = dialogflow.SessionsClient()
PROJECT_ID = os.environ["PROJECT_ID"]


def _detect_intent_from_text(text, session_id=12345, language_code="en"):
    session = dialogflow_session_client.session_path(PROJECT_ID, session_id)
    text_input = dialogflow.types.TextInput(
        text=text, language_code=language_code)
    query_input = dialogflow.types.QueryInput(text=text_input)
    response = dialogflow_session_client.detect_intent(
        session=session, query_input=query_input)
    return response.query_result


def get_reply(query, chat_id):
    response = _detect_intent_from_text(query, chat_id)

    if response.intent.display_name == "get_news":
        return "get_news", dict(response.parameters)
    else:
        return "small_talk", response.fulfillment_text
