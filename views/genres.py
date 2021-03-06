from flask_restx import Resource, Namespace
import requests

from models import Genre, GenreSchema
from setup_db import db

genre_ns = Namespace('genres')


@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        rs = db.session.query(Genre).all()
        res = GenreSchema(many=True).dump(rs)
        return res, 200


    def post(self):
        req_json = request.json
        ent = Genre(**req_json)

        db.session.add(ent)
        db.session.commit()
        return "", 201, {"location": f"/genres/{ent.id}"}


@genre_ns.route('/<int:rid>')
class GenreView(Resource):
    def get(self, rid):
        r = db.session.query(Genre).get(rid)
        sm_d = GenreSchema().dump(r)
        return sm_d, 200


    def put(self, bid):
        genre = db.session.query(Genre).get(bid)
        req_json = request.json
        genre.id = req_json.get("title")
        genre.name = req_json.get("description")
        db.session.commit()
        return "", 204

    def delete(self, bid):
        genre = db.session.query(Genre).get(bid)

        db.session.delete(genre)
        db.session.commit()
        return "", 204