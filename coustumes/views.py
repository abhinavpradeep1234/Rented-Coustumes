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
from coustumes.forms import (
    RentedCostumeForm,
    BookingRentedCollectionForm,
    DressCodeForm,
)
from coustumes.models import RentedCostumes, BookingRentedCostumes, DressCode
from users.utils import create_notification
from users.models import CustomUser
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required


class RentedCostumeListView(LoginRequiredMixin, ListView):
    model = RentedCostumes
    context_object_name = "all_rented_costumes"
    template_name = "view_rented_costumes.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Rented Collections"
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


# filter wise collections
class TrendingListView(LoginRequiredMixin, ListView):
    model = RentedCostumes
    context_object_name = "all_rented_costumes"
    template_name = "trending_coustumes.html"

    def dispatch(self, request, *args, **kwargs):
        if request.user.role != "admin":
            return redirect("403")
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Trending Collections"
        context["all_rented_costumes"] = RentedCostumes.objects.filter(
            costume_categories="trending costumes"
        )
        return context


class CasualListView(LoginRequiredMixin, ListView):
    model = RentedCostumes
    context_object_name = "all_rented_costumes"
    template_name = "casual_coustumes.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Casual Collections"
        context["all_rented_costumes"] = RentedCostumes.objects.filter(
            costume_categories="casual costumes"
        )
        return context


class FormalListView(LoginRequiredMixin, ListView):
    model = RentedCostumes
    context_object_name = "all_rented_costumes"
    template_name = "formal_coustumes.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Formal Collections"
        context["all_rented_costumes"] = RentedCostumes.objects.filter(
            costume_categories="formal costumes"
        )
        return context


class DanceWearListView(LoginRequiredMixin, ListView):
    model = RentedCostumes
    context_object_name = "all_rented_costumes"
    template_name = "dance_costumes.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Dance Costume Collections"
        context["all_rented_costumes"] = RentedCostumes.objects.filter(
            costume_categories="dance costumes"
        )
        return context


class PartyWearListView(LoginRequiredMixin, ListView):
    model = RentedCostumes
    context_object_name = "all_rented_costumes"
    template_name = "trending_coustumes.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Party Wear Collections"
        context["all_rented_costumes"] = RentedCostumes.objects.filter(
            costume_categories="party wear"
        )
        return context


class SweaterCollectionListView(LoginRequiredMixin, ListView):
    model = RentedCostumes
    context_object_name = "all_rented_costumes"
    template_name = "sweater_collections.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Sweater Collections"
        context["all_rented_costumes"] = RentedCostumes.objects.filter(
            costume_categories="sweater"
        )
        return context


#
@login_required(login_url="signup")
def booking_rented_collections(request):
    # rented_costumes=get_object_or_404(RentedCostumes,id=pk)

    if request.method == "POST":

        form = BookingRentedCollectionForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.username = request.user
            booking.save()
            messages.success(
                request,
                "Booking SuccessFully delivery except 2 days",
                extra_tags="alert-success",
            )
            return redirect("dashboard")
        else:
            for error_list in form.errors.values():
                for errors in error_list:
                    messages.error(request, errors, extra_tags="alert-danger")

    context = {"form": BookingRentedCollectionForm, "page_title": "Book Now"}
    return render(request, "add_update.html", context)


# class BookingRentedCostumeUpdateView(LoginRequiredMixin,DeleteView):
#     model=


class BookingRentedCostumeDeleteView(DeleteView):
    def get(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        messages.success(
            self.request, "Deleted Successfully", extra_tags="alert-success"
        )
        return super().delete(request, *args, **kwargs)

#dress Code Crud
class DressCodeListView(LoginRequiredMixin, ListView):
    model = DressCode
    context_object_name = "all_dress"
    template_name = "view_dress_code.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = " Dress Code"
        return context


class DressCodeCreateView(LoginRequiredMixin, CreateView):
    model = DressCode
    success_url = reverse_lazy("dress_code")
    template_name = "add_update.html"

    form_class = DressCodeForm

    def dispatch(self, request, *args, **kwargs):
        if request.user.role != "admin":
            return redirect("403")

        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Add Dress Code"
        return context

    def form_valid(self, form):
        messages.success(
            self.request, "Dress code Added Successfully ", extra_tags="alert-success"
        )

        return super().form_valid(form)

    def form_invalid(self, form):
        for error_list in form.errors.values():
            for errors in error_list:
                messages.error(self.request, errors, extra_tags="alert-danger")
        return super().form_invalid(form)


class DressCodeUpdateView(LoginRequiredMixin, UpdateView):
    model = DressCode
    success_url = reverse_lazy("dress_code")
    template_name = "add_update.html"

    form_class = DressCodeForm

    def dispatch(self, request, *args, **kwargs):
        if request.user.role != "admin":
            return redirect("403")

        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Updated Dress Code"
        return context

    def form_valid(self, form):
        messages.success(
            self.request, "Dress code Updated Successfully ", extra_tags="alert-success"
        )

        return super().form_valid(form)

    def form_invalid(self, form):
        for error_list in form.errors.values():
            for errors in error_list:
                messages.error(self.request, errors, extra_tags="alert-danger")
        return super().form_invalid(form)


class DressCodeDeleteView(LoginRequiredMixin, DeleteView):
    model = DressCode
    success_url = reverse_lazy("dress_code")

    def dispatch(self, request, *args, **kwargs):
        if request.user.role != "admin":
            return redirect("403")

        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        messages.success(
            self.request, "Deleted Successfully", extra_tags="alert-success"
        )
        return super().delete(request, *args, **kwargs)
