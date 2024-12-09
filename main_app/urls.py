from django.urls import path

from main_app import views, admin_views, workers_views, employers_views
from main_app.admin_views import accept, accept_view, feedback_view

urlpatterns = [
    path("",views.index,name="index"),
    path("dashboard",views.dashboard,name="dashboard"),

    path("WorkerR", views.WorkerR, name="WorkerR"),
    path("EmployerR", views.EmployerR, name="EmployerR"),
    path("login_view",views.Login_view,name="login_view"),




    #admin
    path("admin_base",admin_views.admin_base,name="admin_base"),
    path("worker_view", admin_views.worker_view, name="worker_view"),
    path("remove/<int:id>",admin_views.remove,name="remove"),
    path("update1/<int:id>",admin_views.update1,name="update1"),
    path("employer_view", admin_views.employer_view, name="employer_view"),
    path("remove2/<int:id>",admin_views.remove2,name="remove2"),
    path("update2/<int:id>",admin_views.update2,name="update2"),
    path("openings_view",admin_views.openings_view,name="openings_view"),
    path("req_view", admin_views.req_view, name="req_view"),
    path('accept/<int:id>/',admin_views.accept, name="accept"),
    path('reject/<int:id>/',admin_views.reject, name="reject"),
    path("accept_view",admin_views.accept_view,name="accept_view"),
    path("feedback_view",admin_views.feedback_view,name="feedback_view"),
    path("reply_feedback/<int:id>/",admin_views.reply_feedback,name="reply_feedback"),
    path("feedback_employer",admin_views.feedback_employer,name="feedback_employer"),
    path("reply_feed_emp/<int:id>/",admin_views.reply_feed_emp,name="reply_feed_emp"),
    path("logou",admin_views.logou, name="logou"),




    #workers
    path("workers_base",workers_views.workers_base, name="workers_base"),
    path("openings_list",workers_views.openings_list,name="openings_list"),
    path("worker_req", workers_views.worker_req, name="worker_req"),
    path("req_table",workers_views.req_table,name="req_table"),
    path('rmv/<int:id>/', workers_views.rmv, name="rmv"),
    path("feedbk",workers_views.feedbk,name="feedbk"),
    path("reply",workers_views.reply,name="reply"),
    path("profile_worker",workers_views.profile_worker,name="profile_worker"),
    path('profile_update/<int:id>/',workers_views.worker_update, name="profile_update"),
    path("logou",workers_views.logou, name="logou"),







    #employers
    path("employers_base",employers_views.employer_base, name="employers_base"),
    path("add_openings",employers_views.add_openings,name="add_openings"),
    path("view_openings",employers_views.view_openings,name="view_openings"),
    path('rmv/<int:id>/', employers_views.rmv, name="rmv"),
    path('update3/<int:id>/', employers_views.update3, name="update3"),
    path("view_req",employers_views.view_req,name="view_req"),
    path("accept_emp/<int:id>",employers_views.accept_emp, name="accept_emp"),
    path("feedbk_emp", employers_views.feedbk_emp, name="feedbk_emp"),
    path("reply_emp",employers_views.reply_emp,name="reply_emp"),
    path("profile_employer",employers_views.profile_employer,name="profile_employer"),
    path('employer_update/<int:id>/',employers_views.employer_update, name="employer_update"),
    path("logou", employers_views.logou, name="logou"),



]
