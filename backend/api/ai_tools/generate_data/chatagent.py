import openai
import os
import logging
import numpy as np
from dotenv import load_dotenv
from colorama import Fore, Style

class GPTAgent:
    def __init__(self):
        self.client = None

    def open_client(self):
        load_dotenv()
        api_key = os.getenv("OPENAI_KEY_PROMPTS")
        if not api_key:
            raise Exception("API key not found in environment variables.")
        
        self.client = openai.Client(api_key=api_key)
        logging.info(f"{Fore.MAGENTA}Welcome to OpenAI...{Style.RESET_ALL}\n")
        
        return self.client

class EmbeddingAgent(GPTAgent):
    # Function to generate embeddings using GPT

    # Function to compute cosine similarity
    def cosine_similarity(self, vec1, vec2):
        vec1 = np.array(vec1)
        vec2 = np.array(vec2)
        dot_product = np.dot(vec1, vec2)
        norm_vec1 = np.linalg.norm(vec1)
        norm_vec2 = np.linalg.norm(vec2)
        return dot_product / (norm_vec1 * norm_vec2)

    def generate_embeddings(self, text, model='text-embedding-3-large'):
        if not self.client:
            raise Exception("Client not initialized. Call open_client first.")
        
        response = self.client.embeddings.create(
            model=model,  # Specify the embedding model
            input=text
        )
        embeddings = response.data[0].embedding
        return embeddings

    def search_term_in_embeddings(self, df, search_term, n=None, pprint=True):
        if not self.client:
            raise Exception("Client not initialized. Call open_client first.")

        assert 'embeddings' in df.columns, "Expecting a column named 'embeddings' in the dataframe."

        # Drop if embeddings are nan
        df = df.dropna(subset=['embeddings'])
        search_term_embedding = self.generate_embeddings(search_term, 'text-embedding-3-large')

        df['similarities'] = df.embeddings.apply(lambda x: self.cosine_similarity(x, search_term_embedding))

        res = df.sort_values('similarities', ascending=False)
        if n:
            res = res.head(n)
        return res

class ChatAgent(GPTAgent):
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
