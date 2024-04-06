from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from django.contrib.auth.forms import UserCreationForm
from .forms import CreatUserForm
from .forms import ParentSignupForm, CreatUserForm
from .models import Workshop
from django.contrib.auth import logout
from .models import ParentProfile
from .forms import ParentProfileForm
from .forms import FeedbackForm
from .forms import Feedback
from .models import Comment
from django.http import HttpResponseBadRequest
from .forms import CommentForm  # אם יש לך טופס ספציפי לכך
from django.http import JsonResponse
from .forms import SummaryForm
from .forms import PsychologistCommentForm
from .models import PsychologistComment
from .models import InformationBoard
from .forms import InformationBoardForm
from .models import BabyHealth
from .forms import BabyHealthForm
from .forms import PediatricianInfoBoard



def loginpsychologist(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            users_in_group = Group.objects.get(name='Psychologist').user_set.all()
            if user in users_in_group:
                login(request, user)
                return redirect('homepageforpys')
            else:
                messages.info(request, 'Username or password incorrect')
        else:
            messages.info(request, 'Username or password incorrect')
    return render(request, 'loginpsychologist.html')


def index(request):
    return render(request, 'homepage.html')


def homepage(request):
    return render(request, 'homepage.html')


def psychomepage(request):
    return render(request, 'pyschhomepage.html')


def homepageforpys(request):
    return render(request, 'homepageforpys.html')


def schedulepys(request):
    return render(request, 'schedulepys.html')


def Workshopys(request):
    return render(request, 'Workshopys.html')


def loginpediatrician(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            users_in_group = Group.objects.get(name='pediatrician').user_set.all()
            if user in users_in_group:
                login(request, user)
                return redirect('pedhomepage')
            else:
                messages.info(request, 'Username or password incorrect')
        else:
            messages.info(request, 'Username or password incorrect')
    return render(request, 'loginpediatrician.html')


def pedhomepage(request):
    return render(request, 'pedhomepage.html')


def loginParent(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            users_in_group = Group.objects.get(name='Parent').user_set.all()
            if user in users_in_group:
                login(request, user)
                return redirect('parhomepage')
            else:
                messages.info(request, 'Username or password incorrect')
        else:
            messages.info(request, 'Username or password incorrect')
    return render(request, 'loginParent.html')


def parhomepage(request):
    return render(request, 'parhomepage.html')


def aboutus(request):
    return render(request, 'aboutus.html')


def contactus(request):
    return render(request, 'contactus.html')


def extrainfo(request, extrainfo=None):
    extrainfo = extrainfo.objects.all()
    return render(request, 'extrainfo.html', {extrainfo: extrainfo})


def parenthomepage(request):
    return render(request, 'parenthomepage.html')


def Schedule(request):
    return render(request, 'Schedule.html')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account was created for {username}')
            return redirect('homepageforparents')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def signupys(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account was created for {username}')
            return redirect('psychomepage')
    else:
        form = UserCreationForm()
    return render(request, 'signupys.html', {'form': form})


def signuped(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account was created for {username}')
            return redirect('pedhomepage')
    else:
        form = UserCreationForm()
    return render(request, 'signuped.html', {'form': form})


def add_workshop(request):
    if request.method == 'POST':
        workshop_name = request.POST.get('workshop_name')
        workshop_date = request.POST.get('workshop_date')
        workshop_time = request.POST.get('workshop_time')
        workshop_location = request.POST.get('workshop_location')

        # Create a new Workshop object
        workshop = Workshop.objects.create(
            name=workshop_name,
            date=workshop_date,
            time=workshop_time,
            location=workshop_location
        )

        return redirect('successpage')

    return render(request, 'addworkshopform.html')


def addworkshopform(request):
    return render(request, 'pyschhomepage.html')


def parentprofile(request):
    return render(request, 'parentprofile.html')


def successpage(request):
    return render(request, 'successhomepage.html')


def homepageforparents(request):
    return render(request, 'homepageforparents.html')


def logout_view(request):
    logout(request)
    # אפשר להוסיף הודעת התנתקות אם רוצים
    return redirect('homepage')


def contact_pys(request):
    return render(request, 'contact_pys.html')


def contact_doctor(request):
    return render(request, 'contact_doctor.html')


def articls(request):
    return render(request, 'articls.html')


def chatpys(request):
    return render(request, 'chatpys.html')


def meeting(request):
    return render(request, 'meeting.html')


def feedback(request):
    return render(request, 'feedback.html')

def articls(request):
    return render(request,'articls.html')
def parent_comment(request):
    return render(request, 'parent_comment.html')

def submit_profile(request):
    if request.method == 'POST':
        # טיפול בנתונים שנשלחו מהטופס
        parent_name = request.POST.get('parent_name')
        parent_email = request.POST.get('parent_email')
        parent_phone = request.POST.get('parent_phone')
        child_name = request.POST.get('child_name')
        child_age = request.POST.get('child_age')
        child_gender = request.POST.get('child_gender')
        challenges = request.POST.get('challenges')

        # עשוי להיות רצוי להוסיף לקוד זה לוגיקה נוספת לשמירת הנתונים במסד הנתונים או לעיבוד נוסף
        # במקרה זה אני מניח שהפונקציה תחזיר תגובה אוקסלית לבקשת ה-POST
        return HttpResponse("Profile submitted successfully!")

    else:
        return HttpResponseBadRequest("Bad request")
"""def submit_profile(request):
     return render(request, 'submit_profile.html')"""

"""def submit_profile(request):
    if request.method == 'POST':
        form = ParentProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile_detail')  # Redirect to profile detail page
    else:
        form = ParentProfileForm()
    return render(request, 'submit_profile.html', {'form': form})"""

def profile_detail(request):
    profiles = ParentProfile.objects.all()
    return render(request, 'profile_detail.html', {'profiles': profiles})


def feedback_submit(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('parhomepage')
    else:
        form = FeedbackForm()
    return render(request, 'feedbackl.html', {'form': form})

def thank_you(request):
    return render(request, 'thank_you.html')




def submit_comment(request):
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)  # השתמש בטופס שיצרת, אם קיים
        if comment_form.is_valid():
            comment_text = comment_form.cleaned_data['comment_text']
            Comment.objects.create(comment_text=comment_text)
            return redirect('thank_you')  # לדוגמה, דף שמציג הודעה על הצלחת השליחה
    else:
        comment_form = CommentForm()  # אם הבקשה היא GET, הצג את הטופס

    return render(request, 'comment_form.html', {'comment_form': comment_form})



from .forms import SummaryForm


def summary_workshop(request):
    if request.method == 'POST':
        form = SummaryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thank_you')  # redirect to success page after saving the summary
    else:
        form = SummaryForm()
    return render(request, 'workshopys.html', {'form': form})


# views.py

from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import SummaryForm


def submit_summary(request):
    if request.method == 'POST':
        form = SummaryForm(request.POST)
        if form.is_valid():
            summary_text = form.cleaned_data['summary']
            # כאן אתה יכול לעשות מה שברצונך עם הסיכום, לדוגמה, לשמור אותו במסד נתונים
            return HttpResponseRedirect('thank_you')  # או לדף אחר שתרצה
    else:
        form = SummaryForm()

    return render(request, 'workshop_form.html', {'form': form})




def add_comment(request):
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)  # השתמש בטופס שיצרת, אם קיים
        if comment_form.is_valid():
            comment_text = comment_form.cleaned_data['comment_text']
            Comment.objects.create(comment_text=comment_text)
            return redirect('thank_you')  # לדוגמה, דף שמציג הודעה על הצלחת השליחה
    else:
        comment_form = CommentForm()  # אם הבקשה היא GET, הצג את הטופס

    return render(request, 'add_comment.html', {'add_comment': comment_form})

def comment_success(request):
    return render(request, 'comment_success.html')
def add_comment(request):
    return render(request, 'add_comment.html')

def homepagefordoctors(request):
    return render(request, 'homepagefordoctors.html')



def add_data(request):
    if request.method == 'POST':
        form = BabyHealthForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_data')
    else:
        form = BabyHealthForm()
    return render(request, 'add_data.html', {'form': form})

def view_data(request):
    data_list = BabyHealth.objects.all()
    return render(request, 'view_data.html', {'data_list': data_list})

def feedbackl(request):
    return render(request, 'feedbackl.html')
def feedbackl(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('feedbackl')  # Redirect to the feedback page after submission
    else:
        form = FeedbackForm()

    feedbacks = Feedback.objects.all()
    return render(request, 'feedbackl.html', {'form': form, 'feedbacks': feedbacks})

def psyinfoboard(request):
    if request.method == 'POST':
        # If it's a POST request, handle adding an item
        content = request.POST.get('content')
        item = InformationBoard.objects.create(content=content)
        return JsonResponse({'item_id': item.id})
    else:
        # If it's a GET request, render the template with existing items
        items = InformationBoard.objects.all()
        return render(request, 'psyinfoboard.html', {'items': items})




def delete_item(request, item_id):
    if request.method == 'POST':
        item = InformationBoard.objects.get(id=item_id)
        item.delete()
        return JsonResponse({'success':True})


def get_information(request):
    # Retrieve all information items added by psychologists
    information_items = InformationBoard.objects.all()

    # Serialize the information items into JSON format
    data = [{'content': item.content} for item in information_items]

    # Return the serialized data as a JSON response
    return JsonResponse(data, safe=False)
def pedinfoboard(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        item = PediatricianInfoBoard.objects.create(content=content)
        return JsonResponse({'item_id': item.id})
    else:
        items = PediatricianInfoBoard.objects.all()
        return render(request, 'pedinfoboard.html', {'items': items})

def delete_ped_item(request, item_id):
    if request.method == 'POST':
        item = PediatricianInfoBoard.objects.get(id=item_id)
        item.delete()
        return JsonResponse({'success': True})

def get_ped_information(request):
    information_items = PediatricianInfoBoard.objects.all()
    data = [{'content': item.content} for item in information_items]
    return JsonResponse(data, safe=False)
def parboardpsy(request):
    return render(request, 'parboardpsy.html')
def parboardped(request):
    return render(request, 'parboardped.html')
def mwped(request):
    return render(request, 'mwped.html')
def vmwped(request):
    return render(request, 'vmwped.html')
def pedvmw(request):
    return render(request, 'pedvmw.html')
def meetped(request):
    return render(request, 'meetped.html')
def pedmeetv(request):
    return render(request, 'pedmeetv.html')
def vmeetped(request):
    return render(request, 'vmeetped.html')
def porall(request):
    return render(request, 'porall.html')