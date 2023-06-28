from rest_framework.viewsets import ModelViewSet
from .models import InternProfile
from .serializers import AddInternProfileSerializer,ViewInternProfileSerializer

class InternProfileViewset(ModelViewSet):
    http_method_names=['get','post','patch','delete']
    queryset=InternProfile.objects.all()

    def get_serializer_class(self):
        if self.request.method in ['GET','DELETE']:
            return ViewInternProfileSerializer
        return AddInternProfileSerializer