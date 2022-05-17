
from django.shortcuts import get_object_or_404
from rest_framework import status
from .serializers import ReservoirSerializers,TargetSerializer,IndicatorSerializer,HistorySerializer
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import serializers

from .models import Reservoir,Target,Indicator,History


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def ReservoirList(request):
    queryset=Reservoir.objects.filter(user=request.user)
    serializer_class=ReservoirSerializers(queryset,many=True)

    if queryset:
        return Response(serializer_class.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)    


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def ReservoirDetail(request,pk):
    queryset=Reservoir.objects.get(id=pk,user=request.user)
    serializer_class=ReservoirSerializers(queryset,many=False)

    if queryset:
        return Response(serializer_class.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def ReservoirCreate(request):
    data = dict(request.data)
    data['user'] = request.user.id
    serializer_class=ReservoirSerializers(data=data)

    if Reservoir.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')

    serializer_class.is_valid(raise_exception=True)
    serializer_class.save()
    return Response(serializer_class.data)
  
@api_view(['POST'])
def ReservoirUpdate(request,pk):
    queryset=Reservoir.objects.get(id=pk)
    serializer_class=ReservoirSerializers(instance=queryset,data=request.data)

    if serializer_class.is_valid():
        serializer_class.save()
        return Response(serializer_class.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)    

@api_view(['DELETE'])
def ReservoirDelete(request,pk):
    queryset=get_object_or_404(Reservoir,id=pk)
    queryset.delete()

    return Response(status=status.HTTP_202_ACCEPTED)           

@api_view(['GET'])
def TargetList(request):
    queryset=Target.objects.filter(t_user=request.user)
    serializer_class=TargetSerializer(queryset,many=True)

    if queryset:
        return Response(serializer_class.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)    


@api_view(['GET'])
def TargetDetail(request,pk):
    queryset=Target.objects.get(id=pk,t_user=request.user)
    serializer_class=TargetSerializer(queryset,many=False)

    if queryset:
        return Response(serializer_class.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    

@api_view(['POST'])
def TargetCreate(request):
    data=dict(request.data)
    data['t_user']=request.t_user.id
    serializer_class=TargetSerializer(data=request.data)

    if Target.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')   
    serializer_class.is_valid(raise_exception=True)
    serializer_class.save()
    return Response(serializer_class.data)
          

@api_view(['POST'])
def TargetUpdate(request,pk):
    queryset=Target.objects.get(id=pk)
    serializer_class=TargetSerializer(instance=queryset,data=request.data)

    if serializer_class.is_valid():
        serializer_class.save()
        return Response(serializer_class.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
@api_view(['DELETE'])
def TargetDelete(request,pk):
    queryset=Target.objects.get(id=pk)
    queryset.delete()
    return Response(status=status.HTTP_200_OK)

@api_view(['GET'])
def IndicatorList(request):
    indicators=Indicator.objects.filter(i_user=request.user)
    serializers=IndicatorSerializer(indicators,many=True)
    if serializers:
        return Response(serializers.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    

@api_view(['GET'])
def IndicatorDetail(request,pk):
   
    indicators=Indicator.objects.get(id=pk,i_user=request.user)
    serializer=IndicatorSerializer(indicators,many=True)
    if serializer:
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def IndicatorCreate(request):
    data=dict(request.data)
    data['i_user']=request.i_user.id
    serializer=IndicatorSerializer(data=request.data)

    if Indicator.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')

    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)
       

@api_view(['POST'])
def IndicatorUpdate(request,pk):
    indicators=Indicator.objects.get(id=pk)
    serializer=IndicatorSerializer(instance=indicators,data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data) 
    else:
        return Response(status=status.HTTP_404_NOT_FOUND) 
@api_view(['DELETE'])
def IndicatorDelete(request,pk):
    indicator=get_object_or_404(Indicator,id=pk)
    indicator.delete()
    return Response(status=status.HTTP_200_OK)

@api_view(['GET'])
def HistoryList(request):
    history=History.objects.filter(h_user=request.user)
    serializer=HistorySerializer(history,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def HistoryDetail(request,pk):
    try:
        history=History.objects.get(id=pk,h_user=request.user)
    except History.DoesNotExist:
        history=None

    serializer=HistorySerializer(history,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def HistoryCreate(request):
    data=dict(request.data)
    data['h_user']=request.user.id
    serializer=HistorySerializer(data=request.data)
    if History.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')

    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)
    

@api_view(['POST'])
def HistoryUpdate(request,pk):
    history=History.objects.get(id=pk)
    serializer=HistorySerializer(instance=history,data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data) 
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
@api_view(['DELETE'])
def HistoryDelete(request,pk):
    history=get_object_or_404(History,id=pk)
    history.delete()
    return Response(status=status.HTTP_202_ACCEPTED)          