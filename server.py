''' Executing this function initiates the emotion detection application
    to be executed over the Flask channel and deployed on localhost:5000.
'''
# Import Flask, render_template, request from the Flask framework package
from flask import Flask, render_template, request
# Import the emotion_detection function from the package
from EmotionDetection.emotion_detection import emotion_detector

# Initiate the Flask app
app = Flask("Emotion Detector")

# Implement the necessary decorators

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application page over the Flask channel
    '''
    return render_template("index.html")

@app.route("/emotionDetector")
def get_emotions():
    ''' This code receives the text from the HTML interface and runs emotion detection over it using 
    emotion_detector() function. The output returned is displayed according to set requirements.
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    result = emotion_detector(text_to_analyze)
    emotions_phrase = ""
    for emotion, score in result.items():
        if emotion != 'dominant_emotion':
            emotions_phrase = emotions_phrase + f"{emotion}: {score}, "
    emotions_phrase = emotions_phrase[:-2]
    closing_phrase = f". The dominant emotion is <b>{result['dominant_emotion']}</b>."
    result_phrase = f"For the given statement, the system response is {emotions_phrase}{closing_phrase}"
    return result_phrase

if __name__ == "__main__":
    # This functions executes the flask app and deploys it on localhost:5000
    app.run(debug=True, host="0.0.0.0", port=5000)
