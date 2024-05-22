from flask import Flask, render_template, request, jsonify
from ollamaTesting import ollama_chat
from speechToText import get_spoken_text

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# Update the question after a question is asked
@app.route('/update-question', methods=['POST'])
def update_question():
    text = get_spoken_text()
    if "humphrey" in text:
        argument = text.split("humphrey", 1)[1]
        return jsonify({'question': argument})
    else:
        return jsonify({'question': ''})
    
# Update the response after a question is asked and a response is returned
@app.route('/update-response', methods=['POST'])
def update_response():
    question = request.json.get('question', '')
    if question:
        response = ollama_chat(question)
        return jsonify({'response': response})
    else:
        return jsonify({'response': ''})

if __name__ == '__main__':
    app.run(debug=True)
