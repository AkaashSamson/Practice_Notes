from ollama import chat

response = chat(
    model='llama3.2-vision:11b',
    messages=[{
        'role': 'user',
        'content': 'Describe this image in detail.',
        'images': ['process.png']
    }]
)

print(response['message']['content'])
