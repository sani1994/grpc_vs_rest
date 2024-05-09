from flask import Flask
from flask_restful import Resource, Api

from db_helper import UserDatabase

app = Flask(__name__)
api = Api(app)


class UserResource(Resource):
    @staticmethod
    def user_serializer(user):
        return {
            "id": user.id,
            "name": user.name,
            "username": user.username,
            "email": user.email,
            "phone_number": user.phone_number,
            "created": user.created,
            "modified": user.modified
        }

    def get(self, **kwargs):
        users = UserDatabase().get_user(**kwargs)
        if not users:
            return {"message": "User not found"}, 404

        users = users if isinstance(users, list) else [users]
        return [self.user_serializer(user) for user in users], 200


api.add_resource(UserResource, '/user')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000, debug=True)
