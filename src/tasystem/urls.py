from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path

# from signup.views import signup_view
# from add_course.views import add_course_view
# from course_list.views import course_list_view, professor_courses_view
from users.views import register as register_view
from users.views import profile as profile_view
# from apply.views import apply_view
# use this if you want different landing pages per user type
# from landing_page.views import student_view, professor_view, admin_view
from landing_page.views import landing_view
from add_course.views import CourseCreateView
from apply.views import ApplyView, ApplicationsListView, StudentApplicationsListView, ApplicationDeleteView
from course_list.views import CourseListView, ProfessorCoursesView
# Can't render add_course if the view is from pages for some reason
urlpatterns = [
    path('', landing_view, name='home'),
    path('signup/', register_view, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name="users/login.html"), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name="users/logout.html"), name='logout'),
    path('profile/', profile_view, name='profile'),
    
    
    path('add_course/', CourseCreateView.as_view(), name='add_course'),
    path('apply/<int:app_id>/', ApplyView.as_view(), name='apply'),
    path('course_list/', CourseListView.as_view(), name='course_list'),
    path('course_list/<int:pk>/', ProfessorCoursesView.as_view(), name='professor_courses'),
    path('professor_applications/', ApplicationsListView.as_view(), name='professor_applications'),
    path('student_applications/', StudentApplicationsListView.as_view(), name='student_applications'),
    path('application_confirm_delete/<int:pk>/', ApplicationDeleteView.as_view(), name='application_confirm_delete'),


    path('send_offer_email/', ApplicationsListView.send_offer_email, name = 'send_offer_email'),


    # path('course_list/', course_list_view, name='course_list'),
    
    # path('add_course/', add_course_view, name='add_course'),
    
    # path('course_list/apply/<int:app_id>/', apply_view, name='apply'),
    path('landing/<str:email>/<str:usertype>/', landing_view, name = 'landing'),
    # use this if you want different landing pages per user type
    # path('student/', student_view, name = 'student'),
    # path('professor/', professor_view, name = 'professor'),
    # path('bcadmin/', admin_view, name = 'admin'),
    path('admin/', admin.site.urls),
]
