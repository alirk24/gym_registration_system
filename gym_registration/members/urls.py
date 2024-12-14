from django.urls import path
from . import views



urlpatterns = [
    path('register/', views.register_member, name='register_member'),
    path('members/', views.member_list, name='member_list'),
    path('edit/<int:member_id>/', views.edit_member, name='edit_member'),
    path('logout/', views.logout_view, name='logout'),
    path('members/extend/<int:member_id>/', views.extend_membership, name='extend_membership'),
    path('members/delete/<int:member_id>/', views.delete_member, name='delete_member'),
]