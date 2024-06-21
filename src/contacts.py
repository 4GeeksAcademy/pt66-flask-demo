from flask import (
    Blueprint, jsonify, request
)

api = Blueprint(
    "contacts",
    __name__,
    url_prefix="/contacts",
)

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


@api.route("/<int:id>", methods=["GET"])
def read_one_contact(id: int):
    contact = list(filter(
        # (contact) => id === contact.id
        lambda contact: id == contact["id"],
        contacts
    ))
    if len(contact) > 0:
        return jsonify(contact.pop())
    return jsonify(msg="Contact not found"), 404


@api.route("", methods=["GET"])
def read_all_contacts():
    return jsonify(contacts=contacts)


@api.route("", methods=["POST"])
def create_contact():
    data = request.json
    contact = {
        **data,
        "id": len(contacts) + 1
    }
    contacts.append(contact)
    return jsonify(contact)
