import requests

url = "https://personal-agent.onrender.com/ask"
response = requests.options(url)

print("Status:", response.status_code)
print("\nHeaders:")
for k, v in response.headers.items():
    print(f"{k}: {v}")
