from django.shortcuts import redirect
from django.urls import reverse


class ProfileCompletionMiddleware:

    def __init__(self, get_response):
        "Middleware initialization"
        self.get_response = get_response

    def __call__(self, request):
        # Code to be executed for each request/response after
        # the view is called.
        if not request.user.is_anonymous:
            profile = request.user.profile
            if not profile.picture or not profile.biography:
                if request.path not in [reverse('users_my_profile_url'), reverse('posts_logout_url')]:
                    return redirect('users_my_profile_url')

        response = self.get_response(request)
        return response
