
from django.contrib import admin
from django.urls import path, include

from myapp import views

urlpatterns = [
    path('login/',views.login),
    path('view_book_tickets/',views.view_book_tickets),
    path('view_compliants/',views.view_compliants),
    path('sent_reply/',views.sent_reply),
    path('admin_changepassword/',views.admin_changepassword),
    path('add_station/',views.add_station),
    path('view_station/',views.view_station),
    path('add_boat/',views.add_boat),
    path('view_boat/',views.view_boat),
    path('delete_station/',views.delete_station),
    path('delete_boat/',views.delete_boat),
    path('view_payments/',views.view_payments),
    path('add_schedule/',views.add_schedule),
    path('view_users/',views.view_users),
    path('admin_view_services/',views.admin_view_services),




    path('reg/',views.reg),
    path('edit_userprofile/',views.edit_userprofile),
    path('view_profile/',views.view_profile),
    path('send_complaint/',views.send_complaint),
    path('user_view_complaints/',views.user_view_complaints),
    path('userview_boat/',views.userview_boat),
    path('view_services/',views.view_services),
    path('booking/',views.booking),
    path('view_tickets/',views.view_tickets),
    path('user_changepassword/',views.user_changepassword),
    path('and_userpayment/',views.and_userpayment),
    path('view_payment/',views.view_payment),

]
