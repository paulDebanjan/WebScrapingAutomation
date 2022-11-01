
from django.urls import path
from . import views

app_name = "dataCapture"
urlpatterns = [
    path(
        route='',
        view=views.searchIndex,
        name='dataCaptureHome'
    ),
    # path(
    #     route='student/',
    #     view=students.StudentSignUpView.as_view(),
    #     name='studentSignUp'
    # ),
    
]
