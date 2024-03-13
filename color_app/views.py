from django.shortcuts import render
from color_app.models import Color
from random import randint
from django.views.generic import DetailView, ListView, CreateView
from django.urls import reverse_lazy
from color_app.models import Color
from color_app.forms import ColorForm
from django.conf import settings

#######################
# Function Based Views
#######################


def home_view(request):
    "A view function which renders the homepage"

    skyblue = Color(name="red", red=207, green=2, blue=10)

    params = {
        "name": "Cayden",
        "color": skyblue,
    }
    
    response = render(request, 'color_app/index.html', params)
    return response

def random_color_view(request):
    "A view function which renders a random color"

    random_color = Color(
        name="random color", 
        red=randint(0, 256), 
        green=randint(0, 256),
        blue=randint(0, 256)
    )

    params = {"color": random_color}

    return render(request, 'color_app/random_color.html', params)

#######################
# Class Based Views
#######################

class ColorListView(ListView):
    model = Color
    template_name = "color_app/color_list.html"
    queryset = Color.objects.order_by("red")

class NewColorView(CreateView):
    model = Color
    form_class = ColorForm
    template_name = "color_app/color_form.html"
    success_url = reverse_lazy("color_app:color_list")

class ColorDetailView(DetailView):
    model = Color
    template_name = "color_app/color_detail.html"
      
    def get_context_data(self, *args, **kwargs):
        "Adds properties to the context dict sent to the template" 
        context = super().get_context_data(*args, **kwargs)
        color = self.get_object()
        hues = []
        for adjustment in settings.HUES_TO_SHOW:
            if adjustment == 0:
                hues.append(color)
            else:
                hue = color.adjust_hue(adjustment)
                hue.name = hue.hex_code()
                hues.append(hue)
        context['color'] = color
        context['hues'] = hues
        return context


