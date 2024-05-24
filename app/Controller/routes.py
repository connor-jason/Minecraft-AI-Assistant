from flask import Blueprint, Flask, render_template, request, jsonify
from config import Config
from ollamaTesting import ollama_chat
from speechToText import get_spoken_text
from correctText import correct_text

routes_blueprint = Blueprint("routes", __name__)
routes_blueprint.template_folder = Config.TEMPLATE_FOLDER

@routes_blueprint.route('/')
def index():
    return render_template('index.html')

# Update the question after a question is asked
@routes_blueprint.route('/update-question', methods=['POST'])
def update_question():
    text = get_spoken_text()
    if "humphrey" in text:
        argument = text.split("humphrey", 1)[1]
        return jsonify({'question': correct_text(argument)})
    
# Update the response after a question is asked and a response is returned
@routes_blueprint.route('/update-response', methods=['POST'])
def update_response():
    question = request.json.get('question', '')
    if question:
        response = ollama_chat(question)
        return jsonify({'response': response})
