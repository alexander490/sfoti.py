from django.db.models import QuerySet


class TrackQueryset(QuerySet):

    def top(self):
        return self.order_by('-listen')
