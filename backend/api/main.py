import os, json
from flask import Flask, flash, request, redirect, url_for, jsonify
from werkzeug.utils import secure_filename
from dotenv import load_dotenv
from flask_cors import CORS
import logging 

import db

logging.basicConfig(
        level=logging.DEBUG, 
        # format='%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s'
        )

logger = logging.getLogger(__name__);

load_dotenv()

ALLOWED_EXTENSIONS = set(['txt', 'rsp', 'rtf'])
UPLOAD_FOLDER = os.path.abspath(os.path.join(os.path.dirname(__file__), 'Downloads'))

app = Flask(__name__)
CORS(app)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 500 * 1000 * 1000  # 500 MB
app.config['CORS_HEADERS'] = 'application/json'
app.config['CORS_SUPPORTS_CREDENTIALS'] = True
app.config['CORS_ALLOW_HEADERS'] = 'Content-Type'
app.config['CORS_RESOURCES'] = {r"/api/*": {"origins": "http://localhost:3000/"}}

db.connect()


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
        file = request.files.getlist('files')
        filename = ""

        print(request.files, "....")
        for f in file:
            if f.filename is not None:
                print(f.filename)
                filename = secure_filename(f.filename)

                if allowedFile(filename):
                    # TODO add file to db
                    # db.save(transcript_file)

                    f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

                    # TODO start to openai-api service
                    # formatted_response = summary(f)

                    # TODO save the formatted reponse 
                    # db.save(formatted_response);

                else:
                    return jsonify({'message': 'File type not allowed'}), 400

        return jsonify({"name": filename, "status": "success"})
    else:
        return jsonify({"status": "Upload API GET Request Running"})


temp_objects = {"notes": 
[
    {
        "title": "Amazing Dolphin Facts",
        "oneLineSummary": "Discussion about interesting facts related to dolphins, their behavior, and habitat.",
        "studentSummary": [
            {
                "summaryTitle": "Dolphin Characteristics",
                "summaryPoints": [
                    "Dolphins are highly intelligent marine mammals known for their playful behavior and social bonds.",
                    "They communicate using a variety of clicks, whistles, and body language.",
                    "Dolphins are streamlined and fast swimmers, capable of reaching speeds of up to 25 miles per hour.",
                    "They have excellent eyesight both in and out of the water."
                ]
            },
            {
                "summaryTitle": "Dolphin Diet",
                "summaryPoints": [
                    "Dolphins are carnivores, primarily feeding on fish, squid, and crustaceans.",
                    "Some species of dolphins, like the killer whale (orca), also hunt marine mammals such as seals."
                ]
            }
        ],
        "relatedInformation": [],
        "benefits": [],
        "limitations": [],
        "realWorldExample": "In a study conducted in 2019, researchers observed a pod of dolphins working together to create a mud ring to catch fish, demonstrating their cooperative hunting strategies.",
        "stateOfTheArtResearch": "",
        "references": []
    },
    {
        "title": "Majestic Tiger Behavior",
        "oneLineSummary": "Exploring the behavior, hunting techniques, and social structure of tigers in the wild.",
        "studentSummary": [
            {
                "summaryTitle": "Tiger Characteristics",
                "summaryPoints": [
                    "Tigers are the largest cats in the world, known for their distinctive orange coat with black stripes.",
                    "They are solitary hunters and are capable of taking down prey much larger than themselves.",
                    "Tigers are excellent swimmers and often cool off in water bodies during hot weather."
                ]
            },
            {
                "summaryTitle": "Tiger Hunting",
                "summaryPoints": [
                    "Tigers use ambush tactics to surprise their prey, relying on their powerful jaws and sharp claws to secure a kill.",
                    "They are known to hunt a variety of animals, including deer, wild boar, and even young elephants."
                ]
            }
        ],
        "relatedInformation": [],
        "benefits": [],
        "limitations": [],
        "realWorldExample": "Researchers studying tigers in India documented a female tiger successfully raising and teaching her cubs hunting skills, highlighting maternal care and learning behaviors in wild tigers.",
        "stateOfTheArtResearch": "",
        "references": []
    },
    {
        "title": "Fascinating Penguin Life",
        "oneLineSummary": "Insights into the life cycle, adaptations, and behavior of penguins in their Antarctic habitats.",
        "studentSummary": [
            {
                "summaryTitle": "Penguin Characteristics",
                "summaryPoints": [
                    "Penguins are flightless birds adapted for life in the water, with dense feathers for insulation.",
                    "They are excellent swimmers and can dive deep to catch fish and krill.",
                    "Penguins form large colonies for breeding and social interactions, often nesting in rocky or icy habitats."
                ]
            },
            {
                "summaryTitle": "Penguin Adaptations",
                "summaryPoints": [
                    "Their black and white coloration serves as camouflage, helping them evade predators in the water.",
                    "Penguins have specialized salt glands that allow them to excrete excess salt from their bodies, essential for survival in marine environments."
                ]
            }
        ],
        "relatedInformation": [],
        "benefits": [],
        "limitations": [],
        "realWorldExample": "Studies on emperor penguins have shown how they huddle together in extreme cold to conserve heat, showcasing their adaptive behaviors to survive harsh Antarctic winters.",
        "stateOfTheArtResearch": "",
        "references": []
    },
    {
        "title": "Intriguing Elephant Social Structure",
        "oneLineSummary": "Exploring the social behavior, communication, and family dynamics of elephants in the wild.",
        "studentSummary": [
            {
                "summaryTitle": "Elephant Characteristics",
                "summaryPoints": [
                    "Elephants are the largest land mammals, characterized by their long trunks and tusks (in some species).",
                    "They have a complex social structure centered around matriarchs, older females who lead family groups.",
                    "Elephants exhibit a high degree of intelligence and are capable of problem-solving and learning."
                ]
            },
            {
                "summaryTitle": "Elephant Communication",
                "summaryPoints": [
                    "Elephants communicate using a variety of vocalizations, infrasound, and body language.",
                    "They use their trunks for smelling, breathing, drinking, and picking up objects."
                ]
            }
        ],
        "relatedInformation": [],
        "benefits": [],
        "limitations": [],
        "realWorldExample": "Observations of African elephants in Kenya revealed how matriarchs lead their herds to seasonal water sources, demonstrating leadership and knowledge of the environment.",
        "stateOfTheArtResearch": "",
        "references": []
    },
    {
        "title": "Enigmatic Owl Adaptations",
        "oneLineSummary": "Investigating the unique adaptations, hunting techniques, and nocturnal behavior of owls.",
        "studentSummary": [
            {
                "summaryTitle": "Owl Characteristics",
                "summaryPoints": [
                    "Owls are nocturnal birds of prey known for their silent flight and excellent hearing.",
                    "They have specialized feathers for silent flight and large eyes adapted for low-light conditions.",
                    "Owls have a sharp beak and talons for capturing and killing prey efficiently."
                ]
            },
            {
                "summaryTitle": "Owl Hunting Strategies",
                "summaryPoints": [
                    "Owls hunt small mammals, birds, and insects using their sharp vision and precise hearing.",
                    "They swallow their prey whole and later regurgitate indigestible parts such as bones and fur in pellets."
                ]
            }
        ],
        "relatedInformation": [],
        "benefits": [],
        "limitations": [],
        "realWorldExample": "Researchers studying barn owls in North America documented their ability to hunt with pinpoint accuracy using both sight and sound cues, showcasing their adaptive hunting strategies.",
        "stateOfTheArtResearch": "",
        "references": []
    },
    {
        "title": "Spectacular Lion Behavior",
        "oneLineSummary": "Exploring the hunting techniques, social structure, and conservation challenges faced by lions in the wild.",
        "studentSummary": [
            {
                "summaryTitle": "Lion Characteristics",
                "summaryPoints": [
                    "Lions are large carnivorous cats known for their muscular build and golden fur.",
                    "They live in prides consisting of related females, their offspring, and a coalition of males.",
                    "Male lions defend the pride's territory, while females collaborate in hunting and raising young."
                ]
            },
            {
                "summaryTitle": "Lion Hunting",
                "summaryPoints": [
                    "Lions use coordinated tactics to stalk and ambush prey, often relying on stealth and teamwork to bring down large herbivores.",
                    "They are opportunistic feeders and scavenge on kills made by other predators such as hyenas."
                ]
            }
        ],
        "relatedInformation": [],
        "benefits": [],
        "limitations": [],
        "realWorldExample": "Conservation efforts in Africa have focused on protecting lion populations and their habitats, highlighting the importance of maintaining balanced ecosystems.",
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
