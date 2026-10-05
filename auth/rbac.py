ROLES = {'admin': ['read','write','delete'], 'user': ['read']}
def has_permission(role, perm):
    return perm in ROLES.get(role, [])
