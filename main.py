from flask import Flask
from flask_restful import Api, Resource, reqparse, abort

# Initialise flask application Instances
app = Flask(__name__)
# Wrap Flask Application in Api
api = Api(app)
# Use reqparse to setup new data input for post method
signup = reqparse.RequestParser()
signup.add_argument("first_name", type=str, help='you need to enter your first name', required=True)
signup.add_argument("last_name", type=str, help='you need to enter your last name', required=True)
signup.add_argument("set_password", type=str, help='you need to enter your password', required=True)

# create a distionary data of exiting customer for get method
exist_customer = {
    "caleb": {"first_name": "caleb", "last_name": "eghan", "password": "123"},
    "ben": {"first_name": "ben", "last_name": "hendeerson", "password": "321"}
}
# Empty dictionary to store all data of customers who signup
client_details = {}


# If customer in get method does not exist, abort
def abort_request_if_customer_not_found(new_customer):
    if new_customer not in client_details:
        abort(404, message="This customer does not exist")


# if customer exist in post method, abort
def abort_request_if_customer_already_exist(new_customer):
    if new_customer in client_details:
        abort(409, message="customer already exist")


# Create a resource class with a post method for new customers
class service_post(Resource):

    # Set a parameter called new_customer for the post method
    def post(self, new_customer):
        # Call the reqparse instances by passing it to a new variable called post_data
        abort_request_if_customer_already_exist(new_customer)
        post_data = signup.parse_args()

        # Assign the data captured by empty dictionary and for the new customer object
        client_details[new_customer] = post_data

        # return the outcome as the return value for this method
        return client_details[new_customer]

    # Get the data the new customer entered
    def get(self, new_customer):
        abort_request_if_customer_not_found(new_customer)
        return client_details[new_customer]


# Add Service_post as an Api resource and set a url directory
api.add_resource(service_post, '/customer/<string:new_customer>')

# Create a new class as resource to hold the get method for getting an exiting customer's information
# class service_get(Resource):

# Set a parameter called existing_customer for the get method
# def get(self, existing_customer):
# Call and return the data inside the dictionary(exist_customer) for the get method parameter(existing_customer)
# return exist_customer[existing_customer]

# Add Service_get as an Api resource and a url directory
# api.add_resource(service_get, '/customer/<string:existing_customer>')

if __name__ == '__main__':
    app.debug = True
    app.run()
