import models

def open_petitions(request):
    if not request.user.is_authenticated():
        return {}
    if request.user.is_staff or request.user.is_admin:
        petitions = models.Petition.objects.filter(closed=False)
    else:
        petitions = models.Petition.objects.filter(closed=False, author=request.user)
    return {'open_petitions': petitions}