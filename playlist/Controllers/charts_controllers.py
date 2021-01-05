from django.shortcuts import render
from django.core.paginator import Paginator
from django.forms.models import model_to_dict
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from playlist.models.Charts import Charts

def index(request):
    if request.method == 'POST':
        
        req = request.POST.dict()  
        name = req['name']
        type = req['size_filter']
        diameter = req['diameter']
        sizes = Size.objects.all()
        if name:  # filter name
            sizes = sizes.filter(name__contains=name)
        if type and diameter:  # type and diameter are filled
            if type == 'equal':
                sizes = sizes.filter(diameter=diameter)
            elif type == 'less_than':
                sizes = sizes.filter(diameter__lt=diameter)
            elif type == 'less_than_equal':
                sizes = sizes.filter(diameter__lte=diameter)
            elif type == 'more_than':
                sizes = sizes.filter(diameter__gt=diameter)
            elif type == 'more_than_equal':
                sizes = sizes.filter(diameter__gte=diameter)
    else:
        sizes = Size.objects.all()
    data = {
        'sizes': sizes,
    }
    return render(request, 'size/index.html', data)







