# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import viewsets
from models import Ivr
from serializers import IvrSerializer

# Create your views here.

class ivrViewSet(viewsets.ModelViewSet):
    queryset = Ivr.objects.all()
    serializer_class = IvrSerializer