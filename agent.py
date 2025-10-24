# agent.py
from openai import OpenAI
from tools import calculator, web_search, health, weather
from memory.memory import conversation_memory, remember, recall

# Initialize OpenAI client
client = OpenAI(api_key="YOUR_OPENAI_API_KEY")  # replace with your actual key

def process_command(command: str):
    cmd = command.lower()

    # === Built-in tools ===
    if "calculate" in cmd:
        response = calculator.calculate(command)
        remember(command, response)
        return response

    elif "tell me about" in cmd:
        response = web_search.search_wikipedia(command)
        remember(command, response)
        return response

    elif "heart rate" in cmd:
        try:
            rate = int(cmd.split()[-1])
            response = health.check_heart_rate(rate)
        except:
            response = "Please provide the heart rate as a number."
        remember(command, response)
        return response

    elif "recall" in cmd:
        query = command.replace("recall", "").strip()
        response = recall(query)
        return response

    elif "weather" in cmd:
        city = command.lower().replace("weather in", "").strip()
        if not city:
            return "Please tell me the city name, e.g., 'weather in London'"
        response = weather.get_weather(city)
        remember(command, response)
        return response

    # === Chat with OpenAI ===
    else:
        # Prepare conversation context (last 10 interactions)
        messages = []
        for i, (user_cmd, resp) in enumerate(conversation_memory[-10:]):
            messages.append({"role": "user", "content": user_cmd})
            messages.append({"role": "assistant", "content": resp})
        messages.append({"role": "user", "content": command})

        try:
            response_obj = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=messages,
                max_tokens=200
            )

            # Access the content safely
            chat_choice = response_obj.choices[0]
            if hasattr(chat_choice, "message"):
                response = chat_choice.message.content
            else:
                response = str(chat_choice)

        except Exception as e:
            response = f"❌ Jarvis AI: Error processing command: {str(e)}"

        remember(command, response)
        return response
