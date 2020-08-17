# from django_offices2.office.models import OfficeModel
#
#
# office = OfficeModel.objects.get(pk=1)
#
# office = OfficeModel.objects.get(name__startswith='q')
#
# office = OfficeModel.objects.all()
#
# office = OfficeModel.objects.filter(name__startswith='s')
#
# office = OfficeModel.objects.order_by('name')
# office = OfficeModel.objects.order_by('-name')
#
# office = OfficeModel.objects.filter(name__startswith='s').order_by('name')
#
# office = OfficeModel.objects.order_by('price')
#
#
# office = OfficeModel.objects.filter(price__lt=1000).order_by('price')
# office = OfficeModel.objects.filter(price__lte=1000).order_by('price')
#
# office = OfficeModel.objects.filter(price__gt=1000).order_by('price')
#
#
# # aggregation
# from django.db import models
#
# office = OfficeModel.objects.aggregate(models.Avg('price'), models.Max('price'))
#
#
# office = OfficeModel.objects.all()[1:2]
