import requests

response = requests.post(
    "http://127.0.0.1:5000/shorten",
    json={"url": "https://example.com"}
)
print(response.status_code, response.json())

response = requests.post(
    "http://127.0.0.1:5000/shorten",
    json={"url": "https://example2.com"}
)
print(response.status_code, response.json())

response = requests.post(
    "http://127.0.0.1:5000/shorten",
    json={"url": "https://example3.com"}
)
print(response.status_code, response.json())

response = requests.post(
    "http://127.0.0.1:5000/shorten",
    json={"url": "https://example4.com"}
)
print(response.status_code, response.json())

response = requests.post(
    "http://127.0.0.1:5000/shorten",
    json={"url": "https://example5.com"}
)
print(response.status_code, response.json())

response = requests.post(
    "http://127.0.0.1:5000/shorten",
    json={"url": "https://example6/sadwqeqw/131sdas/123dsa.com"}
)
print(response.status_code, response.json())

response = requests.post(
    "http://127.0.0.1:5000/shorten",
    json={"url": "https://example/13123qwweqwesdas/12312eqwe/adasdsd.com"}
)
print(response.status_code, response.json())

response = requests.post(
    "http://127.0.0.1:5000/shorten",
    json={"url": "https://example/13123qwweqwesdas/12312eqwe/adasdsd.com"}
)
print(response.status_code, response.json())

response = requests.post(
    "http://127.0.0.1:5000/shorten",
    json={"url": "assasdasdas"}
)
print(response.status_code, response.json())