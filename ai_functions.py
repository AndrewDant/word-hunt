import openai
import config
openai.api_key = config.OPENAI_API_KEY

def word_hunt_query(user_input):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="I am trying to think of a word. List five words or short phrases that match the following: {}".format(user_input),
        temperature=0.55,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0)
    return response['choices'][0]['text']
