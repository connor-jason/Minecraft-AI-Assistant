import ollama

def ollama_chat(question):
	res = ollama.chat(
		model="llama3",
		messages=[
			{
				'role': 'system',
				'content': 'You are a Minecraft expert who is here to answer any and all questions I have about Minecraft. Please keep your answers short and to the point. Include necessary details to answer my question. No yapping.',
			},
			{
				'role': 'user',
				'content': question,
			}
		],
		stream=False,
	)

	return res['message']['content']

	# for chunk in res:
	# 	yield chunk['message']['content']

	# for chunk in res:
	# 	print(chunk['message']['content'], end='', flush=True)