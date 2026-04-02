
class FAQRepository:
    def create(self, FAQ):
        raise NotImplementedError

    def archive(self, FAQ):
        raise NotImplementedError
    
    def list(self) -> list:
        raise NotImplementedError