import openai
import os
from dotenv import load_dotenv
import logging
from colorama import Fore, Style

class ChatAgent:
    def __init__(self):
        self.client = None
        self.thread = None

    def process_chat(self, user_input, file_ids=None):
        # user_input = 'Say hi to me'
        # Check if client is initialized
        if not self.client:
            raise Exception("Client not initialized. Call open_client first.")
        
        # Create a message with the user input and attached files
        completion = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": user_input}
            ]
        )

        logging.info(f"{Fore.MAGENTA}Processing skeleton document{Style.RESET_ALL}")
        return completion.choices[0].message

    def open_client(self):
        load_dotenv()
        api_key = os.getenv("OPENAI_KEY_PROMPTS")
        if not api_key:
            raise Exception("API key not found in environment variables.")
        
        self.client = openai.Client(api_key=api_key)
        logging.info(f"{Fore.MAGENTA}Welcome to OpenAI...{Style.RESET_ALL}\n")
        
        return self.client

    def open_thread(self):
        if not self.client:
            raise Exception("Client not initialized. Call open_client first.")
        
        logging.debug("Waking up...")
        self.thread = self.client.beta.threads.create()
        logging.info(f"{Fore.MAGENTA}Welcome to the Lecture Notes JSON assistant...{Style.RESET_ALL}\n")
        return self.thread

    def wake_up(self):
        self.open_client()
        self.open_thread()
        
        return self.client, self.thread

# Example usage
if __name__ == "__main__":
    agent = ChatAgent()
    agent.wake_up()
    response = agent.process_chat("Say hi to me.")
    print(response)
