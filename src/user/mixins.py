from user.models import User
from django.contrib.auth.mixins import LoginRequiredMixin

class GroupMixin:
    def user_in_group(self, group: str):
        """
        Check if the current user (self.request.user) is in the group provided as 
        arg: group. For instance: 'Editor'
        """
        if self.request.user.is_authenticated:
            return self.request.user.groups.filter(name=group).exists()
        return False


class StaffRequiredMixin(LoginRequiredMixin):
    """
    Mixin for checking if user is staff in a view.

    Provide in Child class as first class to inherit, e.g: 
        MyClass(StaffRequiredMixin, SomeOtherClass)

    """

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            from django.core.exceptions import PermissionDenied
            raise PermissionDenied("You do not have permission to access this page.")

        return super().dispatch(request, *args, **kwargs)


