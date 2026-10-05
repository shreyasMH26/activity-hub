ALLOWED_REDIRECT_URIS = ['https://app.example.com/callback']
def validate_redirect(uri):
    return uri in ALLOWED_REDIRECT_URIS
