# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import viewsets
from models import Ivr
from serializers import IvrSerializer
from datetime import date

# Create your views here.

class ivrViewSet(viewsets.ModelViewSet):
    today = date.today()
    queryset=Ivr.objects.filter(tarix__year=today.year,tarix__month=today.month)
    print(today)
    serializer_class = IvrSerializer