from django.shortcuts import render
import requests

# Create your views here.
def index(request):
    if request.method == "POST":
        githubname = request.POST.get("githubname")

        user_url = "https://api.github.com/users/" + githubname
        response_user = requests.get(user_url)
        user_info = response_user.json()

        repos_url = "https://api.github.com/users/" + githubname + "/repos"
        response_repos = requests.get(repos_url)
        repos_info = response_repos.json()

        if "message" in user_info:
            return render(request,"index.html",{"message": "Böyle bir kullanıcı bulunamadı"})

    else:
        return render(request,"index.html")

    return render(request,"index.html",{"profile": user_info, "repos": repos_info})