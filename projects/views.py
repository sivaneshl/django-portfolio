from django.shortcuts import render
from projects.models import Project


def project_index(request):
    """ An index view that shows a snippet of information about each project """
    # query to retrieve all objects in Project table
    projects = Project.objects.all()
    # the dict projects has the queryset (result) returned from the above query
    context = {'projects': projects}
    # context is added as an argument to render()
    # Any entries in the context dictionary are available in the template, as long as the context argument is passed
    # to render(). The context dictionary is used to send information to our template. Every view function you create
    # needs to have a context dictionary.
    return render(request, 'project_index.html', context)


def project_detail(request, pk):
    """ A detail view that shows more information on a particular topic """
    # This function will need an additional argument: the id of the project that’s being viewed
    project = Project.objects.get(pk=pk)
    context = {'project': project}
    return render(request, 'project_detail.html', context)
