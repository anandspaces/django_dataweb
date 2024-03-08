from django.shortcuts import render
from .forms import CustomerForm
# Create your views here.
def home(request):
    template = 'index.html'
    return render(request,template,{})

def charts_apexcharts(request):
    template = 'charts-apexcharts.html'
    return render(request,template,{})

def charts_chartjs(request):
    template = 'charts-chartjs.html'
    return render(request,template,{})

def charts_echarts(request):
    template = 'charts-echarts.html'
    return render(request,template,{})

def components_accordion(request):
    template = 'components-accordion.html'
    return render(request,template,{})

def components_alerts(request):
    template = 'components-alerts.html'
    return render(request,template,{})

def components_badges(request):
    template = 'components-badges.html'
    return render(request,template,{})

def components_breadcrumbs(request):
    template = 'components-breadcrumbs.html'
    return render(request,template,{})

def components_buttons(request):
    template = 'components-buttons.html'
    return render(request,template,{})

def components_cards(request):
    template = 'components-cards.html'
    return render(request,template,{})

def components_carousel(request):
    template = 'components-carousel.html'
    return render(request,template,{})

def components_list_group(request):
    template = 'components-list-group.html'
    return render(request,template,{})

def components_modal(request):
    template = 'components-modal.html'
    return render(request,template,{})

def components_pagination(request):
    template = 'components-pagination.html'
    return render(request,template,{})

def components_progress(request):
    template = 'components-progress.html'
    return render(request,template,{})

def components_spinners(request):
    template = 'components-spinners.html'
    return render(request,template,{})

def components_tabs(request):
    template = 'components-tabs.html'
    return render(request,template,{})

def components_tooltips(request):
    template = 'components-tooltips.html'
    return render(request,template,{})

def forms_editors(request):
    template = 'forms-editors.html'
    return render(request,template,{})

def forms_elements(request):
    template = 'forms-elements.html'
    return render(request,template,{})

def forms_layouts(request):
    template = 'forms-layouts.html'
    return render(request,template,{})

def forms_validation(request):
    template = 'forms-validation.html'
    return render(request,template,{})

def icons_bootstrap(request):
    template = 'icons-bootstrap.html'
    return render(request,template,{})

def icons_boxicons(request):
    template = 'icons-boxicons.html'
    return render(request,template,{})

def icons_remix(request):
    template = 'icons-remix.html'
    return render(request,template,{})

def pages_blank(request):
    template = 'pages-blank.html'
    return render(request,template,{})

def pages_contact(request):
    template = 'pages-contact.html'
    return render(request,template,{})

def pages_error(request):
    template = 'pages-error-404.html'
    return render(request,template,{})

def pages_faq(request):
    template = 'pages-faq.html'
    return render(request,template,{})

def pages_login(request):
    template = 'pages-login.html'
    return render(request,template,{})

def pages_register(request):
    template = 'pages-register.html'
    form = CustomerForm
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request,template,{'form':form})

def tables_data(request):
    template = 'tables-data.html'
    return render(request,template,{})

def tables_general(request):
    template = 'tables-general.html'
    return render(request,template,{})

def users_profile(request):
    template = 'users-profile.html'
    return render(request,template,{})