from enum import Enum

__NAMESPACE__ = "http://datacite.org/schema/kernel-4"


class RelatedIdentifierType(Enum):
    """
    The type of the RelatedIdentifier.
    """

    ARK = "ARK"
    AR_XIV = "arXiv"
    BIBCODE = "bibcode"
    DOI = "DOI"
    EAN13 = "EAN13"
    EISSN = "EISSN"
    HANDLE = "Handle"
    IGSN = "IGSN"
    ISBN = "ISBN"
    ISSN = "ISSN"
    ISTC = "ISTC"
    LISSN = "LISSN"
    LSID = "LSID"
    PMID = "PMID"
    PURL = "PURL"
    UPC = "UPC"
    URL = "URL"
    URN = "URN"
    W3ID = "w3id"
