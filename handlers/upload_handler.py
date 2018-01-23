import glob
from werkzeug import secure_filename

def upload(request):
    #Check if the params is declared
    if not valid_params(request.args) or "file" not in request.files:
        return "Missing params"

    f = request.files['file']

    if not valid_login(request.args):
        return "Invalid login"

    #TODO: generate random name and into the right folder
    f.save(secure_filename(f.filename))

    return "Upload file ;)"

def valid_login(args):
    u = args["user"]
    p = args["password"]
    return u in glob.users and glob.users[u] == p

    
def valid_params(args):
    if not glob.config["settings"]["require_login"]:
        return True
    return any(x not in args for x in ["user", "password"])
