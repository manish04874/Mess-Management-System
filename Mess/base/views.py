from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from .models import meal, Category, Attendance, Feedback, MealTicket
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from datetime import date
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.db.models import Q

def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username = username)
        except:
            messages.error(request, 'user does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'username or password does not exist')

    context = {'page':page}
    return render(request, 'base/login_register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')

def registerPage(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occurred during registration')

    return render(request, 'base/login_register.html', {'form':form})



def userProfile(request, pk):
    user = User.objects.get(id=pk)
    meal_ticket = MealTicket.objects.all()
    attendance = Attendance.objects.all()
    context = {'user': user, 'meal_tickets': meal_ticket, 'attendance':attendance}
    return render(request, 'base/profile.html', context)




def home(request):
    meals = meal.objects.all()
    categories = Category.objects.all()

    return render(request, 'base/home.html', { 'meals': meals, 'categories':categories })

def contact(request):
    return render(request, 'base/contact.html')

def about(request):
    return render(request, 'base/about.html')

def mealss(request):
    category = request.GET.get('category')
    meals = meal.objects.all()
    categories = Category.objects.all()

    if category:
        meals = meals.filter(category__name=category)
    
    context = {'meals': meals, 'categories': categories}
    return render(request, 'base/meal.html', context)

def detail(request, pk):
    categories = Category.objects.all()
    meals = get_object_or_404(meal, pk=pk)
    return render(request, 'base/detail.html', {'meal': meals, 'categories':categories})

@login_required(login_url='login')
def search(request):
    query = request.GET.get('query')
    if query:
        meals = meal.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
    else:
        meals = meal.objects.all()
    return render(request, 'base/search_results.html', {'meals': meals, 'query': query})



def feedback(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        feedback = request.POST.get('feedback')
        feedback = Feedback(name=name, email=email, feedback=feedback)
        user = feedback.save()
        return HttpResponse('<h1>Feedback Submitted</h1>')

    return render(request, 'base/feedback.html')



from django.utils import timezone

@login_required
def buy_meal(request, category_id):
    category = get_object_or_404(Category, pk=category_id)

    meal_ticket = MealTicket.objects.create(
        user=request.user,
        category=category,
        date=timezone.now().date()
    )
    attendance, created = Attendance.objects.get_or_create(student=request.user, date=date.today())

    category.attendance = attendance
    category.save()
    
    return render(request, 'base/ticket.html', {'meal_ticket': meal_ticket})


def myticket(request):
    meal_ticket = MealTicket.objects.all()
    return render(request, 'base/mytickets.html', {'meal_tickets': meal_ticket})