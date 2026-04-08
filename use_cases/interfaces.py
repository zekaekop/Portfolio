
class FAQRepository:
    def create(self, FAQ):
        raise NotImplementedError

    def archive(self, FAQ):
        raise NotImplementedError
    
    def list(self) -> list:
        raise NotImplementedError

class FeedbackRepository:
    def create(self, feedback):
        raise NotImplementedError