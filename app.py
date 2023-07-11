import json
from flask import Flask, request, jsonify
from svo import extract_entities, find_root_de, find_root_subject, get_root, lowercase_strings, find_root_subject_de

app = Flask(__name__)



def index():
    return 'HHHHHHH'

@app.route('/')
def index():
    return 'HHHHHHH'



@app.route('/svo', methods=['GET', 'POST'])
def svo():

    if request.method == 'GET':

       
        sentences = ["In June, Diane visited her friends who live in San Francisco, California. This was Diane’s first time in the city, and she enjoyed her opportunities to walk around and explore.", 
                        "On the first day of her trip, Diane visited the Golden Gate Bridge.", 
                        "This red suspension bridge measures 1.7 miles in length."]
        
        result = lowercase_strings(sentences)

        return jsonify(result), 201

    if request.method == 'POST':
       
       
        sentences = ["In June, Diane visited her friends who live in San Francisco, California. This was Diane’s first time in the city, and she enjoyed her opportunities to walk around and explore.", 
                        "On the first day of her trip, Diane visited the Golden Gate Bridge.", 
                        "This red suspension bridge measures 1.7 miles in length."]
        
       # entences = request.json

        
        result = lowercase_strings(sentences)

        hahaha = request.json

        d = type(hahaha)

        uuu = hahaha["strings"]

        result = lowercase_strings(uuu)

        yoo = f"My age is {uuu}."
        
        return result
        return yoo
        return type(hahaha)
       
        string_without_newline = hahaha[:-2]

        return string_without_newline
    
       # parsed_json2 = json.loads(string_without_newline)

        json_string = '{"strings":["hello","byebye"]}'
        parsed_json = json.loads(json_string)
        

        string_array = parsed_json['strings']

       # return json_string
        # string_array = parsed_json['strings']


        return hahaha 

        return jsonify(result), 201

    


if __name__ == '__main__':
    app.run(debug=True)

