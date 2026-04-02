
class Status(Enum):
    UNANSWERED = "Unanswered"
    ANSWERED = "Answered"
    WORK_IN_PROGRESS = "Work In Progress"
    ARCHIVED = "Archived"

class Report(Enum):
    DUPLICATE = "Duplicate Question"
    UNCLEAR = "Requests more information about the question"
    MALICIOUS = "Malicious"

class FAQ:
    def __init__(
        anon,
        asked_question,
        answer,
        created_date
        ):
        self.anon = anon
        self.asked_question = asked_question
        self.answer = answer
        self.created_date = created_date

class FAQS:
    def __init__(
        anon,
        question,
        desc,
        created_date
        ):
        self.anon = anon
        self.question = asked_question
        self.desc = answer
        self.created_date = created_date

    def archive():
        return self.Status == Status.ARCHIVED 

    def create():
        return self.Status == Status.UNANSWERED
    
    def report_duplicate():
        return self.Report == Report.DUPLICATE

    def report_unclear():
        return self.Report == Report.UNCLEAR

    def report_MALICOUS():
        return self.Report == Report.MALICIOUS