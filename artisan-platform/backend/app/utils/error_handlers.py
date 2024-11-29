from flask import jsonify

def handle_404_error(e):
    response = jsonify({"detail": "Resource not found"})
    response.status_code = 404
    return response

def handle_500_error(e):
    response = jsonify({"detail": "Internal server error"})
    response.status_code = 500
    return response