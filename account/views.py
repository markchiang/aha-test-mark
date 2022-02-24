from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from account.serializers import UserSerializer#, GroupSerializer
from django.contrib.auth import logout as auth_logout
from django.shortcuts import redirect

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


#class GroupViewSet(viewsets.ModelViewSet):
#    """
#    API endpoint that allows groups to be viewed or edited.
#    """
#    queryset = Group.objects.all()
#    serializer_class = GroupSerializer
#    permission_classes = [permissions.IsAuthenticated]
def logout(request):
    auth_logout(request)
    return redirect(request.META.get('HTTP_REFERER'))
