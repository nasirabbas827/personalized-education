from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm , PasswordChangeForm 
from django.contrib.auth import update_session_auth_hash
from .forms import userform
from django.contrib.auth import login, logout
from django.contrib import messages 
from .forms import userchangeform


def home(request):
    return render(request, 'dashboard.html')

def signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'signin.html', {'form': form})

def custom_logout(request):
    logout(request)
    return redirect('home')

def signup(request):
    if request.method == 'POST':
        form = userform(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = userform()
    return render(request, 'signup.html', {'form': form})




@login_required
def update_profile(request):
    if request.method == 'POST':
        form = userchangeform(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully.')  
    else:
        form = userchangeform(instance=request.user)
    
    return render(request, 'update_profile.html', {'form': form})

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Password changed successfully.')
            return redirect('change_password')
    else:
        form = PasswordChangeForm(request.user)
    
    return render(request, 'change_password.html', {'form': form})


from django.shortcuts import render
from .models import Quiz

# View to display available quizzes
def available_quizzes(request):
    quizzes = Quiz.objects.all()
    return render(request, 'available_quizzes.html', {'quizzes': quizzes})

# View to attempt a quiz
def attempt_quiz(request, quiz_id):
    quiz = Quiz.objects.get(pk=quiz_id)
    return render(request, 'attempt_quiz.html', {'quiz': quiz})
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Quiz, QuizQuestion

def submit_quiz(request, quiz_id):
    if request.method == 'POST':
        quiz = Quiz.objects.get(pk=quiz_id)
        questions = quiz.quizquestion_set.all()
        total_questions = questions.count()
        correct_answers = 0

        for question in questions:
            answer_key = f'answer_{question.id}'
            selected_answer = request.POST.get(answer_key)

            if selected_answer == question.correct_option:
                correct_answers += 1

        # Calculate the score
        score = (correct_answers / total_questions) * 100

        # You can save the user's score or perform any other actions here
        # For now, we'll just display the results

        return render(request, 'quiz_results.html', {
            'quiz': quiz,
            'total_questions': total_questions,
            'correct_answers': correct_answers,
            'score': score,
        })

    # Handle GET requests (accessing the submission URL without actually submitting the form)
    return redirect('home')  # Redirect to the home page or another appropriate page
