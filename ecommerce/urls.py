from django.urls import path
from django.conf.urls import handler404
from ecommerce import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about", views.about, name="about"),
    # path('<path:unknown_url>', views.handler404),
    # path("page/<int:id>", views.page_render, name="page"),
]

# handler404 = views.handler404