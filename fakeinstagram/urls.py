from django.contrib import admin
from django.urls import path
from fakeinstagram import views as local_views
from posts import views as posts_views
from users import views as user_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
                  # Local views
                  path('admin/', admin.site.urls),
                  path('helloWord/', local_views.hello_word, name='hello_word_url'),
                  path('sorted/', local_views.sort_integer, name='sorted_url'),
                  path('sayHi/<str:name>/<int:age>/', local_views.say_hi, name='say_hi_url'),
                  # Posts views
                  path('showAllPosts/', posts_views.show_all_views, name='show_all_post_url'),
                  # User view
                  path('users/login/', user_views.login_views, name='users_login_url'),
                  path('users/logout/', posts_views.log_out, name='posts_logout_url'),
                  path('users/signup/', user_views.sing_up, name='users_signup_url'),
                  path('users/myprofile/', user_views.my_profile, name='users_my_profile_url')
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
