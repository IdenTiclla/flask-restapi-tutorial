from flask import Flask, request
from flask_restful import Api, Resource, abort, reqparse
from flask_sqlalchemy import SQLAlchemy
import requests

app = Flask(__name__)
api = Api(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class VideoModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    views = db.Column(db.Integer, nullable=False)
    likes = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"<Video: {self.name}>"

video_put_args = reqparse.RequestParser()

video_put_args.add_argument("name", type=str, help="name of the video", required=True)
video_put_args.add_argument("views", type=int, help="views of the video", required=True)
video_put_args.add_argument("likes", type=int, help="likes on the video", required=True)

videos = {}
def abort_if_video_id_doesnt_exist(video_id):
    if video_id not in videos:
        abort(404, message="could not find video...")
class Video(Resource):
    def get(self, video_id):
        abort_if_video_id_doesnt_exist(video_id)
        return videos[video_id]
    
    def put(self, video_id):
        video_dict = video_put_args.parse_args()
        videos[video_id] = video_dict
        return videos[video_id], 201
    
    def delete(self, video_id):
        abort_if_video_id_doesnt_exist(video_id)
        del videos[video_id]
        return '', 204
        
api.add_resource(Video, "/video/<int:video_id>")

if __name__ == "__main__":
    app.run(debug=True)
