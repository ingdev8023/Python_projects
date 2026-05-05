from flask import Flask, request, redirect, jsonify,abort
from services import url_short, get_original_url, return_urls_store

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "URL Shortener API is running"})
    

@app.route("/shorten", methods=["POST"])
def shorten():
    
    if request.is_json:
        main_url = request.root_url
        original_url = request.json.get('url')
        response_json = jsonify(url_short(original_url, main_url))    
        return response_json
    else:
        return jsonify({"error": "Request must be JSON"}), 415

@app.route("/<short_code>", methods=["GET"])
def redirect_url(short_code):
    original_url = get_original_url(short_code)
    if not original_url:
        abort(404)

    return redirect(original_url)

@app.route("/debug/urls")
def debug_urls():
    return return_urls_store()
