from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

from django.db.models import Q, Count
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.models import Group, User

from datetime import datetime, date, timedelta
import random
# Create your views here.
from accounts.models import *
from room.models import *


@login_required(login_url='login')
def home(request):
    role = str(request.user.groups.all()[0])
    if role != "guest":
        return redirect("employee-profile", pk=request.user.id)
    else:
        return redirect("guest-profile", pk=request.user.id)
