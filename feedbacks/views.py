# -*- coding: utf-8 -*-


from django.shortcuts import render
from models import Contact
from django import forms
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import FormView
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import mail_admins



#  creating forms
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        help_texts = {'name': u'Имя отправителя', 'subject': u'Тема письма', 'email': u'email отправителя'}
        fields = '__all__'

        #def save(self, request):


class ContactFormView(FormView):
    form_class = ContactForm
    template_name = 'feedbacks/contact_form.html'
    success_url = 'feedbacks:contact_form'

    def get_context_data(self, **kwargs):
        context = super(ContactFormView, self).get_context_data(**kwargs)
        context['page_title'] = u'Связаться с администратором сайта'
        return context

    '''
    def form_valid(self, form):
        name = self.request.POST.get('name', '')
        subject = self.request.POST.get('subject', '')
        message = self.request.POST.get('body', '')
        from_email = self.request.POST.get('email', '')
        send_mail(subject, message, from_email, ['admin@gmail.com'])
        return super(ContactFormView, self).form_valid(form)
    '''

    def form_valid(self, form):
        #form = super(ContactFormView, self).form_valid(form)
        name = self.request.POST.get('name', '')
        subject = self.request.POST.get('subject', '')
        message = self.request.POST.get('body', '')
        from_email = self.request.POST.get('email', '')
        if name and subject and message and from_email:
            mail_admins(subject, message, fail_silently=True)
            messages.success(self.request, 'Mail successfully send')
            return HttpResponseRedirect('#')
        else:
            return HttpResponse('Make sure all fields are entered and valid.')


'''
    def save(self, *args, **kwargs):
        response = super(ContactFormView, self).save(*args, **kwargs)  # Call the "real" save() method.
        if self.request.method == "POST":
            form = ContactFormView(self.request.POST)
            if form.is_valid():
                name = self.request.POST.get('name', '')
                subject = self.request.POST.get('subject', '')
                message = self.request.POST.get('body', '')
                from_email = self.request.POST.get('email', '')
                send_mail(subject, message, from_email, ['admin@gmail.com'])
                messages.success(self.request, "Message from %s was send" % name)
        return response
        '''