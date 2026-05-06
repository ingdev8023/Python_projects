from flask import Flask, request, redirect, jsonify,abort
from services import url_short, get_original_url, increment_clicks, get_url_stats
from db import init_db

app = Flask(__name__)
init_db()

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

    increment_clicks(short_code)
    return redirect(original_url)

@app.route("/stats/<short_code>", methods=["GET"])
def stats(short_code):
    stats_data = get_url_stats(short_code)

    if not stats_data:
        return jsonify({"error": "Short URL not found"}), 404

    return jsonify(stats_data)
