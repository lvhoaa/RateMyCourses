from django.shortcuts import render, redirect
from .models import Course 
from .forms import CreateNewRating
import datetime
from .chatgpt import chatgpt_summarize
from .profanity_check import profanity_check

def home(request):
    # with open("main\data\courses.json") as json_data:
    #     courses =json.load(json_data)
    courses = Course.objects.all()
    
    return render(request,'home.html',{"courses":courses})

def courseHome(request,courseCode):
    currentCourse = Course.objects.get(code=courseCode)
    
    ratings = currentCourse.rating_set.all()
    
    # Rating Stats Calculation
    avg_stars=0
    avg_grade=0
    avg_difficulty=0
    num_rating=0
    for rating in ratings:
        avg_stars+=rating.stars
        
        if rating.grade=="A":
            avg_grade +=4.0
        elif rating.grade=="A-":
            avg_grade+=3.7
        elif rating.grade=="B+":
            avg_grade+=3.3
        elif rating.grade=="B":
            avg_grade+=3 
        elif rating.grade=="B-":
            avg_grade+=2.7
        elif rating.grade=="C+":
            avg_grade+=2.3
        elif rating.grade=="C":
            avg_grade+=2
        elif rating.grade=="C-":
            avg_grade+=1.7
        elif rating.grade=="D+":
            avg_grade+=1.3
        elif rating.grade=="D":
            avg_grade+=1
        
        avg_difficulty+=rating.difficulty 
        num_rating+=1 
    if num_rating>0:
        avg_stars=round(avg_stars/num_rating,1)
        avg_grade=round(avg_grade/num_rating,1)
        avg_difficulty=round(avg_difficulty/num_rating,1)
    else:
        avg_stars="N/A"
        avg_grade="N/A"
        avg_difficulty="N/A"
    if request.method=='POST':
        form = CreateNewRating(request.POST)
        if form.is_valid():
            stars = form.cleaned_data['stars']
            grade = form.cleaned_data['grade']
            difficulty = form.cleaned_data['difficulty']
            comment = form.cleaned_data['comment']
            anonymous = form.cleaned_data['anonymous']
            if profanity_check(comment):
                user = request.user
                user.delete()
                return redirect('/ban/'+user.username)
            
            else:
                summary = chatgpt_summarize(comment)
                print(summary)
                summary_word1=summary.split('.')[0].split(",")[0].upper()
                summary_word2=summary.split('.')[0].split(",")[1].upper()
                summary_word3=summary.split('.')[0].split(",")[2].upper()        
                currentCourse.rating_set.create(author=request.user.username,stars=stars,grade=grade,difficulty=difficulty,comment=comment,date=datetime.datetime.now(),anonymous=anonymous,summary_word1=summary_word1,summary_word2=summary_word2,summary_word3=summary_word3)
                return redirect('/course/'+courseCode)
            
    form = CreateNewRating()
    return render(request,'course.html',{"course":currentCourse,"ratings":ratings,"form":form,"range":range(1,6),"avg_stars":avg_stars,"avg_grade":avg_grade,"avg_difficulty":avg_difficulty})


def banBadWords(request,username):
    return render(request,'ban.html',{"username":username})
    