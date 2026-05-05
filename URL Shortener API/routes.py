from flask import Flask, request, redirect, jsonify,abort
from services import url_short, get_original_url, return_urls_store

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "URL Shortener API is running"})
    

@app.route("/shorten", methods=["POST"])
def shorten():
    
    data = request.get_json(silent=True)

    if not data or "url" not in data:
        return jsonify({"error": "Missing 'url' field"}), 400        
    else:
        base_url = request.root_url
        original_url = data.get('url')
        if not original_url.startswith(("http://", "https://")):
            return jsonify({"error": "Invalid URL"}), 400
        else:
            response_json = jsonify(url_short(original_url, base_url))    
            return response_json, 201

@app.route("/<short_code>", methods=["GET"])
def redirect_url(short_code):
    original_url = get_original_url(short_code)
    if not original_url:
        abort(404)

    return redirect(original_url)

@app.route("/debug/urls")
def debug_urls():
    return return_urls_store()
