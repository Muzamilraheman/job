from django.urls import path
from jobapp import views

from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *
 

app_name = "jobapp"


urlpatterns = [

    path('', views.home_view, name='home'),
    #path('user/edit',views.user_profile,name='user_profile'),
    path('jobs/', views.job_list_View, name='job-list'),
    path('jobs/know/', views.job_list_View, name='job-list'),
    path('job/create/', views.create_job_View, name='create-job'),
    path('job/<int:id>/', views.single_job_view, name='single-job'),
    path('apply-job/<int:id>/', views.apply_job_view, name='apply-job'),
    path('bookmark-job/<int:id>/', views.job_bookmark_view, name='bookmark-job'),
    path('about/', views.single_job_view, name='about'),
    path('contact/', views.single_job_view, name='contact'),
    path('result/', views.search_result_view, name='search_result'),
    path('result/know/', views.search_result_view, name='search_result'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('know/', views.know, name='know'),
    path('profile_user/',views.user_profile,name='user_profile'),
    path('dashboard/employer/job/<int:id>/applicants/', views.all_applicants_view, name='applicants'),
    path('dashboard/employer/job/edit/<int:id>', views.job_edit_view, name='edit-job'),
    path('dashboard/employer/applicant/<int:id>', views.applicant_details_view, name='applicant-details'),
    path('dashboard/employer/applicant/resume/', views.user_resume, name='user_resume'),
    
    path('dashboard/employer/close/<int:id>/', views.make_complete_job_view, name='complete'),
    path('dashboard/employer/delete/<int:id>/', views.delete_job_view, name='delete'),
    path('dashboard/employee/delete-bookmark/<int:id>/', views.delete_bookmark_view, name='delete-bookmark'),
    path('image_upload/', views.hotel_image_view, name='image_upload'),
    # path('profile_user/image_upload/', views.hotel_image_view, name='image_upload'),
    # path('success', views.success, name='success'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
