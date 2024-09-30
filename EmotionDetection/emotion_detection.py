'''Emotion analysis tool'''
import json
import requests

# Function to run emotion detection using Watson NLP libraries
def emotion_detector(text_to_analyze):
    # URL of the emotion analysis service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    # Headers specifying the model ID for the emotion analysis service
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    # Constructing the request payload in the expected format
    payload = { "raw_document" : { "text" : text_to_analyze } }
    # Sending a POST request to the sentiment analysis API
    response = requests.post(url, json=payload, headers=headers, timeout=20)
    # Handling status_code 400 for no input
    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    # Formatting the response to return a dictionary containing emotion analysis results
    formatted_response = json.loads(response.text)
    formatted_result=formatted_response['emotionPredictions'][0]['emotion']
    dominant_emotion=""
    dominant_score=0
    for emotion, score in formatted_result.items():
        if score > dominant_score:
            dominant_emotion=emotion
            dominant_score=score
    formatted_result['dominant_emotion']=dominant_emotion
    return formatted_result
