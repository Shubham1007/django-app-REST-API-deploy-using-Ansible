from django.contrib.auth.models import Group
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render_to_response

def create_finwallet_default_group(request):
    """
        Create finwallet user group
    """

    for group in settings.DEFAULT_USER_GROUP:
        new_group, created = Group.objects.get_or_create(name=group)

    response = {
        'status': True,
        'message' : 'Group created successful'
    }

    return JsonResponse(response, status=200)


def homeView(request):
    """
        finwallet API home view
    """

    # docs_url =  request.META['HTTP_HOST'] + '/5000'
    # response = {
    #     'status': True,
    #     'message' : 'Welcome to Finwallet API, API docs in ' + docs_url
    # }

    return render_to_response('home.html')
    #return JsonResponse(response, status=200)


def get_pagination_meta(request):
    """
        return calculated pagesize, limit, offset
    """
    post_per_page = request.GET.get('limit')
    page = request.GET.get('page')

    if page: page = int(page)
    if post_per_page: post_per_page = int(post_per_page)

    
    if not page or page == 0:
        page = 1
    else:
        page = int(page)

    if not post_per_page or post_per_page == 0 or post_per_page > 100:
        post_per_page = 20
    else:
        post_per_page = int(post_per_page)


    offset = page * post_per_page - post_per_page
    pagesize = page * post_per_page

    return post_per_page, offset, pagesize
