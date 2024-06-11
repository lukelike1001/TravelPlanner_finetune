import os
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

# Your HuggingFace API token
api_token = os.getenv("HUGGINGFACE_API_KEY")

# Model and tokenizer
model_name = "xingyaoww/CodeActAgent-Mistral-7b-v0.1"

# Initialize the tokenizer and model
tokenizer = AutoTokenizer.from_pretrained(model_name, use_auth_token=api_token)
model = AutoModelForCausalLM.from_pretrained(model_name, use_auth_token=api_token)

# Initialize the pipeline
generator = pipeline('text-generation', model=model, tokenizer=tokenizer)

# Define the input prompt
prompt = "Translate the following English text to French: 'Hello, how are you?'"

# Generate the text
outputs = generator(prompt, max_length=50, num_return_sequences=1)

# Print the output
for i, output in enumerate(outputs):
    print(f"Output {i + 1}: {output['generated_text']}")
