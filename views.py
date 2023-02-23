from django.shortcuts import render,redirect
from .models import Swiggy
# Create your views here.

def home(request):
    s = Swiggy.objects.all()
    return render(request, 'index.html', {'swiggy':s})

def navigateForm(request, data=None):
    dataPresence = False
    if data:
        dataPresence = True
    return render(request, 'upload.html', {'data': data, 'dataPresence': dataPresence})

def pushData(request):
    if request.POST:
        restaurant = request.POST['rname']
        food = request.POST['fname']
        place = request.POST['place']
        cost = request.POST['price']
        rating = request.POST['rating']

        if request.POST.get('update', 0):
            id = request.POST['item-id']
            itemToBeUpdated = Swiggy.objects.get(id=id)
            itemToBeUpdated.restaurant = restaurant
            itemToBeUpdated.food = food
            itemToBeUpdated.cost = cost
            itemToBeUpdated.place = place
            itemToBeUpdated.rating = rating
            if request.FILES:
                itemToBeUpdated.image = request.FILES['image']
            itemToBeUpdated.save()
            return redirect('/')
        data = Swiggy(restaurant=restaurant, food=food, place=place,
                      cost=cost, rating=rating, image=request.FILES['image'])
        data.save()
        return redirect('/')
    return redirect('/form-data')

def deleteFood(request, id):
    Swiggy.objects.filter(id=id)[0].delete()
    return redirect('/')

def updateFood(request, id):
    data = Swiggy.objects.get(id=id)
    return navigateForm(request, data)