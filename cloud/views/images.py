import logging
from django import forms
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response, redirect
from django.template import Context, loader
from django.template.context import RequestContext
from cloud.models.image import Image, IMG_FORMATS, IMG_TARGETS
from cloud.helpers import session_flash

# Configure logging for the module name
logger = logging.getLogger(__name__)
view_vars = {
    'active_item': None,
    'active_menu': 'Computing',
    'active_section': 'Images',
}


@login_required
def index(request):
    global view_vars
    t = loader.get_template('images-index.html')
    image_list = Image.objects.all()
    view_vars.update({
        'active_item': None,
        'title': 'Images List',
        'actions': [{
            'name': 'New Image',
            'url': '/Aurora/cloud/images/new/',
            'image': 'plus'
        }]
    })
    c = Context({
        'image_list': image_list,
        'view_vars': view_vars,
        'request': request,
        'flash': session_flash.get_flash(request)
    })
    return HttpResponse(t.render(c))


@login_required
def detail(request, image_id):
    global view_vars
    try:
        image = Image.objects.get(pk=image_id)
    except Image.DoesNotExist:
        raise Http404

    view_vars.update({
        'active_item': image,
        'title': 'Image Details',
        'actions': [{
            'name': 'Back to List',
            'url': '/Aurora/cloud/images/',
            'image': 'chevron-left'
        }]
    })
    return render_to_response('images-detail.html', {
        'image': image,
        'view_vars': view_vars,
        'request': request
    })


class ImageModelForm(forms.ModelForm):
    action = '/Aurora/cloud/images/new/'
    class Meta:
        model = Image
        fields = ['name', 'file_format', 'target_dev', 'description', 'image_file']


@login_required
def new(request):
    global view_vars
    if request.method == 'POST':  # If the form has been submitted...
        form = ImageModelForm(request.POST, request.FILES)  # A form bound to the POST data
        if form.is_valid():  # All validation rules pass
            form.save()
            session_flash.set_flash(request, "New Image successfully created")
            return redirect('cloud-images-index')  # Redirect after POST
    else:
        form = ImageModelForm()  # An unbound form

    view_vars.update({
        'active_item': None,
        'title': 'New Image',
        'actions': [{
            'name': 'Back to List', 
            'url': "/Aurora/cloud/images/",
            'image': 'chevron-left'
        }]
    })
    c = RequestContext(request, {
        'form': form,
        'view_vars': view_vars,
        'request': request,
        'flash': session_flash.get_flash(request)
    })
    return render_to_response('base-form.html', c)


@login_required
def delete(request, image_id):
    try:
        img = Image.objects.get(pk=image_id)
    except Image.DoesNotExist:
        raise Http404

    img.delete()
    session_flash.set_flash(
        request,
        "Image %s was successfully deleted!" % str(img)
    )
    logger.debug("Host %s was successfully deleted!" % str(img))

    return redirect('cloud-images-index')

