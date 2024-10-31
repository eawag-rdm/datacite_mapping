from enum import Enum

__NAMESPACE__ = "http://datacite.org/schema/kernel-4"


class TitleType(Enum):
    ALTERNATIVE_TITLE = "AlternativeTitle"
    SUBTITLE = "Subtitle"
    TRANSLATED_TITLE = "TranslatedTitle"
    OTHER = "Other"
