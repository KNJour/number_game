from django.shortcuts import render, redirect
import random

# Create your views here.
def index(request):
    try:
        request.session['number']
        if not 'number' in request.session:
            print("try working")
            request.session["number"] = random.randint(1, 100)
        if not 'attempts' in request.session:
            request.session["attempts"] = 0
    except:
        print('No random number path')
        request.session["number"] = random.randint(1, 100)
        request.session["attempts"] = 0

    return render(request, "index.html")    

def attempt(request):
    guess = request.POST.get("guess")
    print(guess)
    guess = int(guess)
    request.session["attempts"] += 1
    
    if guess == request.session["number"]:
        request.session['response'] = "You guessed correctly!"
    elif guess > request.session["number"]:
        request.session['response'] = "Too high!"
    elif guess < request.session["number"]:
        request.session['response'] = "Too low!"

    return redirect('/')  

def reset(request):
    request.session.flush()
    return redirect("/")