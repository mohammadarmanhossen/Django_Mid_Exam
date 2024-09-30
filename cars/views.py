from django.shortcuts import redirect
from cars.models import Car
from . import forms
from . import models
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView


@login_required
def buy_car(request, id):
    car = Car.objects.get(id=id)
    if car.quantity > 0:
        car.purchased = True
        car.owner = request.user
        car.quantity -= 1
        car.save()
        return redirect('profile')
    else:
        return redirect('car_details', id=id)


class DetailCarView(DetailView):
    model = models.Car
    pk_url_kwarg = 'id'
    template_name = 'car_details.html'

    def post(self, request, *args, **kwargs):
        car = self.get_object()
        comment_form = forms.CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.car = car
            new_comment.save()
            return redirect('car_details', id=car.id)
        return self.get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        car = self.object
        comments = car.comments.all()
        comment_form = forms.CommentForm()
        context['comments'] = comments
        context['comment_form'] = comment_form
        return context

