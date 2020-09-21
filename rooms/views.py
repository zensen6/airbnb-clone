from datetime import datetime
from math import ceil
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.views.generic import ListView, DetailView
from django.urls import reverse
from django.http import Http404
from django_countries import countries
from . import models, forms
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
    

def search(request):

    form = forms.SearchForm()

    return render(request,"rooms/search.html", {"form":form})
    '''
    city = request.GET.get("city", "Anywhere")
    city = str.capitalize(city)
    country = request.GET.get("country", "KR")
    room_type = int(request.GET.get("room_type", 0))
    price = int(request.GET.get("price", 0))
    guests = int(request.GET.get("guests", 0))
    bedrooms = int(request.GET.get("bedrooms", 0))
    beds = int(request.GET.get("beds", 0))
    baths = int(request.GET.get("baths", 0))
    instant = bool(request.GET.get("instant", False))
    superhost = bool(request.GET.get("superhost", False))
    s_amenities = request.GET.getlist("amenities")
    s_facilities = request.GET.getlist("facilities")

    form = {
        "city": city,
        "s_room_type": room_type,
        "s_country": country,
        "price": price,
        "guests": guests,
        "bedrooms": bedrooms,
        "beds": beds,
        "baths": baths,
        "s_amenities": s_amenities,
        "s_facilities": s_facilities,
        "instant": instant,
        "superhost": superhost,
    }
    room_types = models.RoomType.objects.all()
    amenities = models.Amenity.objects.all()
    facilities = models.Facility.objects.all()

    choices = {
        "countries": countries,
        "room_types": room_types,
        "amenities": amenities,
        "facilities": facilities,
    }

    filter_args = {}

    if city != "Anywhere":
        filter_args["city__startswith"] = city

    filter_args["country"] = country

    if room_type != 0:
        filter_args["room_type__pk"] = room_type

    if price != 0:
        filter_args["price__lte"] = price

    if guests != 0:
            filter_args["guests__gte"] = guests

    if bedrooms != 0:
        filter_args["bedrooms__gte"] = bedrooms

    if beds != 0:
        filter_args["beds__gte"] = beds

    if baths != 0:
        filter_args["baths__gte"] = baths
    
    if instant is True:
        filter_args["instant_book"] = True

    if superhost is True:
        filter_args["host__superhost"] = True

    if len(s_amenities) > 0:
        for s_amenity in s_amenities:
            filter_args["amenities__pk"] = int(s_amenity)

    if len(s_facilities) > 0:
        for s_facility in s_facilities:
            filter_args["facilities__pk"] = int(s_facility)

    rooms = models.Room.objects.filter(**filter_args)

    return render(request, "rooms/search.html", {**form, **choices, "rooms": rooms})
    '''
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