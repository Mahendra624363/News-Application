from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter

from django_filters.rest_framework import DjangoFilterBackend

from .models import News
from .serializers import NewsSerializer
from .permissions import IsEditorOrReadOnly
from .pagination import NewsPagination


class NewsViewSet(ModelViewSet):

    queryset = News.objects.all().order_by('-created_at')
    serializer_class = NewsSerializer
    permission_classes = [IsAuthenticated, IsEditorOrReadOnly]
    pagination_class = NewsPagination
    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter
    ]
    search_fields = ['title', 'content']
    filterset_fields = ['category', 'state']
    ordering_fields = ['created_at', 'title']
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)