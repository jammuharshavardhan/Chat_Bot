import google.generativeai as genai

genai.configure(api_key="AIzaSyDjeP9-Uho_ZKJp4Aaiu3C4grBzW5c9R8k")

models = genai.list_models()

print("Available models:")
for model in models:
    print(model.name, model.supported_generation_methods)
