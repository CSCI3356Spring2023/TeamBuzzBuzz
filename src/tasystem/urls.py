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
from system_active.views import system_closed_view
from add_course.views import (
    CourseCreateView,
    CourseUpdateView,
    DiscussionCreateView,
    DiscussionListView,
    DiscussionUpdateView
)

from add_oldcourse.views import OldCourseCreateView
from show_oldcourse.views import ProfessorOldCoursesView, NormalCourseListView
from student_oldcourse.views import StudentOldCoursesView
from apply.views import (ApplyView, ApplicationsListView,
                         StudentApplicationsListView, ApplicationDeleteView, ApplicationReviewView)
from course_list.views import CourseListView, ProfessorCoursesView, CourseDetailView, SuggestedCoursesView
from offers.views import OfferListStudentView, OfferListView, OfferListProfessorView

# Can't render add_course if the view is from pages for some reason
urlpatterns = [
    path('', landing_view, name='home'),
    path('landing/system_closed/', system_closed_view, name='system_closed_view'),

    path('signup/', register_view, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name="users/login.html"), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name="users/logout.html"), name='logout'),
    path('profile/', profile_view, name='profile'),

    path('add_course/', CourseCreateView.as_view(), name='add_course'),
    path('edit_course/<int:pk>/', CourseUpdateView.as_view(), name='edit_course'),
    path('add_discussion/<int:pk>/',
         DiscussionCreateView.as_view(), name='add_discussion'),
    path('discussion_list/<int:pk>/',
         DiscussionListView.as_view(), name='discussion_list'),
    path('edit_discussion/<int:pk>/',
         DiscussionUpdateView.as_view(), name='edit_discussion'),




    path('apply/<int:app_id>/', ApplyView.as_view(), name='apply'),
    path('course_list/', CourseListView.as_view(), name='course_list'),
    path('suggested_course_list/<int:pk>/',
         SuggestedCoursesView.as_view(), name='suggested_course_list'),
    path('course_list/<int:pk>/', ProfessorCoursesView.as_view(),
         name='professor_courses'),
    path('course_list_close_course/<int:pk>/',
         ProfessorCoursesView.change_course_status, name='change_course_status'),
    path('course_detail/<int:pk>/', CourseDetailView.as_view(),
         name='course_detail'),
    path('professor_applications/', ApplicationsListView.as_view(),
         name='professor_applications'),
    path('student_applications/', StudentApplicationsListView.as_view(),
         name='student_applications'),
    path('application_confirm_delete/<int:pk>/',
         ApplicationDeleteView.as_view(), name='application_confirm_delete'),
    path('application_review/<int:pk>/',
         ApplicationReviewView.as_view(), name='application_review'),
    path('student_offer/<int:pk>/',
         OfferListStudentView.as_view(), name='student_offers'),
    path('offer/', OfferListView.as_view(), name='admin_offers'),
    path('professor_offer/<int:pk>/',
         OfferListProfessorView.as_view(), name='professor_offers'),
    path('student_offer_accept/<int:pk>/',
         OfferListStudentView.acceptOffer, name='offer_accept'),
    path('student_offer_reject/<int:pk>/',
         OfferListStudentView.rejectOffer, name='offer_reject'),

    path('send_offer_email/<int:app_id>',
         ApplicationsListView.send_offer_email, name='send_offer_email'),

    path('add_oldcourse/', OldCourseCreateView.as_view(), name='add_oldcourse'),
    path('show_oldcourse/', NormalCourseListView.as_view(),
         name='show_normaloldcourse'),
    path('show_oldcourse/<int:pk>/',
         ProfessorOldCoursesView.as_view(), name='show_oldcourse'),
    path('save_old_course/<int:course_id>',
         NormalCourseListView.save_old_course, name='save_old_course'),

    path('show_student_old_course/<int:pk>',
         StudentOldCoursesView.as_view(), name='show_student_old_course'),
    # path('course_list/', course_list_view, name='course_list'),

    # path('add_course/', add_course_view, name='add_course'),

    # path('course_list/apply/<int:app_id>/', apply_view, name='apply'),
    path('landing/<str:email>/<str:usertype>/', landing_view, name='landing'),
    # use this if you want different landing pages per user type
    # path('student/', student_view, name = 'student'),
    # path('professor/', professor_view, name = 'professor'),
    # path('bcadmin/', admin_view, name = 'admin'),
    path('admin/', admin.site.urls),
]
