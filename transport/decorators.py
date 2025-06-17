from django.contrib import messages
from django.shortcuts import redirect
from functools import wraps

def login_required_with_message(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.warning(request, "Please login first to continue.")
            return redirect(f'/accounts/login/?next={request.path}')
        return view_func(request, *args, **kwargs)
    return wrapper
