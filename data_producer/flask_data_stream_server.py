from flask import Flask, request
from flask_restful import Resource, Api
from db_helper import UserDatabase

app = Flask(__name__)
api = Api(app)


class UserResource(Resource):
    def get(self, **kwargs):
        user = UserDatabase().get_user(**kwargs)
        if user is not None:
            return user, 200
        return {"message": "User not found"}, 404


api.add_resource(UserResource, '/user')
api.add_resource(UserResource, '/user/<int:id>')

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
