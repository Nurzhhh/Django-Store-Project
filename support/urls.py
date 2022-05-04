from django.urls import path
from .views import CreateForm, AdminSupportReader, AdminSendMassEmail

app_name = "contact"

urlpatterns = [
	path("", CreateForm.as_view()),
	path("admin/support/", AdminSupportReader.as_view()),
	path("admin/support/<int:year>/<int:month>/", AdminSupportReader.as_view()),
	# path("admin/mass_mail/", AdminSendMassEmail.as_view()),
]
