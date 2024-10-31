from enum import Enum

__NAMESPACE__ = "http://datacite.org/schema/kernel-4"


class DescriptionType(Enum):
    """
    The type of the description.
    """

    ABSTRACT = "Abstract"
    METHODS = "Methods"
    SERIES_INFORMATION = "SeriesInformation"
    TABLE_OF_CONTENTS = "TableOfContents"
    TECHNICAL_INFO = "TechnicalInfo"
    OTHER = "Other"
