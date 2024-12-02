from django.shortcuts import redirect, render
from django.contrib.auth import logout

# from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from users.models import CustomUser, Complaints, Notification
from django.views.generic import (
    ListView,
    CreateView,
    TemplateView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from users.forms import (
    SignupForm,
    UserCreateForm,
    UserUpdateForm,
    ComplaintForm,
    RespondComplaintForm,
)
from users.utils import create_notification


class SignupCreateView(CreateView):
    template_name = "registration/signup.html"
    model = CustomUser
    success_url = reverse_lazy("login")
    form_class = SignupForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Signup"
        return context

    def form_valid(self, form):
        messages.success(
            self.request,
            "Your Account Created SuccessFully",
            extra_tags="alert-success",
        )
        return super().form_valid(form)

    def form_invalid(self, form):
        for error_list in form.errors.items():
            for error in error_list:
                messages.error(self.request, error, extra_tags="alert-danger")

        return super().form_invalid(form)


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "home.html"

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            create_notification(request.user, "welcomeeee")
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Home"
        return context


class UsersListView(LoginRequiredMixin, ListView):
    model = CustomUser
    template_name = "view_users.html"
    context_object_name = "all_users"
    # def dispatch(self, request, *args, **kwargs):
    #     if
    #     return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "All Logged Users"
        return context


class UsersCreateView(LoginRequiredMixin, CreateView):
    model = CustomUser
    template_name = "add_update.html"
    form_class = UserCreateForm
    success_url = reverse_lazy("view_users")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Create User"
        return context

    def form_valid(self, form):
        messages.success(
            self.request,
            "User Created Successfully",
            extra_tags="alert-success",
        )
        return super().form_valid(form)

    def form_invalid(self, form):
        for error_list in form.errors.items():
            for error in error_list:
                messages.error(self.request, error, extra_tags="alert-danger")

        return super().form_invalid(form)


def user_logout(request):
    logout(request)
    messages.add_message(
        request,
        messages.SUCCESS,
        "You have been logged out!",
        extra_tags="alert-success",
    )
    return redirect("user_logout")


class UsersUpdateView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    template_name = "add_update.html"
    form_class = UserUpdateForm
    success_url = reverse_lazy("view_users")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Update User"
        return context

    def form_valid(self, form):
        messages.success(
            self.request,
            "User Created Successfully",
            extra_tags="alert-success",
        )
        return super().form_valid(form)

    def form_invalid(self, form):
        for error_list in form.errors.items():
            for error in error_list:
                messages.error(self.request, error, extra_tags="alert-danger")

        return super().form_invalid(form)


class UsersDeleteView(LoginRequiredMixin, DeleteView):
    model = CustomUser
    success_url = reverse_lazy("view_users")

    def get(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        messages.success(
            self.request,
            "User Deleted Successfully",
            extra_tags="alert-success",
        )
        return super().delete(request, *args, **kwargs)


def dashboard(request):
    if request.user.role == "admin":
        return redirect("admin_dashboard")
    elif request.user:
        return redirect("user_dashboard")


class UserDashBoardListView(LoginRequiredMixin, ListView):
    model = CustomUser
    template_name = "users_dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "User DashBoard"
        return context


class AdminDashBoardListView(LoginRequiredMixin, ListView):
    model = Complaints
    template_name = "admin_dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Admin DashBoard"
        context["all_complaints"] = Complaints.objects.all()

        return context


# complaints
class ComplaintListView(LoginRequiredMixin, ListView):
    model = Complaints
    template_name = "view_complaints.html"
    context_object_name = "all_complaintss"  # Set the context object name

    def get_queryset(self):
        return Complaints.objects.filter(username=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "View Complaints"
        print("All Complaints:", context["all_complaintss"])  # Debug print

        return context


class ComplaintCreateView(LoginRequiredMixin, CreateView):
    model = Complaints
    template_name = "add_update.html"
    form_class = ComplaintForm
    success_url = reverse_lazy("view_complaints")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Create Complaint"
        return context

    def form_valid(self, form):
        complaint = form.save(commit=False)
        complaint.username = self.request.user
        complaint.save()
        messages.success(
            self.request, "Complaint Register Successfully", extra_tags="alert-success"
        )
        return super().form_valid(form)

    def form_invalid(self, form):
        for error_list in form.errors.values():
            for errors in error_list:
                messages.error(self.request, errors, extra_tags="alert-danger")

        return super().form_invalid(form)


class ComplaintUpdateView(LoginRequiredMixin, UpdateView):
    model = Complaints
    template_name = "add_update.html"
    form_class = ComplaintForm
    success_url = reverse_lazy("view_complaints")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Update Complaint"
        return context

    def form_valid(self, form):
        messages.success(
            self.request, "Complaint Register Successfully", extra_tags="alert-success"
        )
        return super().form_valid(form)

    def form_invalid(self, form):
        for error_list in form.errors.values():
            for errors in error_list:
                messages.error(self.request, errors, extra_tags="alert-danger")

        return super().form_invalid(form)


class ComplaintDeleteView(DeleteView):
    model = Complaints
    success_url = reverse_lazy("view_complaints")

    def get(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        messages.success(
            self.request, "Complaint Deleted Successfully", extra_tags="alert-success"
        )
        return super().delete(request, *args, **kwargs)


# Admin View complaint


class AllComplaintListView(LoginRequiredMixin, ListView):
    model = Complaints
    template_name = "all_complaints.html"
    context_object_name = "all_complaints"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "All Complaints"
        return context


# complaint respond


class RespondComplaintView(LoginRequiredMixin, UpdateView):
    model = Complaints
    template_name = "add_update.html"
    form_class = RespondComplaintForm
    success_url = reverse_lazy("all_complaints")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Respond Complaint"
        return context

    def form_valid(self, form):
        messages.success(
            self.request, "Response Created Successfully", extra_tags="alert-success"
        )
        return super().form_valid(form)

    def form_invalid(self, form):
        for error_list in form.errors.values():
            for errors in error_list:
                messages.error(self.request, errors, extra_tags="alert-danger")

        return super().form_invalid(form)


class AllNotificationView(ListView):
    model = Notification
    template_name = "view_notification.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "View Notification"
        context["all_notification"] = Notification.objects.filter(
            username=self.request.user
        )
        return context


