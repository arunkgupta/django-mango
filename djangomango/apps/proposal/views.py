from django.contrib import messages
from django.views.generic import CreateView, TemplateView
from django.utils.translation import ugettext as _

from .forms import SubmitProposalForm
from .models import PENDING


class SubmitProposalView(CreateView):
    form_class = SubmitProposalForm
    template_name = 'proposal/submit.html'
    success_url = '/'

    def form_valid(self, form):
        form.instance.speaker = self.request.user
        form.instance.status = PENDING
        messages.info(self.request,
            _(u"Thank you, your proposal is now being reviewed."))
        return super(SubmitProposalView, self).form_valid(form)


class ScheduleProposalView(TemplateView):
    template_name = 'proposal/schedule.html'
