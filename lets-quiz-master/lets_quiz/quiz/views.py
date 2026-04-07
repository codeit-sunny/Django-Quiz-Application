from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from .models import QuizProfile, Question, AttemptedQuestion
from .forms import UserLoginForm, RegistrationForm


def home(request):
    return render(request, 'quiz/home.html')


@login_required
def user_home(request):
    return render(request, 'quiz/user_home.html')


def leaderboard(request):
    top_quiz_profiles = QuizProfile.objects.order_by('-total_score')[:500]
    total_count = top_quiz_profiles.count()

    context = {
        'top_quiz_profiles': top_quiz_profiles,
        'total_count': total_count,
    }
    return render(request, 'quiz/leaderboard.html', context)


@login_required
def play(request):
    quiz_profile, created = QuizProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        question_pk = request.POST.get('question_pk')
        attempted_question = quiz_profile.attempts.select_related('question').get(question__pk=question_pk)

        choice_pk = request.POST.get('choice_pk')

        try:
            selected_choice = attempted_question.question.choices.get(pk=choice_pk)
        except ObjectDoesNotExist:
            raise Http404("Choice does not exist")  # ✅ Added error message

        quiz_profile.evaluate_attempt(attempted_question, selected_choice)
        
        # ✅ FIXED: Use get_absolute_url() method from model
        return redirect(attempted_question.get_absolute_url())

    else:
        question = quiz_profile.get_new_question()
        if question is not None:
            quiz_profile.create_attempt(question)

        return render(request, 'quiz/play.html', {'question': question})


@login_required
def submission_result(request, attempted_question_pk):
    attempted_question = get_object_or_404(AttemptedQuestion, pk=attempted_question_pk)

    return render(request, 'quiz/submission_result.html', {
        'attempted_question': attempted_question,
    })


def login_view(request):
    form = UserLoginForm(request.POST or None)

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username=username, password=password)
        if user is not None:  # ✅ Added safety check
            login(request, user)
            return redirect('/user-home')
        else:
            # ✅ Added error handling for authentication failure
            form.add_error(None, "Invalid username or password")

    return render(request, 'quiz/login.html', {"form": form})


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')
    else:
        form = RegistrationForm()

    return render(request, 'quiz/registration.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('/')


def error_404(request, exception):
    return render(request, 'error_404.html', status=404)  # ✅ Added status code


def error_500(request):
    return render(request, 'error_500.html', status=500)  # ✅ Added status code