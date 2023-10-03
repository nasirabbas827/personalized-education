from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'), 
    path('signin/', views.signin, name='signin'),            
    path('logout/', views.custom_logout, name='logout'),         
    path('update_profile/', views.update_profile, name='update_profile'),
    path('change_password/', views.change_password, name='change_password'),
    path('quizzes/', views.available_quizzes, name='available_quizzes'),
    # Correct URL pattern name for attempting a specific quiz
    path('quiz/<int:quiz_id>/', views.attempt_quiz, name='attempt_quiz'),
    path('submit_quiz/<int:quiz_id>/', views.submit_quiz, name='submit_quiz'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
