from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
# Create your views here.
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from problems.models import UserRatingSystem,ProblemModel,ProblemAnswerModelUser

def register(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        u=User.objects.filter(username=username)
        if u.exists():
            messages.warning(request,'xatolik')
            return redirect('account:register')
        else:
            user1=User(username=username,email=email,password=make_password(password))
            user1.save()
            return redirect('account:login')
    return render(request,'account/register.html')

def login_view(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('home:homepage')
    return render(request,'account/login.html')

def logout_view(request):
    logout(request)
    return redirect('home:homepage')


@login_required
def profile(request,user):

    filter_user=User.objects.filter(username=user)[0]

    all_prob=ProblemModel.objects.all().count()
    filter_prob=ProblemAnswerModelUser.objects.filter(user=filter_user,is_correct=True).count()
    fil_ans=ProblemAnswerModelUser.objects.filter(user=filter_user)
    filter_us=None
    if fil_ans:
        filter_us=UserRatingSystem.objects.get(user=filter_user)
        filter_us.rating_ball=filter_prob
        filter_us.save()

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=filter_user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=filter_user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            
            return redirect('account:profile')

    else:
        u_form = UserUpdateForm(instance=filter_user)
        p_form = ProfileUpdateForm(instance=filter_user)

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'current_odam':filter_user,
        'filter_us':filter_us,
        'all_prob':all_prob
    }

    return render(request, 'account/profile.html', context)


def all_users(request):
    al_users=User.objects.all()
    return render(request,'account/all_users.html',{'all_users':al_users})