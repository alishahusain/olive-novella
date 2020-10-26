import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Data in the form of dictionaries
novels = [
    {'id': 0,
     'title': 'All the Light We Cannot See',
     'author': 'Anthony Doer',
     'overview': 'A blind French girl and a German boy whose paths collide in occupied France as both try to survive the devastation of World War II',
     'year_published': '2014'},
    {'id': 1,
     'title': 'The Color Purple',
     'author': 'Alice Walker',
     'overview': 'Set in the deep American South between wars, Celia, a young black girl born into poverty and segregation, leads a very hard life.',
     'published': '1973'},
    {'id': 2,
     'title': 'War and Peace',
     'author': 'Leo Tolstoy',
     'overview': 'An in-depth study of the Napoleonic wars’ effects on five Russian aristocrats and their families.',
     'published': '1867'}
]


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Discover Historical Novels</h1>
<p>A prototype API for discovering basic information about historical novels.</p>'''


@app.route('/api/novels/all', methods=['GET'])
def api_all():
    return jsonify(novels)
    
    
    
    
@app.route('/api/novels', methods=['GET'])
def api_id():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."

    results = []


    for novel in novels:
        if novels['id'] == id:
            results.append(novel)


    return jsonify(results)

app.run()