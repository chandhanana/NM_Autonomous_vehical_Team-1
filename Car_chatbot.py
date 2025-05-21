import random
import re

# Basic tokenizer using regex
def simple_tokenize(text):
    return re.findall(r'\b\w+\b', text.lower())

# Car knowledge base
car_knowledge = {
    "fuel": ["Fuel level is at 65%.", "Fuel tank is more than half full."],
    "battery": ["Battery charge is 90%.", "Battery condition is good."],
    "abs": ["ABS prevents wheel lock during braking. It's a safety system."],
    "engine": ["It’s a 4-cylinder petrol engine.", "The engine is running smoothly."],
    "brakes": ["Brakes are in excellent condition — front disc, rear drum."],
    "gearbox": ["Gearbox helps transfer engine power to wheels."],
    "tire": ["All tires are inflated to 32 PSI.", "Tire pressure is optimal."],
    "speed": ["You’re driving at 45 km/h.", "Current speed is moderate."],
    "status": ["Vehicle is operating normally.", "All systems are green."]
}

# Chat function
def car_bot():
    print("🚗 Welcome to the Car Assistant Bot!")
    print("Ask me about fuel, battery, engine, brakes, etc.")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Bot: Bye! Drive safely 🏁")
            break

        tokens = simple_tokenize(user_input)
        found = False

        for keyword in car_knowledge:
            if keyword in tokens:
                print("Bot:", random.choice(car_knowledge[keyword]))
                found = True
                break

        if not found:
            print("Bot: 🤖 I'm not sure about that. Try asking about fuel, battery, brakes, etc.")

# Run the bot
if __name__ == "__main__":
    car_bot()
