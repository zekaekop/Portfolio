from django.shortcuts import render
from adapters.persistence.models import Anon, FAQuestions
from frameworks.django.home.views import get_client_ip
from core.entities import entities
import datetime
# Create your views here.

def create_FAQ(
    repository: interfaces.FAQRepository,
    anon: int,
    question: str,
    answer: str,
    desc: str,
    ):
    
    faq_dict = dict(
        anon = anon,
        question = question,
        answer = answer,
        desc = desc,
        created_date = datetime.datetime.now(),
        answered_date = None,
        deletion_date =  None,
    )

    repository.create(faq_dict)

def answer_FAQ(
    repository: interfaces.FAQRepository,
    anon: int,
    archive_id: int,
    question: str,
    answer: str,
    created_date: datetime,
    answered_date: datetime,
    deletion_date: datetime,
    ):

    # why not just add the POST data directly into faq_dict?
    faq_answer_dict = dict(
        anon = anon,
        question = question,
        answer = answer,
        desc = desc,
        created_date = created_date,
        answered_date = answered_date,
        deletion_date = deletion_date,
    )

    repository.answer_FAQ(faq_answer_dict)

def create_feedback_report(
    repository: interfaces.FAQRepository,
    title: str,
    desc: str,
    anon: int,
    ):

    report_dict = dict(
        anon = anon,
        title = title,
        desc = desc,
    )

    repository.create(report_dict)

# Why not just call the function from FAQ web view instead of having to pass it through use_case?
def archive_FAQ(
    repository: interfaces.FAQRepository,
    archive_id: int,
    ):

    repository.archive(archive_id)

def archive_deletion_check_FAQ():
    FAQ_archive = get_all_archives()
    repository.archive(archive_id)