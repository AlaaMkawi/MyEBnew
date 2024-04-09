from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from django.contrib.auth.forms import UserCreationForm
from .forms import CreatUserForm
from .forms import ParentSignupForm, CreatUserForm
from django.contrib.auth import logout
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
from .forms import *
from .forms import Paropinionform
from .models import Paropinion
from .forms import MeetingForm
from django.contrib.auth.decorators import login_required
from .models import Meeting



def loginpsychologist(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            users_in_group = Group.objects.get(name='Psychologist').user_set.all()
            if user in users_in_group:
                login(request, user)
                return redirect('psychomepage')
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
            return redirect('parhomepage')
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
def sorall(request):
    return render(request, 'sorall.html')
#alaa


def parpedhomepage(request):
    return render(request, 'par.ped.homepage.html')
def add_extra_informationpeda(request):
    if request.method == 'POST':
        form = ExtraInfoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('extrainfopeda')
    else:
        form = ExtraInfoForm()
    return render(request, 'add_extra_informationa.html', {'form': form})
def add_extra_informationpsya(request):
    if request.method == 'POST':
        form = ExtraInfoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('extrainfopsya')
    else:
        form = ExtraInfoForm()
    return render(request, 'add_extra_informationa_psy.html', {'form': form})


def view_extra_informationpara(request):
    extra_info = ExtraInfo.objects.all()
    return render(request, 'extrainfopara.html', {'extra_info': extra_info})
def view_extra_informationpeda(request):
    extra_info = ExtraInfo.objects.all()
    return render(request, 'extrainfopeda.html', {'extra_info': extra_info})
def view_extra_informationpsya(request):
    extra_info = ExtraInfo.objects.all()
    return render(request, 'extrainfopsya.html', {'extra_info': extra_info})

def delete_(request):
    if request.method == 'POST':
        if 'check_details' in request.POST:
            username = request.POST.get('username')
            password = request.POST.get('password')
            email = request.POST.get('email')
            user = authenticate(request, username=username, password=password)
            if user is not None and user.email == email:
                # Save the user object in the session
                request.session['user'] = {'username': user.username, 'email': user.email}
                # Display confirmation message
                messages.info(request, 'Are you sure you want to delete your account?')
                return redirect('delete_confirm')
            else:
                messages.error(request, 'Invalid username, password, or email.')
        return render(request, 'delete_.html')
    else:
        return render(request, 'delete_.html')
def delete_ped(request):
    if request.method == 'POST':
        if 'check_details' in request.POST:
            username = request.POST.get('username')
            password = request.POST.get('password')
            email = request.POST.get('email')
            user = authenticate(request, username=username, password=password)
            if user is not None and user.email == email:
                # Save the user object in the session
                request.session['user'] = {'username': user.username, 'email': user.email}
                # Display confirmation message
                messages.info(request, 'Are you sure you want to delete your account?')
                return redirect('delete_confirm_ped')
            else:
                messages.error(request, 'Invalid username, password, or email.')
        return render(request, 'delete_ped.html')
    else:
        return render(request, 'delete_ped.html')
def delete_psy(request):
    if request.method == 'POST':
        if 'check_details' in request.POST:
            username = request.POST.get('username')
            password = request.POST.get('password')
            email = request.POST.get('email')
            user = authenticate(request, username=username, password=password)
            if user is not None and user.email == email:
                # Save the user object in the session
                request.session['user'] = {'username': user.username, 'email': user.email}
                # Display confirmation message
                messages.info(request, 'Are you sure you want to delete your account?')
                return redirect('delete_confirm_psy')
            else:
                messages.error(request, 'Invalid username, password, or email.')
        return render(request, 'delete_psy.html')
    else:
        return render(request, 'delete_psy.html')

def delete_confirm(request):
    if request.method == 'POST':
        if 'confirm' in request.POST:
            # Delete user account
            user = User.objects.get(username=request.session['user']['username'])
            user.delete()
            # Clear the user object from the session
            del request.session['user']
            messages.success(request, 'Your account has been deleted successfully.')
            return redirect('homepage')
        elif 'cancel' in request.POST:
            # Clear the user object from the session
            del request.session['user']
            return redirect('delete_')
    elif 'user' in request.session:
        # Display confirmation message
        return render(request, 'delete_confirm.html')
    else:
        messages.error(request, 'Invalid request.')
        return redirect('homepage')

def delete_confirm_ped(request):
    if request.method == 'POST':
        if 'confirm' in request.POST:
            # Delete user account
            user = User.objects.get(username=request.session['user']['username'])
            user.delete()
            # Clear the user object from the session
            del request.session['user']
            messages.success(request, 'Your account has been deleted successfully.')
            return redirect('homepage')
        elif 'cancel' in request.POST:
            # Clear the user object from the session
            del request.session['user']
            return redirect('delete_ped')
    elif 'user' in request.session:
        # Display confirmation message
        return render(request, 'delete_confirm_ped.html')
    else:
        messages.error(request, 'Invalid request.')
        return redirect('homepage')
def delete_confirm_psy(request):
    if request.method == 'POST':
        if 'confirm' in request.POST:
            # Delete user account
            user = User.objects.get(username=request.session['user']['username'])
            user.delete()
            # Clear the user object from the session
            del request.session['user']
            messages.success(request, 'Your account has been deleted successfully.')
            return redirect('homepage')
        elif 'cancel' in request.POST:
            # Clear the user object from the session
            del request.session['user']
            return redirect('delete_psy')
    elif 'user' in request.session:
        # Display confirmation message
        return render(request, 'delete_confirm_psy.html')
    else:
        messages.error(request, 'Invalid request.')
        return redirect('homepage')

def track(request):
    tracks = Track.objects.all()
    return render(request, 'tracka.html', {'tracks':tracks})

def track_next(request, pk):
    if request.user.is_authenticated:
       # Look Up Records
       track_next = Track.objects.get(id=pk)
       return render(request, 'track2.html', {'track_next':track_next})
    else:
       return redirect('tracka')

def track_delete(request, pk):
    if request.user.is_authenticated:
       delete_it = Track.objects.get(id=pk)
       delete_it.delete()
       return redirect('tracka')
    else:
       return redirect('tracka')

def track_add(request):
	form = AddTrackForm(request.POST or None)
	if request.user.is_authenticated:
		if request.method == "POST":
			if form.is_valid():
				add_record = form.save()
				return redirect('tracka')
		return render(request, 'track_add.html', {'form':form})
	else:
		return redirect('tracka')

def track_edit(request, pk):
    if request.user.is_authenticated:
       current_record = Track.objects.get(id=pk)
       form = AddTrackForm(request.POST or None, instance=current_record)
       if form.is_valid():
          form.save()
          return redirect('tracka')
       return render(request, 'track_edit.html', {'form':form})
    else:
       return redirect('tracka')
def porall(request):
    return render(request, 'porall.html')
def parop(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        item =Paropinion.objects.create(content=content)
        return JsonResponse({'item_id': item.id})
    else:
        items = Paropinion.objects.all()
        return render(request, 'parop.html', {'items': items})

def delete_parop_item(request, item_id):
    if request.method == 'POST':
        item = Paropinion.objects.get(id=item_id)
        item.delete()
        return JsonResponse({'success': True})

def get_parop_information(request):
    information_items = Paropinion.objects.all()
    data = [{'content': item.content} for item in information_items]
    return JsonResponse(data, safe=False)



def parent_profView(request, parent_id):
    parent = Parent.objects.get(phone=parent_id)
    return render(request, 'parent_profView.html', {'parent': parent})


def pediatrician_profView(request,pediatrician_id):
   # pediatrician = Pediatrician.objects.first()
   pediatrician = Pediatrician.objects.get(id=pediatrician_id)
   logged_in_pediatrician = Pediatrician.objects.get(user=request.user)

   context = {
       'pediatrician': logged_in_pediatrician
   }

  # return render(request, 'pediatrician_profile.html', context)
   return render(request, 'pediatrician_profView.html', {'pediatrician': pediatrician},context)

def psychologist_profiView(request):
    psychologist = Psychologist.objects.first()
    return render(request, 'psychologist_profView.html', {'psychologist': psychologist})

def create_workshop(request):
    if request.method == 'POST':
        form = WorkshopForm(request.POST)
        if form.is_valid():
            form.save()
            # Set workshop_added to True after successfully adding workshop
            workshop_added = True
            return render(request, 'create_workshop.html', {'form': form, 'workshop_added': workshop_added})
    else:
        form = WorkshopForm()
    return render(request, 'create_workshop.html', {'form': form})

def workshops(request):
    workshops = Workshop.objects.all()
    return render(request, 'workshop.html', {'workshops': workshops})


@login_required
def Parent_profile(request):
   # profile = request.user.profile
    return render(request, 'Parent_profile.html')

@login_required
def Parent_editProfile(request):
       return render(request, 'Parent_editProfile.html')



@login_required
def Ped_profile(request):
    #profile = request.user.profile
    return render(request, 'Ped_profile.html')

@login_required
def Ped_editProfile(request):
        return render(request, 'Ped_editProfile.html')

@login_required
def Psy_profile(request):
    #profile = request.user.profile
    return render(request, 'Psy_profile.html')

@login_required
def Psy_editProfile(request):
     return render(request, 'Psy_editProfile.html')


def meeting_board(request):
    meetings = Meeting.objects.all()
    return render(request, 'meeting_board.html')



def psychologist_onParentSide(request):
    return render(request, 'psychologist_onParentSide.html')




def add_data_psy(request):
    if request.method == 'POST':
        form = BabyHealthForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_data')
    else:
        form = BabyHealthForm()
    return render(request, 'add_data_psy.html', {'form': form})
def add_data_ped(request):
    if request.method == 'POST':
        form = BabyHealthForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_data')
    else:
        form = BabyHealthForm()
    return render(request, 'add_data_ped.html', {'form': form})
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

def view_data_psy(request):
    data_list = BabyHealth.objects.all()
    return render(request, 'view_data_psy.html', {'data_list': data_list})

def view_data_ped(request):
    data_list = BabyHealth.objects.all()
    return render(request, 'view_data_ped.html', {'data_list': data_list})


def content(request):
    return render(request, 'content.html')

def read(request):
    return render(request, 'read.html')