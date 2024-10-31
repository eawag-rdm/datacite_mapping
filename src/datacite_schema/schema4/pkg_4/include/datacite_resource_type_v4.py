from enum import Enum

__NAMESPACE__ = "http://datacite.org/schema/kernel-4"


class ResourceType(Enum):
    """
    The general type of a resource.
    """

    AUDIOVISUAL = "Audiovisual"
    BOOK = "Book"
    BOOK_CHAPTER = "BookChapter"
    COLLECTION = "Collection"
    COMPUTATIONAL_NOTEBOOK = "ComputationalNotebook"
    CONFERENCE_PAPER = "ConferencePaper"
    CONFERENCE_PROCEEDING = "ConferenceProceeding"
    DATA_PAPER = "DataPaper"
    DATASET = "Dataset"
    DISSERTATION = "Dissertation"
    EVENT = "Event"
    IMAGE = "Image"
    INTERACTIVE_RESOURCE = "InteractiveResource"
    JOURNAL = "Journal"
    JOURNAL_ARTICLE = "JournalArticle"
    MODEL = "Model"
    OUTPUT_MANAGEMENT_PLAN = "OutputManagementPlan"
    PEER_REVIEW = "PeerReview"
    PHYSICAL_OBJECT = "PhysicalObject"
    PREPRINT = "Preprint"
    REPORT = "Report"
    SERVICE = "Service"
    SOFTWARE = "Software"
    SOUND = "Sound"
    STANDARD = "Standard"
    TEXT = "Text"
    WORKFLOW = "Workflow"
    OTHER = "Other"
