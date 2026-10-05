CACHE_TTL = 300  # 5 minutes
def cache_key(*args):
    return ':'.join(str(a) for a in args)
