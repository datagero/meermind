import os, json
from flask import Flask, flash, request, redirect, url_for, jsonify
from werkzeug.utils import secure_filename
from dotenv import load_dotenv
import logging 

import database.functions as db
import ai_tools.generate_data.main as ai

logging.basicConfig(
        level=logging.DEBUG, 
        # format='%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s'
        )

logger = logging.getLogger(__name__)

load_dotenv()

ALLOWED_EXTENSIONS = set(['txt', 'rsp', 'rtf'])
UPLOAD_FOLDER = os.path.abspath(os.path.join(os.path.dirname(__file__), 'Downloads'))

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 500 * 1000 * 1000  # 500 MB
app.config['CORS_HEADER'] = 'application/json'

# Debug is on
if os.environ.get("DEBUG") is not None:
    logger.debug(f' msg --> DEBUG is set {os.environ.get("DEBUG")}')
    # logger.debug(f'URI: {os.environ.get("DB_CONNECTION_CONNECTION_STRING")}')

@app.route('/', methods=['GET'])

def home():
    return 'Hello, World!'

def allowedFile(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/upload', methods=['POST', 'GET'])
def fileUpload():
    if request.method == 'POST':
        files = request.files.getlist('files')
        print(request.files, "....")
        for file in files:
            if file.filename is not None:
                print(file.filename)
                filename = secure_filename(file.filename)

                if allowedFile(filename):
                    # TODO add file to db
                    # db.save(transcript_file)

                    name, file_ext = os.path.splitext(filename)
                    module_name='meermind'
                    file_data = file.read()
                    db.insert_transcript(module_name, name, file_ext, file_data)

                    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

                    # Start to openai-api service
                    # formatted_response = ai.process_transcript(file_data.decode('utf-8'))
                    # For Testing -> To avoid using the API, we can use the following:
                    formatted_response = '{\n"title": "Fascinating Facts about Meerkats",\n"oneLineSummary": "Discussion of interesting facts about meerkats, including their unique markings, social behavior, and diet.",\n"studentSummary": [\n{\n"summaryTitle": "Interesting Facts about Meerkats",\n"summaryPoints": [\n"The dark markings under their eyes act like sunglasses, allowing them to see in harsh desert light.",\n"Meerkats stand guard to protect the group from predators like eagles and jackals.",\n"They live in social groups called mobs, ranging from five to thirty members.",\n"Meerkats are fiercely territorial and will defend their territory from threats like snakes.",\n"They use their claws to dig burrows and tunnels where they sleep.",\n"Meerkats belong to the Mongoose family and enjoy wrestling as a form of play.",\n"They have a diverse diet, including scorpions, beetles, spiders, lizards, and small rodents."\n]\n}\n],\n"relatedInformation": [],\n"benefits": [],\n"limitations": [],\n"realWorldExample": "",\n"stateOfTheArtResearch": "",\n"references": []\n}'

                    # Might need this to debug JSON formatting issues - There will be some other issues... let's try to document them.
                    try:
                        data = json.loads(formatted_response)
                    except json.JSONDecodeError as e:
                        # formatted_response_clean = formatted_response.replace('\\n', '\n').replace('\\', '')
                        print(f"JSON decoding error: {e.msg} at line {e.lineno} column {e.colno}")
                        print(f"Problematic JSON snippet: {formatted_response[e.pos - 10:e.pos + 10]}")
                        raise e

                    # TODO save the formatted reponse 
                    db.insert_transcript_summary(module_name, name, file_ext, data)

                else:
                    return jsonify({'message': 'File type not allowed'}), 400

        return jsonify({"name": filename, "status": "success"})
    else:
        return jsonify({"status": "Upload API GET Request Running"})


temp_objects = {"notes": 
                    [ {
    "title": "Fascinating Meerkat Facts",
    "oneLineSummary": "Discussion about interesting facts related to meerkats, their behavior, and diet.",
    "studentSummary": [
        {
            "summaryTitle": "Meerkat Characteristics",
            "summaryPoints": [
                "The dark markings under meerkats' eyes act like sunglasses in the harsh desert light.",
                "Meerkats are vigilant against predators like eagles and jackals, with some standing guard while others forage.",
                "They live in social groups called mobs, ranging from five to thirty members, and are fiercely territorial.",
                "Meerkats dig burrows and tunnels in their territory for shelter and rest.",
                "They are members of the Mongoose family, grow up to 12 inches, and weigh about two pounds.",
                "Meerkats exhibit playful wrestling behavior, starting from a young age."
            ]
        },
        {
            "summaryTitle": "Meerkat Diet",
            "summaryPoints": [
                "Meerkats love to eat scorpions and are immune to their venom.",
                "If scorpions are not available, they will also consume beetles, spiders, lizards, and small rodents."
            ]
        }
    ],
    "relatedInformation": [],
    "benefits": [],
    "limitations": [],
    "realWorldExample": "In 2017, a wildlife documentary crew captured footage of a meerkat mob defending their territory from a rival group intruding on their turf. The footage showcased the intense territorial behaviors and strategic defense tactics exhibited by the meerkats, providing valuable insights into their social dynamics and survival instincts.",
    "stateOfTheArtResearch": "",
    "references": []
},
{
    "title": "Another One",
    "oneLineSummary": "another one line summary",
    "studentSummary": [
        {
            "summaryTitle": "Another title",
            "summaryPoints": [
                "TESTING",
            ]
        },
        {
            "summaryTitle": "Some title",
            "summaryPoints": [
                "More information",
            ]
        }
    ],
    "relatedInformation": [],
    "benefits": [],
    "limitations": [],
    "realWorldExample": "EXAMPLES",
    "stateOfTheArtResearch": "",
    "references": []
}
        ]}

@app.route('/get-notes', methods=['GET'])
def get_transcripts():
    #TODO get objects from the mongodb 

    #TODO any processing before sending 

    #TODO send data to frontend
    return jsonify(temp_objects);

if __name__ == '__main__':
   app.run(port=5000)
