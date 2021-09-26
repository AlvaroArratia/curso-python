from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from appApi.models import User

# Create your views here.
def index(request):
    return JsonResponse(
        {
            "AAA": "BBB",
        }
    )


def create_user(request):
    if request.method == "POST":
        try:
            user = User(
                name=request.POST.get("name"),
                email=request.POST.get("email"),
                password=request.POST.get("password"),
            )
            user.save()
            return JsonResponse(
                {
                    "name": request.POST.get("name"),
                    "email": request.POST.get("email"),
                    "password": request.POST.get("password"),
                }
            )
        except Exception as err:
            print(err.__name__() + ": " + str(err))
    else:
        return HttpResponse("Wrong http method")


def get_user_by_id(request):
    pass


def get_users(request):
    pass


def update_user(request):
    pass


def delete_user(request):
    pass
