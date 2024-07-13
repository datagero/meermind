import os
import json
from chatagent import ChatAgent

def get_prompt_template():
    with open('backend/ai_tools/generate_data/prompts/json_summaries.txt', 'r') as file:
        prompt_template = file.read()
    return prompt_template

def process_file(module_name, file_name, file_ext, reprocess_failed=False):
    path_ext = f'/{module_name}/{file_name}'
    file_path = 'data/ingest'+path_ext+file_ext
    out_path = 'data/summaries'+path_ext+'.json'
    failed_out_path = 'data/failed'+path_ext+'.txt'
    process_module(module_name, file_path, out_path, failed_out_path)

def process_module(module_name, file_path, out_path, failed_out_path):

    # Create the output directory if it doesn't exist
    if not os.path.exists(os.path.dirname(out_path)):
        os.makedirs(os.path.dirname(out_path))

    assert os.path.isfile(file_path), "Expecting a transcript file for each module"
    with open(file_path, 'r', encoding='utf-8') as f:
        transcript = f.read()

    agent = ChatAgent()
    agent.open_client()

    prompt_template = get_prompt_template()
    separator = '\n\n=============\n'

    response = agent.process_chat(prompt_template+separator+transcript)
    response_content = response.content

    try:
        json_response = json.loads(response_content)
        with open(out_path, "w") as f:
            json.dump(json_response, f, indent=4)

    except Exception as e:
        print('Failed to parse response as JSON')
        raise e

if __name__ == '__main__':
    module_name = 'Meerkats'
    file_name = 'meerkat'
    file_ext = '.rtf'

    args = [module_name, file_name, file_ext]

    process_file(*args)
