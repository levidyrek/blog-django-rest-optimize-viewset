from rest_framework import viewsets

from .models import BlogPost
from .serializers import BlogPostSerializer


class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

    def dispatch(self, *args, **kwargs):
        response = super().dispatch(*args, **kwargs)

        # For debugging purposes only.
        from django.db import connection
        print('# of Queries: {}'.format(len(connection.queries)))

        return response
