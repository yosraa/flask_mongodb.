from flask import jsonify,  request, make_response
from flask_restful import Api, Resource
from ..model.user import  User, UserSchema, db
users_schema = UserSchema(many=True)
user_schema = UserSchema()
class UserResource(Resource):


    def get(self):


        users = User.get_all()
        user = users_schema.dump(users).data
        return {'status': 'success', 'data': user}, 200


    def post(self):


            json_data = request.get_json(force=True)
            if not json_data:
                return {'message': 'No input data provided'}, 400
            # Validate and deserialize input
            data, errors = user_schema.load(json_data)
            if errors:
                return errors, 422

            user = User(
                first_name=json_data['first_name']
            )
            User.save(user)
            result = user_schema.dump(user).data

            responseObject = {"status": 'success', 'message': 'Successfully registered.', 'data': result}
            return responseObject


    def put(self):

        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = users_schema.load(json_data)
        if errors:
            return errors, 422
        user = User.find_by_id(data['id'])
        if not user:
            return {'message': 'User does not exist'}, 400
        user.username = data['username']
        User.check_query()

        result = users_schema.dump(user).data

        return {"status": 'success', 'data': result}, 204


    def delete(self):

        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = users_schema.load(json_data)
        if errors:
            return errors, 422

        user = User.query.filter_by(id=data['id']).delete()
        db.session.commit()

        result = user_schema.dump(user).data

        return {"status": 'success', 'data': result}, 204
