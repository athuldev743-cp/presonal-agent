# agent.py
import openai
from config import OPENAI_API_KEY
from tools import calculator, web_search, health, weather
from memory.memory import conversation_memory, remember, recall


openai.api_key = OPENAI_API_KEY

def process_command(command: str):
    cmd = command.lower()

    # Tool logic
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

    else:
        # Default → send to GPT model with memory context
        prompt = ""
        for user_cmd, resp in conversation_memory[-10:]:
            prompt += f"User: {user_cmd}\nAssistant: {resp}\n"
        prompt += f"User: {command}\nAssistant:"

        completion = openai.ChatCompletion.create(
            model="gpt-4o-mini",  # or gpt-3.5-turbo
            messages=[{"role": "user", "content": prompt}],
            max_tokens=200
        )

        response = completion.choices[0].message["content"]
        remember(command, response)
        return response
