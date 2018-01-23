import glob
from werkzeug import secure_filename

def upload(request):
    #Check if the params is declared
    if any(x not in request.args for x in ["user", "password"]) or "file" not in request.files:
        return "Missing params"

    u = request.args["user"]
    p = request.args["password"]
    f = request.files['file']

    #Check if valid login
    if u not in glob.users or glob.users[u] != p:
        return "Invalid login"

    #TODO: generate random name and into the right folder
    f.save(secure_filename(f.filename))

    return "Upload file ;)"