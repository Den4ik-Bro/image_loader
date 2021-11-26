from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import generic
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .forms import RegistrationUserForm, ImageLoadForm
from .models import Image
from .serializers import ImageSerializer

User = get_user_model()


class Home(generic.TemplateView):
    template_name = 'home.html'


class ImageLoadView(LoginRequiredMixin, generic.FormView):
    template_name = 'image_load.html'
    form_class = ImageLoadForm


class ImageCreateView(generic.CreateView):
    model = Image

    def post(self, request, *args, **kwargs):
        form = ImageLoadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('image_loader:home'))
        return redirect(reverse('image_loader:image_load'))


class RegistrationFormView(generic.FormView):
    template_name = 'register.html'
    form_class = RegistrationUserForm


class UserCreateView(generic.CreateView):
    model = User

    def post(self, request, *args, **kwargs):
        form = RegistrationUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            if form.cleaned_data['password_1'] == form.cleaned_data['password_2']:
                user.set_password(form.cleaned_data['password_1'])
                user.save()
                return redirect(reverse('image_loader:home'))
        return redirect(reverse('image_loader:home'))


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
