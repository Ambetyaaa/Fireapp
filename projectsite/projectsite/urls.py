from django.contrib import admin
from django.urls import path

from fire.views import *
from fire import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', HomePageView.as_view(), name='home'),
    path('dashboard_chart', ChartView.as_view(), name='dashboard-chart'),
    path('chart/', PieCountbySeverity, name='chart'),
    path('lineChart/', LineCountbyMonth, name='chart'),
    path('multilineChart/', MultilineIncidentTop3Country, name='chart'),
    path('multiBarChart/', MultiBarbySeverity, name='chart'),
    path('stations', views.map_station, name='map-station'),
    path('incidents', views.map_incident, name='map-incident'),
    path('firestationlist', FireStationList.as_view(), name='firestation-list'),
    path('firestationlist/add', FireStationCreateView.as_view(), name='firestation-add'),
    path('firestationlist/<pk>', FireStationUpdateView.as_view(), name='firestation-update'),
    path('firestationlist/<pk>/delete', FireStationDeleteView.as_view(), name='firestation-delete'),
    path('incidentlist', IncidentList.as_view(), name='incident-list'),
    path('incidentlist/add', IncidentCreateView.as_view(), name='incident-add'),
    path('incidentlist/<pk>', IncidentUpdateView.as_view(), name='incident-update'),
    path('incidentlist/<pk>/delete', IncidentDeleteView.as_view(), name='incident-delete'),
    path('locationlist', LocationList.as_view(), name='location-list'),
    path('locationlist/add', LocationCreateView.as_view(), name='location-add'),
    path('locationlist/<pk>', LocationUpdateView.as_view(), name='location-update'),
    path('locationlist/<pk>/delete', LocationDeleteView.as_view(), name='location-delete'),
    path('firetrucklist', FireTruckList.as_view(), name='firetruck-list'),
    path('firetrucklist/add', FireTruckCreateView.as_view(), name='firetruck-add'),
    path('firetrucklist/<pk>', FireTruckUpdateView.as_view(), name='firetruck-update'),
    path('firetrucklist/<pk>/delete', FireTruckDeleteView.as_view(), name='firetruck-delete'),
    path('firefighters_list', FireFighterList.as_view(), name='firefighter-list'),
    path('firefighters_list/add', FireFighterCreateView.as_view(), name='firefighter-add'),
    path('firefighters_list/<pk>', FireFighterUpdateView.as_view(), name='firefighter-update'),
    path('firefighters_list/<pk>/delete', FireFighterDeleteView.as_view(), name='firefighter-delete'),
    path('weatherconditionlist', WeatherConditionList.as_view(), name='weathercondition-list'),
    path('weatherconditionlist/add', WeatherConditionCreateView.as_view(), name='weathercondition-add'),
    path('weatherconditionlist/<pk>', WeatherConditionUpdateView.as_view(), name='weathercondition-update'),
    path('weatherconditionlist/<pk>/delete', WeatherConditionDeleteView.as_view(), name='weathercondition-delete'),

]
