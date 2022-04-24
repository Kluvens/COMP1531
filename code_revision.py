# python strings are immutable
# lists are for mutable ordered structures of the same type
# tuples are fore immutable ordered structures of any mix of types
# An exception is an action that disrupts the normal flow of a program. This action is often representative of an error being thrown. Exceptions are ways that we can elegantly recover from errors

# In python, basically every data type acts like an "object"
try:
  print(x)
except:
  # if try block cannot run, run except block
  print("An exception occurred")

try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")

try:
  print(x)
except:
  print("Something went wrong")
finally:
  # no matter which block is run before, we run finally block in the end
  print("The 'try except' is finished")

# pytest for checking exception
def test_zero_division():
  with pytest.raises(ZeroDivisionError):
      1 / 0

Flask example:
from json import dumps
from flask import Flask, request
APP = Flask(__name__)
@APP.route("/search/v1", methods=['GET'])
def search_request():
    token = request.args.get('token')
    query_str = request.args.get('query_str')
    return dumps(search_v1(token, query_str))
@APP.route("/message/pin/v1", methods=['POST'])
def message_pin_http():
    data = request.get_json()
    token = data['token']
    message_id = data['message_id']
    return dumps(message_pin_v1(token, message_id))

API testing:
# setup is a fixture and fixture is a decorator
def test_channel_create_token_error(setup):
    response = requests.post(
        f"{url}/channels/create/v2",
        json={
            "token": "Invalid token",
            "name": "this_channel",
            "is_public": True}
        )

    assert response.status_code == AccessError.code
def test_channel_details_working_single_member(setup):
    user_dict = setup[0]
    channel_dict = setup[2]

    token = user_dict['token']
    channel_id = channel_dict['channel_id']


    response = requests.get(
        f'{url}/channel/details/v2',
        params={'token': token,
        'channel_id': int(channel_id)})

    assert response.status_code == OKAY
    first_channel_details = response.json()

    assert first_channel_details['name'] == "this_channel"

map, reduce and filter are functions that help as accomplish basic iterative tasks without the overhead of a loop setup
Map: creates a new list with the results of calling a provided function on every element in the given list
Reduce: executes a reducer function (that you provide) on each member of the array resulting in a single output value
Filter: creates a new array with all elements that pass the test implemented by the provided function

Decorators allow us to add functionality to a function without altering the function itself, by "decorating" (wrapping) around it.
Arguments in python can either be keyword arguments (named) or non-keyword arguments. Non-keyword arguments cannot appear after keyword arguments in the argument list
*args: non-keyword arguments as a list and *kwargs: keyword arguments as a dictionary
