
class FAQRepository:
    def create(self, FAQ):
        raise NotImplementedError

    def archive(self, FAQ):
        raise NotImplementedError
    
    def list(self) -> list:
        raise NotImplementedError

class ProjectShowcaseRepository:

    def create(self, project):
        raise NotImplementedError

    def delete(self, project):
        raise NotImplementedError

    def list(self) -> list:
        raise NotImplementedError

class FeedbackRepository:
    def create(self, feedback):
        raise NotImplementedError

    def list(self) -> list:
        raise NotImplementedError

class LogRepository:
    def create(self, log):
        raise NotImplementedError

    def delete(self, log):
        raise NotImplementedError

    def list(self) -> list:
        raise NotImplementedError