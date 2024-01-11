# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:

user1 = {
    "name" : "Annabelle",
    "valid" : True, #if valid is set to false then the output will be invalid user.
}

def authenticating(fn):

    def wrapper(*args, **kwargs):
        if args[0]["valid"]:
            return fn(*args, **kwargs)
        else:
            return print("invalid user")
    return wrapper

@authenticating
def message_friends(user):
    print("message has been sent")

message_friends(user1)