def get_user_id(request):
    user = getattr(request, 'user', None)
    return user.id if user else None
