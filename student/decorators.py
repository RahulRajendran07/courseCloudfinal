from django.shortcuts import redirect

from django.contrib import messages

def signin_required(fn):

    def wrapper(request,*args,**kwargs):
        messages.error(request,"Signin Required")

        if not request.user.is_authenticated:

            return redirect('signin')
        
        else:

            return fn(request,*args,**kwargs)
        
    return wrapper