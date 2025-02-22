from rest_framework import generics, permissions
from .models import post
from .serializers import postSerializer
from .permissions import IsAuthorOrReadOnly

# Create your views here.
class postList(generics.ListCreateAPIView):
    queryset = post.objects.all()
    serializer_class = postSerializer
    permission_classes = (IsAuthorOrReadOnly,)

class postDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = post.objects.all()
    serializer_class = postSerializer
    permission_classes = (IsAuthorOrReadOnly,)

