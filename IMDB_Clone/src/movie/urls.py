
from django.urls import path
from .views import MovieList, MovieDetail

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', MovieList.as_view(), name='movie_list'),
    path('<int:pk>', MovieDetail.as_view(), name='movie_detail'),

]
