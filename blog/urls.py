from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.home, name='homepage'),

    # drafts 
    
    path('accounts/<str:username>/drafts/', views.DraftListView.as_view(), name='user_drafts'),

    path('accounts/<str:username>/draft/new/', views.DraftCreateView.as_view(), name='create-draft'),

    path('<str:username>/draft/<str:slug>/', views.DraftDetailView.as_view(), name='draft-detail'),

    path('<str:username>/draft/<str:slug>/update/', views.DraftUpdateView.as_view(), name='update-draft'),

    path('<str:username>/draft/<str:slug>/delete/', views.DraftDeleteView.as_view(), name='delete-draft'),
]
