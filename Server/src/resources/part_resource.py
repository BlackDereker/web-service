from flask_restful import Resource
from flask_restful.reqparse import RequestParser

from models.part_repository import PartRepository
from models.part import Part

class PartResource(Resource):
    def get(self):
        
        parser = RequestParser()

        parser.add_argument("part_id", type=int)

        args = parser.parse_args()

        if args["part_id"] is None:
            parts = PartRepository.list_parts()
            return {
                "parts": parts
            }, 200
        else:
            part = PartRepository.get_part(args["part_id"])
            if not part:
                return {
                    "message": "Part not found!"
                }, 404
            return part.to_dict(), 200

    def post(self):
        parser = RequestParser()

        parser.add_argument("part", type=dict, required=True)

        args = parser.parse_args()

        Part.from_dict(args["part"])

        return {
            "message": "Parts created successfully"
        }, 201

