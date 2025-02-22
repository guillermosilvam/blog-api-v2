from rest_framework import generics
from .models import post
from .serializers import postSerializer

# Create your views here.
class postList(generics.ListCreateAPIView):
    queryset = post.objects.all()
    serializer_class = postSerializer

class postDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = post.objects.all()
    serializer_class = postSerializer