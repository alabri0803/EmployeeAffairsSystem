from django.core.exceptions import PermissionDenied

def owner_required(user):
    if user.role != 'owner':
        raise PermissionDenied
    
def hr_required(user):
    if user.role != 'hr':
        raise PermissionDenied