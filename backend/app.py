from typing import Tuple

from flask import Flask, jsonify, request, Response
import mockdb.mockdb_interface as db

app = Flask(__name__)

CODE_UNPROCESSABLE = 422
CODE_CREATED = 201
CODE_NOT_FOUND = 404
CODE_BAD_REQUEST = 400

CONTACT_PROPS = {"REQUIRED": ["hobby", "name", "nickname"],
                 "OPTIONAL": ["id"]}

def create_response(
    data: dict = None, status: int = 200, message: str = ""
) -> Tuple[Response, int]:
    """Wraps response in a consistent format throughout the API.
    
    Format inspired by https://medium.com/@shazow/how-i-design-json-api-responses-71900f00f2db
    Modifications included:
    - make success a boolean since there's only 2 values
    - make message a single string since we will only use one message per response
    IMPORTANT: data must be a dictionary where:
    - the key is the name of the type of data
    - the value is the data itself

    :param data <str> optional data
    :param status <int> optional status code, defaults to 200
    :param message <str> optional message
    :returns tuple of Flask Response and int, which is what flask expects for a response
    """
    if type(data) is not dict and data is not None:
        raise TypeError("Data should be a dictionary 😞")

    response = {
        "code": status,
        "success": 200 <= status < 300,
        "message": message,
        "result": data,
    }
    return jsonify(response), status


"""
~~~~~~~~~~~~ API ~~~~~~~~~~~~
"""
@app.route("/")
def hello_world():
    return create_response({"content": "hello world!"})

@app.route("/mirror/<name>")
def mirror(name):
    data = {"name": name}
    return create_response(data)

@app.route("/contacts", methods=['GET'])
def get_all_contacts():
    if len(request.args) == 0:
        return create_response({"contacts": db.get('contacts')})
    
    return get_contacts_by_hobby(request.args.get("hobby"))

def get_contacts_by_hobby(hobby):
    if not isValid(hobby):
        return create_response(status=CODE_BAD_REQUEST, message="Hobby not specified in params")

    contacts = db.getByPropValue("contacts", "hobby", hobby)
    return create_response({"contacts": contacts})

@app.route("/contacts/<id>", methods=['GET'])
def get_contact_by_id(id):
    if not id.isdigit():
        return create_response(status=CODE_BAD_REQUEST, message="Invalid id, " + id)

    contact = db.getById('contacts', int(id))
    
    if contact is None:
        return create_response(status=CODE_NOT_FOUND, message="No contact with id " + id +  " exists")
    
    return create_response({"contact": contact})

@app.route("/contacts", methods=['POST'])
def create_contact():
    data = request.form
    value = None
    userToAdd = {}

    for prop in CONTACT_PROPS["REQUIRED"]:
        try:
            value = data[prop]
        except:
            return create_response(status=CODE_UNPROCESSABLE, 
            message="Field '" + prop +  "' must be in request body.")

        if not(isValid(value)):
            return create_response(status=CODE_UNPROCESSABLE, 
            message= prop + " must be non-null and not empty") 

        userToAdd[prop] = value   

    db.create("contacts", userToAdd) 
    return create_response(status=CODE_CREATED, message="User created")

@app.route("/contacts/<id>", methods=['PUT'])
def modify_contact(id):
    if db.getById('contacts', int(id)) is None:
        return create_response(status=CODE_NOT_FOUND, message="No contact with id " + id + " exists")
    
    values = request.form
    updateValues = {}
    for key, value in values.items():
        if(key in CONTACT_PROPS["REQUIRED"]):
            updateValues[key] = value
    
    c = db.updateById('contacts', int(id), updateValues)

    return create_response(status=CODE_CREATED, message="Contact updated")

@app.route("/shows/<id>", methods=['DELETE'])
def delete_show(id):
    if db.getById('contacts', int(id)) is None:
        return create_response(status=CODE_NOT_FOUND, message="No contact with this id exists")
    db.deleteById('contacts', int(id))
    return create_response(message="Contact deleted")


def isValid(input):
    return input is not None and input.replace(" ", "") != ""

# TODO: Implement the rest of the API here!
"""
~~~~~~~~~~~~ END API ~~~~~~~~~~~~
"""
# NOTE: Changed port to 8081 due to interference on 8080
if __name__ == "__main__":
    app.run(port=8081, debug=True)
