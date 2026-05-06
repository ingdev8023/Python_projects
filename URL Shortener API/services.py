import string
import secrets
from db import get_connection

def generate_short_code(length=6):
    characters = string.ascii_letters + string.digits
    return "".join(secrets.choice(characters) for _ in range(length))

def short_code_exists(short_code):
    with get_connection() as connection:
        row = connection.execute(
            "SELECT 1 FROM urls WHERE short_code = ?",
            (short_code,)
        ).fetchone()

    return row is not None

def create_unique_short_code():
    while True:
        short_code = generate_short_code()

        if not short_code_exists(short_code):
            return short_code

def url_short(original_url, server_url):

    short_code = create_unique_short_code()
    short_url = server_url + short_code
    

    with get_connection() as connection:
        connection.execute(
            """
            INSERT INTO urls (short_code, original_url, short_url)
            VALUES (?, ?, ?)
            """,
            (short_code, original_url, short_url)
        )

    return {
        "original_url": original_url,
        "short_url": short_url,
        "short_code": short_code
    }


def get_original_url(short_code):
    with get_connection() as connection:
        row = connection.execute(
            "SELECT original_url FROM urls WHERE short_code = ?",
            (short_code,)
        ).fetchone()

    if not row:
        return None

    return row["original_url"]

def increment_clicks(short_code):
    with get_connection() as connection:
        connection.execute(
            "UPDATE urls SET clicks = clicks + 1 WHERE short_code = ?",
            (short_code,)
        )


def get_url_stats(short_code):
    with get_connection() as connection:
        row = connection.execute(
            """
            SELECT short_code, original_url, short_url, clicks, created_at
            FROM urls
            WHERE short_code = ?
            """,
            (short_code,)
        ).fetchone()

    if not row:
        return None

    return dict(row)

    
        
       







