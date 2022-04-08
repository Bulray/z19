from flask_restx import Resource, Namespace

from models import Director, DirectorSchema
from setup_db import db

director_ns = Namespace('directors')


@director_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        rs = db.session.query(Director).all()
        res = DirectorSchema(many=True).dump(rs)
        return res, 200

    def post(self):
        req_json = request.json
        ent = Director(**req_json)

        db.session.add(ent)
        db.session.commit()
        return "", 201, {"location": f"/directors/{ent.id}"}


@director_ns.route('/<int:rid>')
class DirectorView(Resource):
    def get(self, rid):
        r = db.session.query(Director).get(rid)
        sm_d = DirectorSchema().dump(r)
        return sm_d, 200


    def put(self, bid):
        director = db.session.query(Director).get(bid)
        req_json = request.json
        director.id = req_json.get("title")
        director.name = req_json.get("description")
        db.session.commit()
        return "", 204

    def delete(self, bid):
        director = db.session.query(Director).get(bid)

        db.session.delete(director)
        db.session.commit()
        return "", 204
