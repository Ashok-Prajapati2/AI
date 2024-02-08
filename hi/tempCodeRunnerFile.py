from bardapi import Bard
import os


os.environ['_BARD_API_KEY'] =
input_text = 'why is the sky blue?'

def make_request(input_text):
    
        response = Bard().get_answer(str(input_text))
        return response['content']
 
result = make_request(input_text)
print(result)