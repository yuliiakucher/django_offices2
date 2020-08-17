from rest_framework import generics
from rest_framework.mixins import ListModelMixin
from .serializers import OfficeSerializer
from .models import OfficeModel


class OfficeView(ListModelMixin, generics.CreateAPIView):
    serializer_class = OfficeSerializer
    queryset = OfficeModel.objects.all()

    def get(self, request, *args, **kwargs):
        # if request.method == 'GET':
        #     self.serializer_class =
        return self.list(request, *args, **kwargs)


