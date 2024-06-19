from flask import Flask, jsonify, request

app = Flask(__name__)

"""
Contact object:
{
    "id": 1,
    "name": "Cat McCattington",
    "phone": "123-456-7890",
    "email": "mccattington@catmail.com",
}
"""
contacts: list[dict] = [
    {
        "id": 1,
        "name": "Cat McCattington",
        "phone": "123-456-7890",
        "email": "mccattington@catmail.com",
    }
]


@app.route("/", methods=["GET", "POST"])
def hello_world():
    return """<h1>Hello world!</h1>"""


@app.route("/error")
def throw_error():
    raise Exception("Oh no, something broke!")


@app.route("/contacts/<int:id>", methods=["GET"])
def read_one_contact(id: int):
    contact = list(filter(
        # (contact) => id === contact.id
        lambda contact: id == contact["id"],
        contacts
    ))
    if len(contact) > 0:
        return jsonify(contact.pop())
    return jsonify(msg="Contact not found"), 404


@app.route("/contacts", methods=["GET"])
def read_all_contacts():
    return jsonify(contacts=contacts)


@app.route("/contacts", methods=["POST"])
def create_contact():
    data = request.json
    contact = {
        **data,
        "id": len(contacts) + 1
    }
    contacts.append(contact)
    return jsonify(contact)
