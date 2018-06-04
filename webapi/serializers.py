from rest_framework import serializers
from .models import Ivr
from datetime import date

class IvrSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ivr
        fields=('__all__')