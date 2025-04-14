from marshmallow import Schema, fields, post_load
from flaskApp.app.models.user import User

class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True)
    email = fields.Str(required=True)
    password = fields.Str(load_only=True, required=True)

    @post_load
    def make_user(self, data, **kwargs):
        user = User(username=data['username'], email=data['email'])
        user.password = data['password'] 
        return user
