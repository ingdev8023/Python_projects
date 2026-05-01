from flask import Flask, request, redirect, jsonify,abort
from services import url_short, get_original_url, return_urls_store

app = Flask(__name__)

@app.route("/")
def home():
    return return_urls_store()

@app.route("/shorten", methods=["POST"])
def shorten():
    main_url = request.root_url
    original_url = request.json.get('url')
    response_json = jsonify(url_short(original_url, main_url))    
    return response_json

@app.route("/<short_code>", methods=["GET"])
def redirect_url(short_code):
    original_url = get_original_url(short_code)
    if not original_url:
        abort(404)

    return redirect(original_url)
