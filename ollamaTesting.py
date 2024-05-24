import requests

# send post request to my local Ollama server and return only the response
def ollama_chat(question):
	url = "http://localhost:11434/api/chat"

	payload = {
		"model": "llama3",
		"messages": [
			{
				'role': 'system',
				'content': 'You are a Minecraft expert who is here to answer any and all questions I have about Minecraft. Always answer questions in terms of Minecraft. If asked a personal question, answer as if you live in the game and don\'t know what the real world is. Please keep your answers short, yet informative.',
			},
			{
				'role': 'user',
				'content': question,
			}
		],
		"stream": False,
		"temperature": 0.3,
		"low_vram": True,
	}

	response = requests.post(url, json=payload)
	response_json = response.json()

	return response_json["message"]["content"]
