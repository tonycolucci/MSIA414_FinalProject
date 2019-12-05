#!/usr/bin/python

from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
import pickle
import numpy as np
import spacy

app = Flask(__name__)
api = Api(app)


ner_path = 'models/baseline'
nlp = spacy.load(ner_path)


# argument parsing
parser = reqparse.RequestParser()
parser.add_argument('query')


class ReturnEntities(Resource):
    def get(self):
        # use parser and find the user's query
        args = parser.parse_args()
        user_query = args['query']


        doc = nlp(user_query)

        output = {}
        for ent in doc.ents:
            output[ent.text] = ent.label_
            
        

        # create JSON object
        # output = {'entities': entity, 'text': text}
        
        return output


# Setup the Api resource routing here
# Route the URL to the resource
api.add_resource(ReturnEntities, '/')


if __name__ == '__main__':
    app.run(debug=True)