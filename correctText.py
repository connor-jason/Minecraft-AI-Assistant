from transformers import pipeline
import os

# avoid a warning I was getting
os.environ["TOKENIZERS_PARALLELISM"] = "false"

# load the pipeline with the NLP model
pipe = pipeline("text2text-generation", model="Finnish-NLP/t5-small-nl24-casing-punctuation-correction", max_length=100)

def correct_text(input_text):
    corrected_text = pipe(input_text)[0]['generated_text']
    return corrected_text
