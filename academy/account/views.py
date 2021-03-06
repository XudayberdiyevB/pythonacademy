from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail, BadHeaderError
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
# Create your views here.
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from problems.models import UserRatingSystem, ProblemModel, ProblemAnswerModelUser
from blogs.models import BlogModel
from quiz.models import Progress
from home.models import AdmingaXabar, UsergaJavob


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        u = User.objects.filter(username=username)
        if u.exists():
            messages.warning(request, 'xatolik')
            return redirect('account:login')
        else:
            user1 = User(username=username, email=email, password=make_password(password))
            user1.save()
            return redirect('account:login')
    return render(request, 'account/register.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home:homepage')
    return render(request, 'account/login.html')


def logout_view(request):
    logout(request)
    return redirect('home:homepage')


@login_required
def profile(request, user):
    filter_user = User.objects.filter(username=user)[0]
    all_prob = ProblemModel.objects.all().count()
    filter_prob = ProblemAnswerModelUser.objects.filter(user=filter_user, is_correct=True).count()
    fil_ans = ProblemAnswerModelUser.objects.filter(user=filter_user)
    filter_us = None
    if fil_ans:
        filter_us = UserRatingSystem.objects.get(user=filter_user)
        filter_us.rating_ball = filter_prob
        filter_us.save()
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=filter_user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=filter_user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('account:profile', request.user.username)
    else:
        u_form = UserUpdateForm(instance=filter_user)
        p_form = ProfileUpdateForm(instance=filter_user)
    my_blogs = BlogModel.objects.filter(author=filter_user)
    # exam_results = Progress.objects.filter(user=filter_user)[0]
    context = {
        'u_form': u_form,
        'p_form': p_form,
        'current_odam': filter_user,
        'filter_us': filter_us,
        'all_prob': all_prob,
        'my_blogs': my_blogs
    }
    return render(request, 'account/profile.html', context)


def all_users(request):
    al_users = User.objects.all()
    if request.method == 'POST':
        text = request.POST['search']
        filter_users = User.objects.filter(username__icontains=text)
        return render(request, 'account/all_users.html', {'all_users': filter_users})
    return render(request, 'account/all_users.html', {'all_users': al_users})


@login_required
def support(request):
    usermsg = None
    adminmsg = None
    if request.user.is_authenticated:
        usermsg = AdmingaXabar.objects.filter(user=request.user)
        adminmsg = UsergaJavob.objects.filter(send_to=request.user)
    if request.method == 'POST' is not None and 'supportchat' in request.method and request.POST != None:
        msg = request.POST.get['supportchat']
        u = AdmingaXabar(user=request.user, text=msg)
        u.save()
        return redirect('account:support')
    context = {
        'usermsg': usermsg,
        'adminmsg': adminmsg
    }
    return render(request, 'account/support.html', context)

def password_reset_request(request):
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = User.objects.filter(Q(email=data))
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "account/password_reset_email.txt"
                    c = {
                        "email": user.email,
                        'domain': '127.0.0.1:8000',
                        'site_name': 'Website',
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "user": user,
                        'token': default_token_generator.make_token(user),
                        'protocol': 'http',
                    }
                    email = render_to_string(email_template_name, c)
                    try:
                        send_mail(subject, email, 'admin@example.com', [user.email], fail_silently=False)
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                    return redirect("account:password_reset_done")
    password_reset_form = PasswordResetForm()
    return render(request=request, template_name="account/password_reset.html",
                  context={"password_reset_form": password_reset_form})
