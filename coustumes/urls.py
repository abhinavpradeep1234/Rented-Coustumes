from django.urls import path  # type:ignore
from . import views

urlpatterns = [
    # CRUD rented coustumes
    path(
        "rented/view/",
        views.RentedCostumeListView.as_view(),
        name="view_rented_costumes",
    ),
    path(
        "rented/create/",
        views.RentedCostumeCreateView.as_view(),
        name="create_rented_costumes",
    ),
    path(
        "rented/updated/<int:pk>",
        views.RentedCostumeUpdateView.as_view(),
        name="update_rented_costumes",
    ),
    path(
        "rented/delete/<int:pk>",
        views.RentedCostumeDeleteView.as_view(),
        name="delete_rented_costumes",
    ),
]
