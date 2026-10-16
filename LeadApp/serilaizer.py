from django.contrib.auth.models import User
from LeadApp.models import LeadModel
from rest_framework import serializers

class LeadSerilaizer(serializers.ModelSerializer):
    # source=serializers.ChoiceField(choice=LeadModel.SOURCE_CHOICES)
    class Meta:
        model=LeadModel
        fields="__all__"
        read_only_fields=['id','added_date']