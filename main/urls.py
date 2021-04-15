from django.contrib import admin
from django.urls import path, include
from main.views import ReportCreateView, ReportDetailView, ReportUpdateView, ReportDeleteView
from . import views
from users.views import ProfileDetailView

urlpatterns = [
    path('', views.overview, name='overview'),
    path('reports/', views.reports_page, name='reports-page'),
    path('report/new/', ReportCreateView.as_view(), name='report-create'),
    path('report/<int:pk>/', ReportDetailView.as_view(), name="report-detail"),
    path('profile/<int:pk>/', ProfileDetailView.as_view(), name='profile-detail'),
    path('report/<int:pk>/update/', ReportUpdateView.as_view(), name='report-update'),
    path('report/<int:pk>/delete/', ReportDeleteView.as_view(), name='report-delete')
]
