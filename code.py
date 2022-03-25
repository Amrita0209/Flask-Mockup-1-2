import csv
from flask import Flask, jsonify, request

with open('users_interactions.csv', newline="") as f:
  reader = csv.reader(f)
  data = list(reader)

app = Flask(__name__)

@app.route("/view")
def get_views():
    view = []
    for i in data:
        if i[1] == 'VIEW':
            view.append(i)
    return jsonify({
        "data": view,
        "message": "success"
        }), 200


@app.route("/bookmark")
def get_bookmarks():
    bookmark = []
    for i in data:
        if i[1] == 'BOOKMARK':
            bookmark.append(i)
    return jsonify({
        "data": bookmark,
        "message": "success"
        }), 200


@app.route("/follow")
def get_follows():
    follow = []
    for i in data:
        if i[1] == 'FOLLOW':
            follow.append(i)
    return jsonify({
        "data": follow,
        "message": "success"
        }), 200


@app.route("/like")
def get_likes():
    like = []
    for i in data:
        if i[1] == 'LIKE':
            like.append(i)
    return jsonify({
        "data": like,
        "message": "success"
        }), 200


@app.route("/comment")
def get_comments():
    comment = []
    for i in data:
        if i[1] == 'COMMENT CREATED':
            comment.append(i)
    return jsonify({
        "data": comment,
        "message": "success"
        }), 200



if __name__ == "__main__":
    app.run()

