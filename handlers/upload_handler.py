import glob

def upload(request):
    #Check if the params is declared
    if any(x not in request.args for x in ["user", "password"]):
        return "Missing params"

    u = request.args["user"]
    p = request.args["password"]

    #Check if valid login
    if u not in glob.users or glob.users[u] != p:
        return "Invalid login"

    return "Upload file ;)"