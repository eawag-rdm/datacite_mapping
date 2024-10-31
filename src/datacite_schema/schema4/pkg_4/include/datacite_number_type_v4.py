from enum import Enum

__NAMESPACE__ = "http://datacite.org/schema/kernel-4"


class NumberType(Enum):
    ARTICLE = "Article"
    CHAPTER = "Chapter"
    REPORT = "Report"
    OTHER = "Other"
