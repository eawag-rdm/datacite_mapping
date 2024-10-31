from enum import Enum

__NAMESPACE__ = "http://datacite.org/schema/kernel-4"


class FunderIdentifierType(Enum):
    """
    The type of the funderIdentifier.
    """

    ISNI = "ISNI"
    GRID = "GRID"
    ROR = "ROR"
    CROSSREF_FUNDER_ID = "Crossref Funder ID"
    OTHER = "Other"
