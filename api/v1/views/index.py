""" Index Route """
from api.v1.views import app_views
from flask import jsonify

@app_views.route("/status", strict_slashes=False)
def return_json():
    """ return Json """
    return jsonify({"status": "OK"})
