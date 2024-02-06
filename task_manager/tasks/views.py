from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.views.generic import TemplateView , FormView ,ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.utils import timezone

from .models import Tasks, Photos
from .forms import CustomUserCreationForm, TaskForm, PhotoForm

# Create your views here.

class CustomLoginView(LoginView):
    template_name = 'login.html'
    form_class = AuthenticationForm

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)
    
    def form_valid(self, form):
        return super().form_valid(form)
    
    def form_invalid(self, form):
        print("Form is invalid. Errors:", form.errors)
        return self.render_to_response(self.get_context_data(form=form))
    


class CustomLogoutView(LogoutView):
    def dispatch(self, request):
        if request.user.is_authenticated:
            logout(request)
            return redirect('login')



class UserRegistrationView(FormView):
    template_name = 'registration.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        username = form.cleaned_data['username']
        password = form.cleaned_data['password1']
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return super().form_valid(form)



class HomeView(LoginRequiredMixin,ListView):
    model=Tasks
    context_object_name = 'tasks'
    template_name = 'home.html'
    login_url = 'login'

    def get_queryset(self):
        queryset = Tasks.objects.filter(user=self.request.user, complete=False)
        search_query = self.request.GET.get('q', None)
        if search_query:
            queryset = queryset.filter(title__icontains=search_query)
        filter_priority = self.request.GET.get('priority', None)
        if filter_priority:
            queryset = queryset.filter(priority=filter_priority)
        filter_createdDate = self.request.GET.get('created_date', None)
        if filter_createdDate:
            print("Timezone",timezone.now())
            print(filter_createdDate)
            filter_createdDate = timezone.make_aware(
                timezone.datetime.strptime(filter_createdDate, "%Y-%m-%d"),
                timezone.get_default_timezone()
            )
            queryset = queryset.filter(created_at__date=filter_createdDate)
        filter_dueDate = self.request.GET.get('due_date', None)
        print(filter_dueDate)
        if filter_dueDate:
            queryset = queryset.filter(due_date=filter_dueDate)
        return queryset
    


class CreateTaskView(LoginRequiredMixin,CreateView):
    model = Tasks
    form_class = TaskForm
    template_name = 'create.html'
    success_url = reverse_lazy('home')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)



class SingleTaskView(LoginRequiredMixin,DetailView):
    model = Tasks
    context_object_name = 'task'
    template_name = 'single_task.html'
    login_url = 'login'

    def post(self, request, *args, **kwargs):
        task = self.get_object()
        print(task)
        task.complete = not task.complete
        task.save()
        if task.complete:
            return redirect('home')
        else:
            return redirect('task-completed')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        task = self.get_object()
        photos = Photos.objects.filter(task=task)
        context['photos'] = photos
        return context



class CompletedTaskView(LoginRequiredMixin,ListView):
    model=Tasks
    context_object_name = 'tasks'
    template_name = 'home.html'
    login_url = 'login'

    def get_queryset(self):
        return Tasks.objects.filter(user=self.request.user, complete=True)
    


class UpdateTaskView(LoginRequiredMixin, UpdateView):
    model = Tasks
    form_class = TaskForm
    template_name = 'edit.html'
    login_url = 'login'

    def get_success_url(self):
        return self.request.GET.get('next', reverse_lazy('home'))



class DeleteTaskConfirmView(LoginRequiredMixin, DeleteView):
    model = Tasks
    context_object_name = 'task'
    template_name = 'delete.html'
    success_url = reverse_lazy('home')
    login_url = 'login'

    def get_success_url(self):
        if self.object.complete:
            return reverse_lazy('task-completed')
        else:
            return reverse_lazy('home')

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    


class PhotoCreateView(CreateView):
    model = Photos
    form_class = PhotoForm
    template_name = 'photo_upload.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        task_id = self.kwargs['pk']
        task = Tasks.objects.get(pk=task_id)
        form.instance.task = task
        return super().form_valid(form)
    
class PhotoView(DetailView):
    model = Photos
    context_object_name = 'photo'
    template_name = 'single_photo.html'
    success_url = reverse_lazy('home')

    






