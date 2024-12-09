from django.urls import path  # type:ignore
from . import views

urlpatterns = [
    # this url for rented collection main page all collections
    path(
        "rented/view/",
        views.RentedCostumeListView.as_view(),
        name="view_rented_costumes",
    ),
    # CRUD rented coustumes
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
    # filter list only show the trending collections
    path(
        "list/trending/",
        views.TrendingListView.as_view(),
        name="view_trending_item",
    ),
    # filter list only show the Casual collections
    path(
        "list/casuals/",
        views.CasualListView.as_view(),
        name="view_casual_item",
    ),
    # filter list only show the formal collections
    path(
        "list/formals/",
        views.FormalListView.as_view(),
        name="view_formal_item",
    ),
    # filter list only show the dance collections
    path(
        "list/dance_wear/",
        views.DanceWearListView.as_view(),
        name="view_dance_item",
    ),
    # filter list only show the party wear collections
    path(
        "list/party_wear/",
        views.PartyWearListView.as_view(),
        name="view_party_wear",
    ),
    # filter list only show the Sweater collections
    path(
        "list/sweater_collection/",
        views.SweaterCollectionListView.as_view(),
        name="view_sweater",
    ),
]
