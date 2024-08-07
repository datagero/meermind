"""
Here we define the main functions that will be used to process the transcript data.
These will be called by the app as an entry point to the AI tools.
"""

import os
from api.ai_tools.gptagent import ChatAgent, EmbeddingAgent

def search_term_in_transcript(df_embeddings, search_term):
    agent = EmbeddingAgent()
    agent.open_client()
    df_similarity = agent.search_term_in_embeddings(df_embeddings, search_term)
    return df_similarity

def get_prompt_template():
    with open('ai_tools/prompts/json_summaries.txt', 'r') as file:
        prompt_template = file.read()
    return prompt_template

def process_transcript(transcript):

    agent = ChatAgent()
    agent.open_client()

    prompt_template = get_prompt_template()
    separator = '\n\n=============\n'

    response = agent.process_chat(prompt_template+separator+transcript)
    response_content = response.content

    return response_content

def process_transcript_path(module_name, file_name, file_ext, reprocess_failed=False):
    path_ext = f'/{module_name}/{file_name}'
    file_path = 'data/ingest'+path_ext+file_ext
    out_path = 'data/summaries'+path_ext+'.json'
    failed_out_path = 'data/failed'+path_ext+'.txt'

    assert os.path.isfile(file_path), "Expecting a transcript file for each module"
    with open(file_path, 'r', encoding='utf-8') as f:
        transcript = f.read()

    process_transcript(transcript)

if __name__ == '__main__':
    module_name = 'Meerkats'
    file_name = 'meerkat'
    file_ext = '.rtf'

    args = [module_name, file_name, file_ext]

    process_transcript_path(*args)
