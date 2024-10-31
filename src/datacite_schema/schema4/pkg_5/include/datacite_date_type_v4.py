from enum import Enum

__NAMESPACE__ = "http://datacite.org/schema/kernel-4"


class DateType(Enum):
    """The type of date.

    Use RKMS‐ISO8601 standard for depicting date ranges.To indicate the
    end of an embargo period, use Available. To indicate the start of an
    embargo period, use Submitted or Accepted, as appropriate.
    """

    ACCEPTED = "Accepted"
    AVAILABLE = "Available"
    COLLECTED = "Collected"
    COPYRIGHTED = "Copyrighted"
    CREATED = "Created"
    ISSUED = "Issued"
    OTHER = "Other"
    SUBMITTED = "Submitted"
    UPDATED = "Updated"
    VALID = "Valid"
    WITHDRAWN = "Withdrawn"
