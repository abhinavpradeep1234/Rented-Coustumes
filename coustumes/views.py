from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.contrib import messages  # type: ignore
from django.contrib.auth.mixins import LoginRequiredMixin  # type: ignore
from coustumes.forms import RentedCostumeForm
from coustumes.models import RentedCostumes
from users.utils import create_notification
from users.models import CustomUser


class RentedCostumeListView(LoginRequiredMixin, ListView):
    model = RentedCostumes
    context_object_name = "all_rented_costumes"
    template_name = "view_rented_costumes.html"

    def dispatch(self, request, *args, **kwargs):
        if request.user.role != "admin":
            return redirect("403")
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Rented Costumes"
        return context


class RentedCostumeCreateView(LoginRequiredMixin, CreateView):
    model = RentedCostumes
    form_class = RentedCostumeForm
    template_name = "add_update.html"
    success_url = reverse_lazy("view_rented_costumes")

    def dispatch(self, request, *args, **kwargs):
        if request.user.role != "admin":
            return redirect("403")
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Add Rented Costumes"
        return context

    def form_valid(self, form):
        users = CustomUser.objects.all()
        for user in users:
            create_notification(user, "New Costumes Added check it now")
        messages.success(
            self.request, "Added Costumes Successfully", extra_tags="alert-success"
        )
        return super().form_valid(form)

    def form_invalid(self, form):
        for error_list in form.errors.values():
            for errors in error_list:
                messages.success(self.request, errors, extra_tags="alert-success")
        return super().form_invalid(form)


class RentedCostumeUpdateView(LoginRequiredMixin, UpdateView):
    model = RentedCostumes
    form_class = RentedCostumeForm
    template_name = "add_update.html"
    success_url = reverse_lazy("view_rented_costumes")

    def dispatch(self, request, *args, **kwargs):
        if request.user.role != "admin":
            return redirect("403")
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Update Rented Costumes"
        return context

    def form_valid(self, form):
        messages.success(
            self.request, "Updated Costumes Successfully", extra_tags="alert-success"
        )
        return super().form_valid(form)

    def form_invalid(self, form):
        for error_list in form.errors.values():
            for errors in error_list:
                messages.success(self.request, errors, extra_tags="alert-success")
        return super().form_invalid(form)


class RentedCostumeDeleteView(LoginRequiredMixin, DeleteView):
    model = RentedCostumes
    success_url = reverse_lazy("view_rented_costumes")

    def dispatch(self, request, *args, **kwargs):
        if request.user.role != "admin":
            return redirect("403")
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        messages.success(
            self.request, "Costumes Deleted Successfully", extra_tags="alert-success"
        )
        return super().delete(request, *args, **kwargs)
