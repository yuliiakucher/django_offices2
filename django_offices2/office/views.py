from rest_framework.generics import CreateAPIView
from rest_framework.mixins import ListModelMixin
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import OfficeSerializer
from .models import OfficeModel


class OfficeView(ListModelMixin, CreateAPIView):
    serializer_class = OfficeSerializer
    # authentication_classes = [JWTAuthentication] //если отдельно а не на все
    permission_classes = [IsAuthenticated]

    # queryset = OfficeModel.objects.all()

    def get_queryset(self):
        params = self.request.query_params
        id = params.get('id', None)
        if not id:
            return OfficeModel.objects.all()
        return OfficeModel.objects.filter(id=id)

    def get(self, request, *args, **kwargs):
        # if request.method == 'GET':
        #     self.serializer_class =
        return self.list(request, *args, **kwargs)
