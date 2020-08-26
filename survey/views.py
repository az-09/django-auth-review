import json

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import redirect, render, reverse
from django.views import View

from .models import Survey, Question, Choice, SurveyAssignment


class RegisterView(View):
    def get(self, request):
        return render(request, 'survey/register.html', { 'form': UserCreationForm() })

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect(reverse('login'))

        return render(request, 'survey/register.html', { 'form': form })


class ProfileView(LoginRequiredMixin, View):
    def get(self, request):
        surveys = Survey.objects.filter(created_by=request.user).all()
        assigned_surveys = SurveyAssignment.objects.filter(assigned_to=request.user).all()
        # survey_results = get_objects_for_user(request.user, 'can_view_results', klass=Survey)

        context = {
          'surveys': surveys,
          'assgined_surveys': assigned_surveys,
        #   'survey_results': survey_results
        }

        return render(request, 'survey/profile.html', context)

class SurveyCreateView(LoginRequiredMixin, View):
    def get(self, request):
        users = User.objects.all()
        return render(request, 'survey/create_survey.html', {'users': users})

    def post(self, request):
        data = request.POST
        title = data.get('title')
        questions_json = data.getlist('questions')
        assignees = data.getlist('assignees')
        valid = True
        context = {}
        if not title:
            valid = False
            context['title_error'] = 'title is required'

        if not questions_json:
            valid= False
            context['questions_error'] = 'questions are required'

        if not assignees:
            valid = False
            context['assignees_error'] = 'assignees are required'

        if not valid:
            context['users'] = User.objects.all()
            return render(request, 'survey/create_survey.html', context)

        survey = Survey.objects.create(title=title, created_by=request.user)
        for question_json in questions_json:
            question_data = json.loads(question_json)
            question = Question.objects.create(text=question_data['text'], survey=survey)
            for choice_data in question_data['choices']:
                Choice.objects.create(text=choice_data['text'], question=question)

        for assignee in assignees:
            assigned_to = User.objects.get(pk=int(assignee))
            SurveyAssignment.objects.create(
                survey=survey,
                assigned_by=request.user,
                assigned_to=assigned_to
            )
        
        return redirect(reverse('profile'))
