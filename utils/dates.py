from datetime import timezone
def utcnow():
    import datetime
    return datetime.datetime.now(timezone.utc)
