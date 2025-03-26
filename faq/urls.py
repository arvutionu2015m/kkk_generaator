from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('genereeri/', views.generate_faq_view, name='generate_faq'),
    path('admin/faqs/', views.admin_review_faqs, name='admin_review_faqs'),
    path('admin/faqs/approve/<int:faq_id>/', views.approve_faq, name='approve_faq'),
    path('admin/faqs/delete/<int:faq_id>/', views.delete_faq, name='delete_faq'),
]