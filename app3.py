from flask import Flask, request, json, Response
from flask_restful import Resource, Api, reqparse
from pymongo import MongoClient

#initialized the flask app
app = Flask(__name__)
api = Api(app)

class GUID(Resource):
   def post(self):
    client = MongoClient('localhost', 27017)
    db = client["training-delta"]
    guid = db['guid']
    response_json = {
            "guid": "9094E4C980C74043A4B586B420E69DDF",
            "expire": "1427736345",
            "user": "Sindhu"
       }
    return response_json

    def get(self):
     client = MongoClient('localhost', 27017)
     db = client["training-delta"]
     guid = db['guid']
     response_json = {
            "guid": "9094E4C980C74043A4B586B420E69DDF",
            "expire": "1427736345",
            "user": "Sindhu"
        }
     return response_json
    
    
    def patch(self):
     client = MongoClient('localhost', 27017)
     db = client["training-delta"]
     guid = db['guid']
     response_json = {
            "expire": "1427736345"
        }
     return response_json
    
    def delete(self):
     client = MongoClient('localhost', 27017)
     db = client["training-delta"]
     guid = db['guid']
     response_json = {}  
     return response_json
    
@app.route('/GUID', methods=['POST'])
def post():
    data = request.json
    post_obj = GUID(data)
    response = post_obj.insert_data({"expire": "1427736345", "user": "Sindhu"})
    print(response.inserted_id)    
    return Response(response=json.dumps(response))

@app.route('/GUID', methods=['GET'])
def get():
    data = request.json
    get_obj = GUID(data)
    response = get_obj.find_data({ "guid": "9094E4C980C74043A4B586B420E69DDF","expire": "1427736345","user": "Sindhu"})
    print(response.find_id)    
    return Response(response=json.dumps(response))

@app.route('/GUID', methods=['PATCH'])
def patch():
    data = request.json
    patch_obj = GUID(data)
    response = patch_obj.update_data({"expire:","1427736345"})
    print(response.update_id)    
    return Response(response=json.dumps(response))

@app.route('/GUID', methods=['DELETE'])
def delete():
    data = request.json
    delete_obj = GUID(data)
    response = patch_obj.delete_data({})
    print(response.update_id)    
    return Response(response=json.dumps(response))


api.add_resource(GUID, '/api/guid')

if __name__ == '__main__':
    app.run()
