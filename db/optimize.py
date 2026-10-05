def select_related(*fields):
    return {'select_related': fields}

def prefetch_related(*fields):
    return {'prefetch_related': fields}
