
from enum import Enum

class Status(Enum):
    UNANSWERED = "Unanswered"
    ANSWERED = "Answered"
    WORK_IN_PROGRESS = "Work In Progress"
    ARCHIVED = "Archived"

class Report(Enum):
    DUPLICATE = "Duplicate Question"
    UNCLEAR = "Requests more information about the question"
    MALICIOUS = "Malicious"

# These would probably be the same as on github but for now i will add placeholder tags
class Feedback_tags(Enum):
    ENHANCEMENT = "New feature or request"
    BUG = "Something has gone wrong"
    OTHER = "Other"

# class GenericQrs():
#     def 


class FAQ():
    def __init__(
        anon,
        question,
        answer,
        desc,
        created_date,
        answered_date,
        deletion_date,
        ):
        self.anon = anon
        self.question = question
        self.answer = answer
        self.desc = desc
        self.created_date = created_date
        self.answered_date = answered_date
        self.deletion_date = deletion_date

    def archive(self):
        return self.Status == Status.ARCHIVED 

    def create(self):
        return self.Status == Status.UNANSWERED
    
    def report_duplicate(self):
        return self.Report == Report.DUPLICATE

    def report_unclear(self):
        return self.Report == Report.UNCLEAR

    def report_malicious(self):
        return self.Report == Report.MALICIOUS