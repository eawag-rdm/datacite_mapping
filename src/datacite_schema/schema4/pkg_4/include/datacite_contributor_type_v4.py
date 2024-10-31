from enum import Enum

__NAMESPACE__ = "http://datacite.org/schema/kernel-4"


class ContributorType(Enum):
    """
    The type of contributor of the resource.
    """

    CONTACT_PERSON = "ContactPerson"
    DATA_COLLECTOR = "DataCollector"
    DATA_CURATOR = "DataCurator"
    DATA_MANAGER = "DataManager"
    DISTRIBUTOR = "Distributor"
    EDITOR = "Editor"
    HOSTING_INSTITUTION = "HostingInstitution"
    OTHER = "Other"
    PRODUCER = "Producer"
    PROJECT_LEADER = "ProjectLeader"
    PROJECT_MANAGER = "ProjectManager"
    PROJECT_MEMBER = "ProjectMember"
    REGISTRATION_AGENCY = "RegistrationAgency"
    REGISTRATION_AUTHORITY = "RegistrationAuthority"
    RELATED_PERSON = "RelatedPerson"
    RESEARCH_GROUP = "ResearchGroup"
    RIGHTS_HOLDER = "RightsHolder"
    RESEARCHER = "Researcher"
    SPONSOR = "Sponsor"
    SUPERVISOR = "Supervisor"
    WORK_PACKAGE_LEADER = "WorkPackageLeader"
