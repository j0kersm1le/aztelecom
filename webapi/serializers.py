from rest_framework import serializers
from .models import Ivr 

class IvrSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ivr
        fields=('full_name','hal','sobe')