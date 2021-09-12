from flask_restful import Resource


class IndexView(Resource):

    def get(self):
        """
        This is what shows up when you successfully launch the API
        """
        return dict(status="success", message="Welcome to the API")
