import requests

start_sequence = "\nMonika:"
restart_sequence = "\n\nPerson:"
session_prompt = ""

def ask(question, chat_log=None):
    prompt_text = f'{chat_log}{restart_sequence}: {question}{start_sequence}:'
    resp = requests.post(
        "https://api.ai21.com/studio/v1/j1-large/complete",
        headers={"Authorization": "Bearer 4Vyt47IveUCFO7KeDRtciO3hpHLwi4v4"},
        json={
            "prompt": prompt_text,  # f'User: {text}',
            "numResults": 1,
            "maxTokens": 50,
            "temperature": 0.0,
            "presencePenalty": {'scale': 5.0},
            "countPenalty": {'scale': 10.0},
            "frequencyPenalty": {'scale': 42.7},
        }
    )
    story = resp.json()['completions'][0]['data']['text']
    return str(story)





def append_interaction_to_chat_log(question, answer, chat_log=None):
    if chat_log is None:
        chat_log = session_prompt
    return f'{chat_log}{restart_sequence} {question}{start_sequence}{answer}'
