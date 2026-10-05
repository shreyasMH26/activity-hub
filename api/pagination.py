def paginate(queryset, page=1, size=20):
    offset = (page - 1) * size
    return queryset[offset:offset+size]
