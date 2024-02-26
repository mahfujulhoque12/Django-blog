from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("news/", views.news, name="news"),
    path("research/", views.research, name="research"),
    path('research/<str:research_id>/', views.research_content_details, name='show_research_content'),
    path("contact/", views.contact, name="contact"),
    path("more_info/<str:news_id>/", views.more_info, name="more_info"),
    path("company/", views.company, name="company"),
    path("customers/", views.customers , name="customers"),
    path("partner/", views.partner, name="partner"),
    path("eda/", views.eda, name="eda"),
    path("jm/", views.jm, name="jm"),
    path("databases/", views.databases, name="databases"),
    path("database_details/<str:database_id>/", views.database_details, name="database_details"),
    path("meterial/", views.meterial, name="meterial"),
    path("implement/", views.implement, name="implement"),
    path("home_details/<str:home_id>/", views.home_details, name="home_details"),
    path("stahldat/", views.stahldat, name="stahldat"),
    path("aluselect/", views.aluselect, name="aluselect"),
    path("jm_pro/", views.for_jm_pro, name="for_jm_pro"),
    path("eda_details/<str:eda_id>/", views.eda_details, name="eda_details"),
    path("jm_details/", views.jm_details, name="jm_details"),
    path("imprint/", views.imprint, name="imprint"),
    path("privacy/", views.privacy, name="privacy"),
    path("cookies/", views.cookies, name="cookies"),
    path("notice/", views.notice, name="notice"),
    path("terms/", views.terms, name="terms"),
    path("search/", views.search, name="search"),
]
