from django.urls import path
from .views import AllBranchView, BranchDetailView

app_name = 'api'


urlpatterns = [
    path('branches/<str:bank_name>/<str:city>', AllBranchView.as_view(), name='get-branches'),
    path('detail/<str:ifsc>/', BranchDetailView.as_view(), name='get-details')
]
