import random

wrong_answers = [
    "The Earth is flat and made of cheese.",
    "2 + 2 equals 5.",
    "Water boils at 10°C if you believe hard enough.",
    "The moon is a hologram controlled by penguins.",
    "Sharks are actually vegetables."
]

print("🤖 WrongChatGPT - Ask me anything, I will always be wrong!")
while True:
    question = input("\nYou: ")
    if question.lower() in ["exit", "quit", "bye"]:
        print("🤖 WrongChatGPT: Goodbye! Remember, I'm never right!")
        break
    print("🤖 WrongChatGPT:", random.choice(wrong_answers))
