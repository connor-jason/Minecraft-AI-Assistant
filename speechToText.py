import speech_recognition as sr

def get_spoken_text():
	r = sr.Recognizer() 

	while True: 
		try:
			with sr.Microphone() as source2:
				# wait for a second to let the recognizer adjust the energy threshold based on the surrounding noise level 
				r.adjust_for_ambient_noise(source2, duration=0.5)
				
				# listens for the user's input 
				audio2 = r.listen(source2)
				
				# Using google to recognize audio
				spoken_text = r.recognize_google(audio2)
				spoken_text = spoken_text.lower()

				return spoken_text
				
		except sr.RequestError as e:
			print("Could not request results; {0}".format(e))
			
		except sr.UnknownValueError:
			pass
			# print("Unknown error occurred")
