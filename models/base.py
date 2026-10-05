class SoftDeleteMixin:
    deleted_at = None
    def delete(self):
        import datetime
        self.deleted_at = datetime.datetime.utcnow()
