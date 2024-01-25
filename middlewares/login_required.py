from django.contrib.auth.decorators import login_required


class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        if getattr(view_func, "login_exempt", False):
            return

        if request.user.is_authenticated:
            return

        if not request.user.is_authenticated:
            return login_required(view_func)(request, *view_args, **view_kwargs)
