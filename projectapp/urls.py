
from django.urls import path
from .import views

urlpatterns=[
    #Reservoir
    path('reservoir/',views.ReservoirList),
    path('reservoir/<int:pk>/',views.ReservoirDetail),
    path('reservoir/create/',views.ReservoirCreate),
    path('reservoir/update/<int:pk>/',views.ReservoirUpdate),
    path('reservoir/delete/<int:pk>/',views.ReservoirDelete),

    #Target
    path('target/',views.TargetList),
    path('target/<int:pk>/',views.TargetDetail),
    path('target/create/',views.TargetCreate),
    path('target/update/<int:pk>/',views.TargetUpdate),
    path('target/delete/<int:pk>/',views.TargetDelete),

    #Indicator
    path('indicator/',views.IndicatorList),
    path('indicator/<int:pk>/',views.IndicatorDetail),
    path('indicator/create/',views.IndicatorCreate),
    path('indicator/update/<int:pk>/',views.IndicatorUpdate),
    path('indicator/delete/<int:pk>/',views.IndicatorDelete),

    #History
    path('history/',views.HistoryList),
    path('history/<int:pk>/',views.HistoryDetail),
    path('history/create/',views.HistoryCreate),
    path('history/update/<int:pk>/',views.HistoryUpdate),
    path('history/delete/<int:pk>/',views.HistoryDelete),
  
]