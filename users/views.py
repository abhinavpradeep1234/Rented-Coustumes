from django.shortcuts import redirect
from django.contrib.auth import logout
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from users.models import CustomUser, Complaints, Notification, Offers
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
    OffersForm,
    ProfileForm,
)
from users.utils import create_notification

from coustumes.models import BookingRentedCostumes
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
        for error_list in form.errors.values():
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
    paginate_by = 6
    ordering = ["-id"]

    def dispatch(self, request, *args, **kwargs):
        if request.user.role != "admin":
            return redirect("403")
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "All Logged Users"
        return context


class UsersCreateView(LoginRequiredMixin, CreateView):
    model = CustomUser
    template_name = "add_update.html"
    form_class = UserCreateForm
    success_url = reverse_lazy("view_users")

    def dispatch(self, request, *args, **kwargs):
        if request.user.role != "admin":
            return redirect("403")
        return super().dispatch(request, *args, **kwargs)

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
    return redirect("signup")


class UsersUpdateView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    template_name = "add_update.html"
    form_class = UserUpdateForm
    success_url = reverse_lazy("view_users")

    def dispatch(self, request, *args, **kwargs):
        if request.user.role != "admin":
            return redirect("403")
        return super().dispatch(request, *args, **kwargs)

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

    def dispatch(self, request, *args, **kwargs):
        if request.user.role != "admin":
            return redirect("403")
        return super().dispatch(request, *args, **kwargs)

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
    model = BookingRentedCostumes
    template_name = "users_dashboard.html"
    context_object_name = "all_bookings"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "User DashBoard"
        context["all_bookings"] = BookingRentedCostumes.objects.filter(username=self.request.user)
        return context


class AdminDashBoardListView(LoginRequiredMixin, ListView):
    model = Complaints
    template_name = "admin_dashboard.html"

    def dispatch(self, request, *args, **kwargs):
        if request.user.role != "admin":
            return redirect("403")
        return super().dispatch(request, *args, **kwargs)

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
    paginate_by = 6
    ordering = ["-id"]

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
        admins = CustomUser.objects.filter(role="admin")
        for admin in admins:
            create_notification(
                admin, f"user {self.request.user} registered complaint check it now"
            )

        create_notification(self.request.user, "Registerd Complaints Successfully")
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
    paginate_by = 6
    ordering = ["-id"]

    def dispatch(self, request, *args, **kwargs):
        if request.user.role != "admin":
            return redirect("403")
        return super().dispatch(request, *args, **kwargs)

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

    def dispatch(self, request, *args, **kwargs):
        if request.user.role != "admin":
            return redirect("403")
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Respond Complaint"
        return context

    def form_valid(self, form):
        messages.success(
            self.request, "Response Created Successfully", extra_tags="alert-success"
        )
        admins = CustomUser.objects.filter(role="admin")
        for admin in admins:
            create_notification(admin, "Authority respond complaint check it now")

        return super().form_valid(form)

    def form_invalid(self, form):
        for error_list in form.errors.values():
            for errors in error_list:
                messages.error(self.request, errors, extra_tags="alert-danger")

        return super().form_invalid(form)


class AllNotificationView(LoginRequiredMixin, ListView):
    model = Notification
    template_name = "view_notification.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "View Notification"
        context["all_notification"] = Notification.objects.filter(
            username=self.request.user
        ).order_by("-id")
        return context


@login_required(login_url="signup")
def is_read(request, pk):
    to_read = get_object_or_404(Notification, id=pk)
    to_read.is_read = True
    to_read.save()
    return redirect("view_notification")


# offers
class AllOffersView(LoginRequiredMixin, ListView):
    model = Offers
    template_name = "add_view_offers.html"
    context_object_name = "all_offers"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "View Offers"

        return context


class AddOffersView(LoginRequiredMixin, CreateView):
    model = Offers
    template_name = "add_update.html"
    form_class = OffersForm
    success_url = reverse_lazy("view_offers")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Add Offers"

        return context

    def form_valid(self, form):
        messages.success(
            self.request, "Offers Added Successfully", extra_tags="alert-success"
        )
        users = CustomUser.objects.all()
        for user in users:
            create_notification(user, "New Exclusive Offers Added Check it now !!")

        return super().form_valid(form)

    def form_invalid(self, form):
        for error_list in form.errors.values():
            for errors in error_list:
                messages.error(self.request, errors, extra_tags="alert-danger")
        return super().form_invalid(form)


class DeleteOffersView(DeleteView):
    model = Offers
    success_url = reverse_lazy("view_offers")

    def get(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        messages.success(
            self.request, "Offers Deleted Successfully", extra_tags="alert-danger"
        )

        return super().delete(request, *args, **kwargs)


# profile
class ProfileView(LoginRequiredMixin, ListView):
    model = CustomUser
    template_name = "profile.html"
    context_object_name = "all_user"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Profile"

        return context


class UpdateProfileView(UpdateView):
    model = CustomUser
    template_name = "add_update.html"
    form_class = ProfileForm
    success_url = reverse_lazy("profile")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Update Profile"

        return context

    def form_valid(self, form):
        messages.success(
            self.request, "Profile Updated Successfully", extra_tags="alert-success"
        )

        return super().form_valid(form)

    def form_invalid(self, form):
        for error_list in form.errors.values():
            for errors in error_list:
                messages.error(self.request, errors, extra_tags="alert-danger")
        return super().form_invalid(form)


class Unrestricted(TemplateView):
    template_name = "403.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "403"

        return context
