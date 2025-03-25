import os
import requests
import time
import random
import signal
import sys
import threading
from dotenv import load_dotenv

load_dotenv()

class HyperbolicBot:
    def __init__(self, api_key, model="meta-llama/Meta-Llama-3.1-8B-Instruct"):
        self.URL = "https://api.hyperbolic.xyz/v1/chat/completions"
        self.HEADERS = {
            "Content-Type": "application/json", 
            "Authorization": f"Bearer {api_key}"
        }
        self.model = model

    def generate_random_question(self):
        topics = [
            "technology", "science", "history", "health", "space", "AI", "finance", "travel", "sports", "food",
            "education", "psychology", "philosophy", "nature", "entertainment", "medicine", "biology", "physics",
            "economics", "politics", "literature", "engineering", "artificial intelligence", "climate change", "geography",
            "mathematics", "robotics", "social media", "cybersecurity", "ethics", "mental health", "astronomy", "quantum mechanics"
        ]
        actions = [
            "explain", "describe", "tell me about", "how does", "what is", "why is", "what are the benefits of",
            "what are the challenges of", "what are the latest developments in", "how can we improve", "how does it impact society",
            "what are the risks of", "how does it compare to", "what are some interesting facts about"
        ]
        
        specifics = [
            "in modern society", "in the next decade", "for beginners", "for experts", "in simple terms", "in detail", "with examples",
            "from a historical perspective", "from a scientific perspective", "in the context of business", "in education", "in healthcare"
        ]
        
        topic = random.choice(topics)
        action = random.choice(actions)
        specific = random.choice(specifics)
        return f"{action} {topic} {specific}?"

    def send_chat_request(self, question):
        data = {
            "messages": [
                {
                    "role": "user",
                    "content": question
                }
            ],
            "model": self.model,
            "max_tokens": 2048,
            "temperature": 0.7,
            "top_p": 0.9
        }
        
        try:
            response = requests.post(self.URL, headers=self.HEADERS, json=data)
            response.raise_for_status()
            result = response.json()
            answer = result['choices'][0]['message']['content']
            return answer
        except Exception as e:
            return f"Error: {str(e)}"

    def run_chat_bot(self, bot_id):
        print(f"Starting automated chat bot {bot_id}...")
        question_count = 0
        
        while True:
            question = self.generate_random_question()
            question_count += 1
            
            print(f"\nBot {bot_id} - Question {question_count}: {question}")
            answer = self.send_chat_request(question)
            print(f"Bot {bot_id} - Answer: {answer}")
            
            delay = random.uniform(60, 120)
            print(f"Bot {bot_id} waiting {delay:.1f} seconds before next question...")
            time.sleep(delay)

def main():
    api_keys = []
   
    i = 1
    while True:
        api_key = os.getenv(f'HYPERBOLIC_API_KEY_{i}')
        if not api_key:
            break
        api_keys.append(api_key)
        i += 1

    if not api_keys:
        print("Tidak ada API key yang ditemukan. Pastikan Anda sudah mengatur .env")
        sys.exit(1)

    
    bot_threads = []

    
    def signal_handler(sig, frame):
        print("\nProgram dihentikan oleh pengguna. Keluar...")
        sys.exit(0)

    signal.signal(signal.SIGINT, signal_handler)


    for i, api_key in enumerate(api_keys, 1):
        bot = HyperbolicBot(api_key)
        thread = threading.Thread(target=bot.run_chat_bot, args=(i,), daemon=True)
        thread.start()
        bot_threads.append(thread)

    
    for thread in bot_threads:
        thread.join()

if __name__ == "__main__":
    main()
