from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot("SimpleBot",
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///database.sqlite3',
    logic_adapters=[
        {
            "import_path": "chatterbot.logic.BestMatch",
            "default_response": "I'm still learning. Could you rephrase that?",
            "maximum_similarity_threshold": 0.65
        }
    ],
    preprocessors=[
        'chatterbot.preprocessors.clean_whitespace'
    ]
)

# Training data
trainer = ListTrainer(chatbot)
trainer.train([
    "Hello", "Hi there! How can I help you today?",
    "Goodbye", "See you later!",
    "How are you?", "I'm just a program, but thanks for asking!",
    "What's your purpose?", "I'm here to chat and learn from you!"
])

# Rest of the code remains the same...
# Conversation loop with error handling
exit_commands = ("exit", "quit", ":q")
print("Chatbot activated! Type 'exit' to end")

while True:
    try:
        user_input = input("You: ")
        if user_input.lower() in exit_commands:
            print("Bot: Goodbye!")
            break
            
        response = chatbot.get_response(user_input)
        print(f"Bot: {response}")
        
    except (KeyboardInterrupt, EOFError):
        print("\nSession ended unexpectedly")
        break