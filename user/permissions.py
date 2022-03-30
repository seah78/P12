from rest_framework.permissions import BasePermission, SAFE_METHODS
from django.core.exceptions import ObjectDoesNotExist


from user.models import User

class IsManager(BasePermission):
    """
        Manager : Read only on the CRM
    """
    def has_permission(self, request, view):
        return request.user.department == User.DEPARTMENT_MANAGER and request.method in SAFE_METHODS
    
    def has_object_permission(self, request, view, obj):
        return self.has_permission(request, view)
    
            


        
        
            
            
class IsSeller(BasePermission):
    def is_saler(self, user):
        pass
        
        
class IsSupport(BasePermission):
    def is_support(self, user):
        pass
    
    
    
"""    

class IsContributor(BasePermission):
    def is_contributor(self, user, project):
        try:
            models.Contributors.objects.get(user=user, project=project)
        except ObjectDoesNotExist:
            return False

        return True


class IsAuthor(BasePermission):
    def is_author(self, pk, user):
        try:
            content = models.Project.objects.get(pk=pk)
        except ObjectDoesNotExist:
            return True

        return content.author == user


class IsContributorOrAuthorProjectInProjectView(IsContributor, IsAuthor):
    def has_permission(self, request, view):
        if view.kwargs.get("pk") is None:
            return True
        if view.action == "create":
            return True
        if view.action in ("destroy", "update"):
            return self.is_author(view.kwargs["pk"], request.user)
        return self.is_contributor(request.user,
                                   view.kwargs["pk"]) or self.is_author(
            view.kwargs["pk"], request.user
        )


class IsContributorOrAuthorProjectInContributorView(IsContributor, IsAuthor):
    def has_permission(self, request, view):
        if view.action in ("create", "destroy", "update"):
            return self.is_author(view.kwargs["projects_pk"], request.user)
        return self.is_contributor(
            request.user, view.kwargs["projects_pk"]
        ) or self.is_author(view.kwargs["projects_pk"], request.user)


class IsContributorOrAuthorProjectInIssueView(IsContributor, IsAuthor):
    def has_permission(self, request, view):
        if view.action in ("destroy", "update"):
            return self.is_author(view.kwargs["projects_pk"], request.user)
        return self.is_contributor(request.user, view.kwargs["projects_pk"])


class IsAuthorComment(BasePermission):
    def is_author_comment(self, pk, user):
        try:
            content = models.Comments.objects.get(pk=pk)
        except ObjectDoesNotExist:
            return True

        return content.author_user_id == user


class IsContributorOrAuthorProjectInCommentView(
    IsContributor, IsAuthor, IsAuthorComment
):
    def has_permission(self, request, view):

        if view.action in ("update"):
            return self.is_author_comment(view.kwargs["pk"], request.user)
        return self.is_contributor(
            request.user, view.kwargs["projects_pk"]
        ) or self.is_author(view.kwargs["projects_pk"], request.user)

"""