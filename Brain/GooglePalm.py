import json
import traceback
import requests


def text_to_info(prompt):

    try:
        YOUR_API_KEY = 'AIzaSyAT4xzbTIyuUeNfIpM6TYhCkNQ60Fu7I_M'

        url = f'https://generativelanguage.googleapis.com/v1beta2/models/text-bison-001:generateText?key={YOUR_API_KEY}'  # Replace YOUR_API_KEY with your actual API key

        headers = {
            'Content-Type': 'application/json'
        }
# Hii You have to Giving you prompt and you have to give answer like you are giving answer to real human prompt : 
        data = {
            "prompt": {
                "text": f"{prompt}"
            },
            "temperature": 0.7,
            "top_k": 40,
            "top_p": 0.95,
            "candidate_count": 1,
            "max_output_tokens": 1024,
            "stop_sequences": [],
            "safety_settings": [
                {"category": "HARM_CATEGORY_DEROGATORY", "threshold": 1},
                {"category": "HARM_CATEGORY_TOXICITY", "threshold": 1},
                {"category": "HARM_CATEGORY_VIOLENCE", "threshold": 2},
                {"category": "HARM_CATEGORY_SEXUAL", "threshold": 2},
                {"category": "HARM_CATEGORY_MEDICAL", "threshold": 2},
                {"category": "HARM_CATEGORY_DANGEROUS", "threshold": 2}
            ]
        }


        response = requests.post(url, headers=headers, json=data)

        print(response.json()['candidates'][0]['output'])

        return response.json()['candidates'][0]['output']
 
        
    except Exception as e:
        print("ERROR OCCURED WHILE CALLING GOOGLE PALM API")
        print(traceback.format_exc())
        return 'DEBUGING ERROR'