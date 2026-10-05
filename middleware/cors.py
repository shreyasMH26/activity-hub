ALLOWED_ORIGINS = ['https://app.example.com']
def cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response
