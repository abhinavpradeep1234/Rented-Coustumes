from django.urls import path
from . import views

urlpatterns = [
    path("", views.SignupCreateView.as_view(), name="signup"),
    path("logout", views.user_logout, name="user_logout"),
    path("home/", views.HomeView.as_view(), name="home"),
    path("view/users", views.UsersListView.as_view(), name="view_users"),
    path("create/users", views.UsersCreateView.as_view(), name="create_users"),
    path("delete/users/<int:pk>", views.UsersDeleteView.as_view(), name="delete_users"),
    path("update/users/<int:pk>", views.UsersUpdateView.as_view(), name="update_users"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path(
        "dashboard/user", views.UserDashBoardListView.as_view(), name="user_dashboard"
    ),
    path(
        "dashboard/admin",
        views.AdminDashBoardListView.as_view(),
        name="admin_dashboard",
    ),
    # complaints for user
    path("view/complaints", views.ComplaintListView.as_view(), name="view_complaints"),
    path(
        "create/complaints",
        views.ComplaintCreateView.as_view(),
        name="create_complaints",
    ),
    path(
        "update/complaints/<int:pk>",
        views.ComplaintUpdateView.as_view(),
        name="update_complaints",
    ),
    path(
        "delete/complaints/<int:pk>",
        views.ComplaintDeleteView.as_view(),
        name="delete_complaints",
    ),
    # complaints admin
    path("all/complaints", views.AllComplaintListView.as_view(), name="all_complaints"),
    path(
        "respond/complaints/<int:pk>",
        views.RespondComplaintView.as_view(),
        name="respond_complaints",
    ),
    # notification
    path(
        "view/notification",
        views.AllNotificationView.as_view(),
        name="view_notification",
    ), 
    path(
        "notification/is_read/<int:pk>",
        views.is_read,
        name="is_read",
    ),
    # offers
    path(
        "view/offers",
        views.AllOffersView.as_view(),
        name="view_offers",
    ),
    path(
        "add/offers",
        views.AddOffersView.as_view(),
        name="add_offers",
    ),
    path(
        "delete/offers/<int:pk>",
        views.DeleteOffersView.as_view(),
        name="delete_offers",
    ),
    # profile
    path(
        "profile",
        views.ProfileView.as_view(),
        name="profile",
    ),
    path(
        "update/profile/<int:pk>",
        views.UpdateProfileView.as_view(),
        name="update_profile",
    ),
    path(
        "403",
        views.Unrestricted.as_view(),
        name="403",
    ),
]
