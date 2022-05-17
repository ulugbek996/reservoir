from rest_framework import serializers
from .models import Reservoir,Target,Indicator,History

class ReservoirSerializers(serializers.ModelSerializer):
    class Meta:
        model=Reservoir
        fields=['id','user', 'rname','targets_number','rimage','rregion','rdistrict']

class TargetSerializer(serializers.ModelSerializer):

    class Meta:
        model=Target
        fields=['id','t_user','target_name', 'k1value', 'k2value', 'k3value', 'timage', 'resevoirid']

class IndicatorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Indicator
        fields=['id','i_user','iname','parametres','targetid']

class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model=History
        fields=['id','h_user','hreservoirid','htargetid','indicatorid','hvalue']   



