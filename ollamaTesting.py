import requests
import shelve

# send post request to my local Ollama server and return only the response
def ollama_chat(question):
	with shelve.open('ollama_cache.db') as cache:
		if question in cache:
			return cache[question]

		url = "http://localhost:11434/api/chat"

		payload = {
			"model": "llama3",
			"messages": [
				{
					'role': 'system',
					'content': 'You are a Minecraft guru, ready to assist with any questions about the game. Whether it\'s how to craft specific items, strategies for surviving and thriving, building techniques, or understanding game mechanics, provide expert advice. Answer with clarity, ensuring the user can easily follow your guidance. Please be concise with your answers, as I will be reading them as I play. Don\'t include a lot of fluff in your answer, the information is the important part here.',
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
		answer = response_json["message"]["content"]
		cache[question] = answer
	
	return answer
			