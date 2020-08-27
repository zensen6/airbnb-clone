from datetime import datetime
from math import ceil
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.views.generic import ListView, DetailView
from django.urls import reverse
from django.http import Http404
from . import models
# Create your views here.


class HomeView(ListView):

    """HomeView Definition"""

    model = models.Room
    ordering = "created"
    paginate_by = 10
    paginate_orphans = 5
    context_object_name = "rooms"


class RoomDetail(DetailView):

    model = models.Room
    

'''
def room_detail(request, pk):

    try:
        room = models.Room.objects.get(pk=pk)
        return render(request, "rooms/detail.html", context={"room": room})
    except models.Room.DoesNotExist:
        raise Http404()
'''

'''
def all_rooms(request):
    
    page = request.GET.get('page', 1)
    #page = int(page or 1)
    #request.GET 은 :8000/?page=1?love=2&.. 식으로 query 인자 dict형태로 저장한거 보내주는거다
    #get은 {'page'=1,'love'=2}이면 dict['page'] 나 같다. 
    #만약 :8000/?page=2 이런식으로 page없는 query라면, page's default = 1 로 한다.
    room = models.Room.objects.all()
    paginator = Paginator(room, 10, orphans=5)
    try:
        return render(
            request,
            "rooms/home.html", 
            context={"page": paginator.page(int(page))}
        )
    except InvalidPage:
        return redirect("/")
    #-> paginator.page는 .get_page와 다르게
'''
'''
    page_size = 10
    limit = page_size * page
    offset = limit - page_size
    room = models.Room.objects.all()[offset:limit]
    page_count = ceil(models.Room.objects.count()/page_size)
    page_range = range(1, page_count)
    return render(request, "rooms/home.html", context={
        "room": room,
        "page_range": page_range,
        "page": page,
        "page_count": page_count
    })
'''