from . import log_service
from adapters.persistence import repositories
class ProjectActions():
    
    def create(self, request):
        log_service.Log.create()
        self.create_project_card(request)

        content = {
            "create_status": False # guilty before proven 
        }

    def create_project_card(self, request):

        if request.POST:

            title = request.POST.get("title")
            desc = request.POST.get("desc")
            image = request.POST.FILE("image")

            

        pass

    def delete():
        pass
