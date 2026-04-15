# from . import log_service
from adapters.persistence import repositories

class ProjectActions():
    
    def create_project_showcase_card(self,  POST_data):
        # log_service.Log.create(request)

        showcase = repositories.DjangoProjectShowcaseRepository()

        showcase.create(POST_data)

        content = {
            "create_status": False, 
        }

        return content

    def delete():
        pass
