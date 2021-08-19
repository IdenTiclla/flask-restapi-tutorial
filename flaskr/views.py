from flask import views
from flask_restful import Resource, abort, reqparse, fields, marshal_with
from flaskr.models import VideoModel
from flaskr import api, db
video_put_args = reqparse.RequestParser()

video_put_args.add_argument("name", type=str, help="name of the video", required=True)
video_put_args.add_argument("views", type=int, help="views of the video", required=True)
video_put_args.add_argument("likes", type=int, help="likes on the video", required=True)

video_update_args = reqparse.RequestParser()
video_update_args.add_argument("name", type=str, help="name of the video", required=True)
video_update_args.add_argument("views", type=int, help="views of the video", required=True)
video_update_args.add_argument("likes", type=int, help="likes on the video", required=True)
resource_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'views': fields.Integer,
    'likes': fields.Integer
}

class Video(Resource):
    @marshal_with(resource_fields)
    def get(self, video_id):
        result = VideoModel.query.filter_by(id=video_id).first()
        return result
        
    @marshal_with(resource_fields)
    def post(self, video_id):
        args = video_put_args.parse_args()
        result = VideoModel.query.filter_by(id=video_id).first()
        if result:
            abort(409, message="video id taken...")
        video = VideoModel(id=video_id, name=args['name'], views=args['views'], likes=args['likes'])
        db.session.add(video)
        db.session.commit()
        return video, 201

    @marshal_with(resource_fields)
    def patch(self, video_id):
        args = video_put_args.parse_args()
        result = VideoModel.query.filter_by(id=video_id).first()
        if not result:
            abort(404, message="Video doesn't exists, cannot update")
        if args["name"]:
            result.name = args["name"]
        if args["views"]:
            result.views = args["views"]
        if args["likes"]:
            result.likes = args["likes"]
        
        db.session.commit()
        return result
    def delete(self, video_id):
        
        return '', 204
        
api.add_resource(Video, "/video/<int:video_id>")