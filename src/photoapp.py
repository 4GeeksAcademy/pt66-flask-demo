from flask import (
    Blueprint, jsonify, request
)

api = Blueprint(
    "photos",
    __name__,
    url_prefix="/photos",
)

users: dict = []
photos: dict = []
favorites: dict = []


@api.route("/users/<string:username>", methods=["POST"])
def create_user(username):
    if username in [u["username"] for u in users]:
        return jsonify(msg="User already exists"), 400
    user = {
        "id": len(users) + 1,
        "username": username,
        "favorites": []
    }
    users.append(user)
    return jsonify(user)


@api.route("/users", methods=["GET"])
def read_users():
    photo_users = []
    for user in users:
        photo_users.append({
            **user,
            "photos": list(filter(
                lambda photo: photo["user_id"] == user["id"],
                photos
            ))
        })
    return jsonify(users=photo_users)


@api.route("/photos", methods=["POST"])
def create_photo():
    """
    Body:
    {
        "url": "https://wob.site/photo.jpg",
        "user_id": 1
    }
    """
    data = request.json
    if data["user_id"] not in [u["id"] for u in users]:
        return jsonify(msg="User does not exist."), 404
    photo = {
        **data,
        "id": len(photos) + 1
    }
    photos.append(photo)
    return jsonify(photo)
