from django.views.generic.base import TemplateView

from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse_lazy

from django.contrib.auth.decorators import login_required

# Create your views here.




#--- TemplateView
class HomeView(TemplateView):
    template_name = '../templates/home.html'

class VaccineView(TemplateView):
    template_name = '../templates/vaccine/vaccine.html'


class HospitalView(TemplateView):
    template_name = '../templates/hospital/hospital_list.html'

class HospitalDetailView(TemplateView):
    template_name = '../templates/hospital/hospital_detail.html'

class HospitalNoticeView(TemplateView):
    template_name = '../templates/hospital/hospital_notice.html'

class HospitalReservationView(TemplateView):
    template_name = '../templates/hospital/hospital_reservation.html'

class DiaryView(TemplateView):
    template_name = '../templates/diary/diary.html'

class MedicalView(TemplateView):
    template_name = '../templates/medical/medical.html'
    # # --- User Creation
    # class UserCreateView(CreateView):
    #     template_name = 'registration/register.html'
    #     form_class = UserCreationForm
    #     success_url = reverse_lazy('register_done')

    # class UserCreateDoneTV(TemplateView):
    #     template_name = 'registration/register_done.html'

    # # --- @login_required
    # class LoginRequiredMixin(object):
    #     @classmethod
    #     def as_view(cls, **initkwargs):
    #         view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
    #         return login_required(view)


#--- @login_required
class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)