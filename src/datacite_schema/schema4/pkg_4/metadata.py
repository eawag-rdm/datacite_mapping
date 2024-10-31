from typing import List, Optional, Union

from pydantic import BaseModel, ConfigDict
from xsdata_pydantic.fields import field

from src.datacite_schema.schema4.pkg_4.include.datacite_contributor_type_v4 import (
    ContributorType,
)
from src.datacite_schema.schema4.pkg_4.include.datacite_date_type_v4 import (
    DateType,
)
from src.datacite_schema.schema4.pkg_4.include.datacite_description_type_v4 import (
    DescriptionType,
)
from src.datacite_schema.schema4.pkg_4.include.datacite_funder_identifier_type_v4 import (
    FunderIdentifierType,
)
from src.datacite_schema.schema4.pkg_4.include.datacite_name_type_v4 import (
    NameType,
)
from src.datacite_schema.schema4.pkg_4.include.datacite_number_type_v4 import (
    NumberType,
)
from src.datacite_schema.schema4.pkg_4.include.datacite_related_identifier_type_v4 import (
    RelatedIdentifierType,
)
from src.datacite_schema.schema4.pkg_4.include.datacite_relation_type_v4 import (
    RelationType,
)
from src.datacite_schema.schema4.pkg_4.include.datacite_resource_type_v4 import (
    ResourceType,
)
from src.datacite_schema.schema4.pkg_4.include.datacite_title_type_v4 import (
    TitleType,
)
from src.datacite_schema.schema4.pkg_4.include.xml import LangValue

__NAMESPACE__ = "http://datacite.org/schema/kernel-4"


class Affiliation(BaseModel):
    """
    Uniquely identifies an affiliation, according to various identifier schemes.
    """

    class Meta:
        name = "affiliation"

    model_config = ConfigDict(defer_build=True)
    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        },
    )
    affiliation_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "affiliationIdentifier",
            "type": "Attribute",
        },
    )
    affiliation_identifier_scheme: Optional[str] = field(
        default=None,
        metadata={
            "name": "affiliationIdentifierScheme",
            "type": "Attribute",
        },
    )
    scheme_uri: Optional[str] = field(
        default=None,
        metadata={
            "name": "schemeURI",
            "type": "Attribute",
        },
    )


class Box(BaseModel):
    class Meta:
        name = "box"

    model_config = ConfigDict(defer_build=True)
    west_bound_longitude: float = field(
        metadata={
            "name": "westBoundLongitude",
            "type": "Element",
            "namespace": "http://datacite.org/schema/kernel-4",
            "required": True,
            "min_inclusive": -180.0,
            "max_inclusive": 180.0,
        }
    )
    east_bound_longitude: float = field(
        metadata={
            "name": "eastBoundLongitude",
            "type": "Element",
            "namespace": "http://datacite.org/schema/kernel-4",
            "required": True,
            "min_inclusive": -180.0,
            "max_inclusive": 180.0,
        }
    )
    south_bound_latitude: float = field(
        metadata={
            "name": "southBoundLatitude",
            "type": "Element",
            "namespace": "http://datacite.org/schema/kernel-4",
            "required": True,
            "min_inclusive": -90.0,
            "max_inclusive": 90.0,
        }
    )
    north_bound_latitude: float = field(
        metadata={
            "name": "northBoundLatitude",
            "type": "Element",
            "namespace": "http://datacite.org/schema/kernel-4",
            "required": True,
            "min_inclusive": -90.0,
            "max_inclusive": 90.0,
        }
    )


class NameIdentifier(BaseModel):
    """
    Uniquely identifies a creator or contributor, according to various identifier
    schemes.
    """

    class Meta:
        name = "nameIdentifier"

    model_config = ConfigDict(defer_build=True)
    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        },
    )
    name_identifier_scheme: str = field(
        metadata={
            "name": "nameIdentifierScheme",
            "type": "Attribute",
            "required": True,
        }
    )
    scheme_uri: Optional[str] = field(
        default=None,
        metadata={
            "name": "schemeURI",
            "type": "Attribute",
        },
    )


class Point(BaseModel):
    class Meta:
        name = "point"

    model_config = ConfigDict(defer_build=True)
    point_longitude: float = field(
        metadata={
            "name": "pointLongitude",
            "type": "Element",
            "namespace": "http://datacite.org/schema/kernel-4",
            "required": True,
            "min_inclusive": -180.0,
            "max_inclusive": 180.0,
        }
    )
    point_latitude: float = field(
        metadata={
            "name": "pointLatitude",
            "type": "Element",
            "namespace": "http://datacite.org/schema/kernel-4",
            "required": True,
            "min_inclusive": -90.0,
            "max_inclusive": 90.0,
        }
    )


class Resource(BaseModel):
    """Root element of a single record.

    This wrapper element is for XML implementation only and is not defined in the DataCite DOI standard.
    Note: This is the case for all wrapper elements within this schema.
    No content in this wrapper element.

    :ivar identifier: A persistent identifier that identifies a
        resource.
    :ivar creators:
    :ivar titles:
    :ivar publisher: The name of the entity that holds, archives,
        publishes prints, distributes, releases, issues, or produces the
        resource. This property will be used to formulate the citation,
        so consider the prominence of the role. In the case of datasets,
        "publish" is understood to mean making the data available to the
        community of researchers.
    :ivar publication_year: Year when the data is made publicly
        available. If an embargo period has been in effect, use the date
        when the embargo period ends. In the case of datasets, "publish"
        is understood to mean making the data available on a specific
        date to the community of researchers. If there is no standard
        publication year value, use the date that would be preferred
        from a citation perspective. YYYY
    :ivar resource_type: The type of a resource. You may enter an
        additional free text description. The format is open, but the
        preferred format is a single term of some detail so that a pair
        can be formed with the sub-property.
    :ivar subjects:
    :ivar contributors:
    :ivar dates:
    :ivar language: Primary language of the resource. Allowed values are
        taken from  IETF BCP 47, ISO 639-1 language codes.
    :ivar alternate_identifiers:
    :ivar related_identifiers:
    :ivar sizes:
    :ivar formats:
    :ivar version: Version number of the resource. If the primary
        resource has changed the version number increases. Register a
        new identifier for a major version change. Individual stewards
        need to determine which are major vs. minor versions. May be
        used in conjunction with properties 11 and 12
        (AlternateIdentifier and RelatedIdentifier) to indicate various
        information updates. May be used in conjunction with property 17
        (Description) to indicate the nature and file/record range of
        version.
    :ivar rights_list:
    :ivar descriptions:
    :ivar geo_locations:
    :ivar funding_references:
    :ivar related_items:
    """

    class Meta:
        name = "resource"
        namespace = "http://datacite.org/schema/kernel-4"

    model_config = ConfigDict(defer_build=True)
    identifier: "Resource.Identifier" = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    creators: "Resource.Creators" = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    titles: "Resource.Titles" = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    publisher: "Resource.Publisher" = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    publication_year: str = field(
        metadata={
            "name": "publicationYear",
            "type": "Element",
            "required": True,
            "pattern": r"[\d]{4}",
        }
    )
    resource_type: "Resource.ResourceType" = field(
        metadata={
            "name": "resourceType",
            "type": "Element",
            "required": True,
        }
    )
    subjects: Optional["Resource.Subjects"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    contributors: Optional["Resource.Contributors"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    dates: Optional["Resource.Dates"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    language: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    alternate_identifiers: Optional["Resource.AlternateIdentifiers"] = field(
        default=None,
        metadata={
            "name": "alternateIdentifiers",
            "type": "Element",
        },
    )
    related_identifiers: Optional["Resource.RelatedIdentifiers"] = field(
        default=None,
        metadata={
            "name": "relatedIdentifiers",
            "type": "Element",
        },
    )
    sizes: Optional["Resource.Sizes"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    formats: Optional["Resource.Formats"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    version: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    rights_list: Optional["Resource.RightsList"] = field(
        default=None,
        metadata={
            "name": "rightsList",
            "type": "Element",
        },
    )
    descriptions: Optional["Resource.Descriptions"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    geo_locations: Optional["Resource.GeoLocations"] = field(
        default=None,
        metadata={
            "name": "geoLocations",
            "type": "Element",
        },
    )
    funding_references: Optional["Resource.FundingReferences"] = field(
        default=None,
        metadata={
            "name": "fundingReferences",
            "type": "Element",
        },
    )
    related_items: Optional["Resource.RelatedItems"] = field(
        default=None,
        metadata={
            "name": "relatedItems",
            "type": "Element",
        },
    )

    class Identifier(BaseModel):
        model_config = ConfigDict(defer_build=True)
        value: str = field(
            default="",
            metadata={
                "required": True,
                "min_length": 1,
            },
        )
        identifier_type: object = field(
            metadata={
                "name": "identifierType",
                "type": "Attribute",
                "required": True,
            }
        )

    class Creators(BaseModel):
        """
        :ivar creator: The main researchers involved working on the
            data, or the authors of the publication in priority order.
            May be a corporate/institutional or personal name. Format:
            Family, Given. Personal names can be further specified using
            givenName and familyName.
        """

        model_config = ConfigDict(defer_build=True)
        creator: List["Resource.Creators.Creator"] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "min_occurs": 1,
            },
        )

        class Creator(BaseModel):
            model_config = ConfigDict(defer_build=True)
            creator_name: "Resource.Creators.Creator.CreatorName" = field(
                metadata={
                    "name": "creatorName",
                    "type": "Element",
                    "required": True,
                }
            )
            given_name: Optional[object] = field(
                default=None,
                metadata={
                    "name": "givenName",
                    "type": "Element",
                },
            )
            family_name: Optional[object] = field(
                default=None,
                metadata={
                    "name": "familyName",
                    "type": "Element",
                },
            )
            name_identifier: List[object] = field(
                default_factory=list,
                metadata={
                    "name": "nameIdentifier",
                    "type": "Element",
                },
            )
            affiliation: List[object] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                },
            )

            class CreatorName(BaseModel):
                model_config = ConfigDict(defer_build=True)
                value: str = field(
                    default="",
                    metadata={
                        "required": True,
                    },
                )
                name_type: Optional[NameType] = field(
                    default=None,
                    metadata={
                        "name": "nameType",
                        "type": "Attribute",
                    },
                )
                lang: Optional[Union[str, LangValue]] = field(
                    default=None,
                    metadata={
                        "type": "Attribute",
                        "namespace": "http://www.w3.org/XML/1998/namespace",
                    },
                )

    class Titles(BaseModel):
        """
        :ivar title: A name or title by which a resource is known.
        """

        model_config = ConfigDict(defer_build=True)
        title: List["Resource.Titles.Title"] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "min_occurs": 1,
            },
        )

        class Title(BaseModel):
            model_config = ConfigDict(defer_build=True)
            value: str = field(
                default="",
                metadata={
                    "required": True,
                },
            )
            title_type: Optional[TitleType] = field(
                default=None,
                metadata={
                    "name": "titleType",
                    "type": "Attribute",
                },
            )
            lang: Optional[Union[str, LangValue]] = field(
                default=None,
                metadata={
                    "type": "Attribute",
                    "namespace": "http://www.w3.org/XML/1998/namespace",
                },
            )

    class Publisher(BaseModel):
        model_config = ConfigDict(defer_build=True)
        value: str = field(
            default="",
            metadata={
                "required": True,
                "min_length": 1,
            },
        )
        lang: Optional[Union[str, LangValue]] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": "http://www.w3.org/XML/1998/namespace",
            },
        )

    class ResourceType(BaseModel):
        model_config = ConfigDict(defer_build=True)
        value: str = field(
            default="",
            metadata={
                "required": True,
            },
        )
        resource_type_general: ResourceType = field(
            metadata={
                "name": "resourceTypeGeneral",
                "type": "Attribute",
                "required": True,
            }
        )

    class Subjects(BaseModel):
        """
        :ivar subject: Subject, keywords, classification codes, or key
            phrases describing the resource.
        """

        model_config = ConfigDict(defer_build=True)
        subject: List["Resource.Subjects.Subject"] = field(
            default_factory=list,
            metadata={
                "type": "Element",
            },
        )

        class Subject(BaseModel):
            model_config = ConfigDict(defer_build=True)
            value: str = field(
                default="",
                metadata={
                    "required": True,
                },
            )
            subject_scheme: Optional[object] = field(
                default=None,
                metadata={
                    "name": "subjectScheme",
                    "type": "Attribute",
                },
            )
            scheme_uri: Optional[str] = field(
                default=None,
                metadata={
                    "name": "schemeURI",
                    "type": "Attribute",
                },
            )
            value_uri: Optional[str] = field(
                default=None,
                metadata={
                    "name": "valueURI",
                    "type": "Attribute",
                },
            )
            classification_code: Optional[str] = field(
                default=None,
                metadata={
                    "name": "classificationCode",
                    "type": "Attribute",
                },
            )
            lang: Optional[Union[str, LangValue]] = field(
                default=None,
                metadata={
                    "type": "Attribute",
                    "namespace": "http://www.w3.org/XML/1998/namespace",
                },
            )

    class Contributors(BaseModel):
        """
        :ivar contributor: The institution or person responsible for
            collecting, creating, or otherwise contributing to the
            developement of the dataset. The personal name format should
            be: Family, Given.
        """

        model_config = ConfigDict(defer_build=True)
        contributor: List["Resource.Contributors.Contributor"] = field(
            default_factory=list,
            metadata={
                "type": "Element",
            },
        )

        class Contributor(BaseModel):
            model_config = ConfigDict(defer_build=True)
            contributor_name: "Resource.Contributors.Contributor.ContributorName" = field(
                metadata={
                    "name": "contributorName",
                    "type": "Element",
                    "required": True,
                }
            )
            given_name: Optional[object] = field(
                default=None,
                metadata={
                    "name": "givenName",
                    "type": "Element",
                },
            )
            family_name: Optional[object] = field(
                default=None,
                metadata={
                    "name": "familyName",
                    "type": "Element",
                },
            )
            name_identifier: List[object] = field(
                default_factory=list,
                metadata={
                    "name": "nameIdentifier",
                    "type": "Element",
                },
            )
            affiliation: List[object] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                },
            )
            contributor_type: ContributorType = field(
                metadata={
                    "name": "contributorType",
                    "type": "Attribute",
                    "required": True,
                }
            )

            class ContributorName(BaseModel):
                model_config = ConfigDict(defer_build=True)
                value: str = field(
                    default="",
                    metadata={
                        "required": True,
                        "min_length": 1,
                    },
                )
                name_type: Optional[NameType] = field(
                    default=None,
                    metadata={
                        "name": "nameType",
                        "type": "Attribute",
                    },
                )
                lang: Optional[Union[str, LangValue]] = field(
                    default=None,
                    metadata={
                        "type": "Attribute",
                        "namespace": "http://www.w3.org/XML/1998/namespace",
                    },
                )

    class Dates(BaseModel):
        """
        :ivar date: Different dates relevant to the work. YYYY,YYYY-MM-
            DD, YYYY-MM-DDThh:mm:ssTZD or any other format or level of
            granularity described in W3CDTF. Use RKMS-ISO8601 standard
            for depicting date ranges.
        """

        model_config = ConfigDict(defer_build=True)
        date: List["Resource.Dates.Date"] = field(
            default_factory=list,
            metadata={
                "type": "Element",
            },
        )

        class Date(BaseModel):
            model_config = ConfigDict(defer_build=True)
            value: str = field(
                default="",
                metadata={
                    "required": True,
                },
            )
            date_type: DateType = field(
                metadata={
                    "name": "dateType",
                    "type": "Attribute",
                    "required": True,
                }
            )
            date_information: Optional[object] = field(
                default=None,
                metadata={
                    "name": "dateInformation",
                    "type": "Attribute",
                },
            )

    class AlternateIdentifiers(BaseModel):
        """
        :ivar alternate_identifier: An identifier or identifiers other
            than the primary Identifier applied to the resource being
            registered. This may be any alphanumeric string which is
            unique within its domain of issue. May be used for local
            identifiers. AlternateIdentifier should be used for another
            identifier of the same instance (same location, same file).
        """

        model_config = ConfigDict(defer_build=True)
        alternate_identifier: List[
            "Resource.AlternateIdentifiers.AlternateIdentifier"
        ] = field(
            default_factory=list,
            metadata={
                "name": "alternateIdentifier",
                "type": "Element",
            },
        )

        class AlternateIdentifier(BaseModel):
            model_config = ConfigDict(defer_build=True)
            value: str = field(
                default="",
                metadata={
                    "required": True,
                },
            )
            alternate_identifier_type: object = field(
                metadata={
                    "name": "alternateIdentifierType",
                    "type": "Attribute",
                    "required": True,
                }
            )

    class RelatedIdentifiers(BaseModel):
        """
        :ivar related_identifier: Identifiers of related resources. Use
            this property to indicate subsets of properties, as
            appropriate.
        """

        model_config = ConfigDict(defer_build=True)
        related_identifier: List[
            "Resource.RelatedIdentifiers.RelatedIdentifier"
        ] = field(
            default_factory=list,
            metadata={
                "name": "relatedIdentifier",
                "type": "Element",
            },
        )

        class RelatedIdentifier(BaseModel):
            model_config = ConfigDict(defer_build=True)
            value: str = field(
                default="",
                metadata={
                    "required": True,
                },
            )
            resource_type_general: Optional[ResourceType] = field(
                default=None,
                metadata={
                    "name": "resourceTypeGeneral",
                    "type": "Attribute",
                },
            )
            related_identifier_type: RelatedIdentifierType = field(
                metadata={
                    "name": "relatedIdentifierType",
                    "type": "Attribute",
                    "required": True,
                }
            )
            relation_type: RelationType = field(
                metadata={
                    "name": "relationType",
                    "type": "Attribute",
                    "required": True,
                }
            )
            related_metadata_scheme: Optional[object] = field(
                default=None,
                metadata={
                    "name": "relatedMetadataScheme",
                    "type": "Attribute",
                },
            )
            scheme_uri: Optional[str] = field(
                default=None,
                metadata={
                    "name": "schemeURI",
                    "type": "Attribute",
                },
            )
            scheme_type: Optional[object] = field(
                default=None,
                metadata={
                    "name": "schemeType",
                    "type": "Attribute",
                },
            )

    class Sizes(BaseModel):
        """
        :ivar size: Unstructures size information about the resource.
        """

        model_config = ConfigDict(defer_build=True)
        size: List[str] = field(
            default_factory=list,
            metadata={
                "type": "Element",
            },
        )

    class Formats(BaseModel):
        """
        :ivar format: Technical format of the resource. Use file
            extension or MIME type where possible.
        """

        model_config = ConfigDict(defer_build=True)
        format: List[str] = field(
            default_factory=list,
            metadata={
                "type": "Element",
            },
        )

    class RightsList(BaseModel):
        """
        :ivar rights: Any rights information for this resource. Provide
            a rights management statement for the resource or reference
            a service providing such information. Include embargo
            information if applicable. Use the complete title of a
            license and include version information if applicable.
        """

        model_config = ConfigDict(defer_build=True)
        rights: List["Resource.RightsList.Rights"] = field(
            default_factory=list,
            metadata={
                "type": "Element",
            },
        )

        class Rights(BaseModel):
            model_config = ConfigDict(defer_build=True)
            value: str = field(
                default="",
                metadata={
                    "required": True,
                },
            )
            rights_uri: Optional[str] = field(
                default=None,
                metadata={
                    "name": "rightsURI",
                    "type": "Attribute",
                },
            )
            rights_identifier: Optional[object] = field(
                default=None,
                metadata={
                    "name": "rightsIdentifier",
                    "type": "Attribute",
                },
            )
            rights_identifier_scheme: Optional[object] = field(
                default=None,
                metadata={
                    "name": "rightsIdentifierScheme",
                    "type": "Attribute",
                },
            )
            scheme_uri: Optional[str] = field(
                default=None,
                metadata={
                    "name": "schemeURI",
                    "type": "Attribute",
                },
            )
            lang: Optional[Union[str, LangValue]] = field(
                default=None,
                metadata={
                    "type": "Attribute",
                    "namespace": "http://www.w3.org/XML/1998/namespace",
                },
            )

    class Descriptions(BaseModel):
        """
        :ivar description: All additional information that does not fit
            in any of the other categories. May be used for technical
            information. It is a best practice to supply a description.
        """

        model_config = ConfigDict(defer_build=True)
        description: List["Resource.Descriptions.Description"] = field(
            default_factory=list,
            metadata={
                "type": "Element",
            },
        )

        class Description(BaseModel):
            model_config = ConfigDict(defer_build=True)
            description_type: DescriptionType = field(
                metadata={
                    "name": "descriptionType",
                    "type": "Attribute",
                    "required": True,
                }
            )
            lang: Optional[Union[str, LangValue]] = field(
                default=None,
                metadata={
                    "type": "Attribute",
                    "namespace": "http://www.w3.org/XML/1998/namespace",
                },
            )
            content: List[object] = field(
                default_factory=list,
                metadata={
                    "type": "Wildcard",
                    "namespace": "##any",
                    "mixed": True,
                    "choices": (
                        {
                            "name": "br",
                            "type": object,
                        },
                    ),
                },
            )

    class GeoLocations(BaseModel):
        model_config = ConfigDict(defer_build=True)
        geo_location: List["Resource.GeoLocations.GeoLocation"] = field(
            default_factory=list,
            metadata={
                "name": "geoLocation",
                "type": "Element",
            },
        )

        class GeoLocation(BaseModel):
            """
            :ivar geo_location_place: Spatial region or named place
                where the data was gathered or about which the data is
                focused.
            :ivar geo_location_point: A point contains a single
                latitude-longitude pair.
            :ivar geo_location_box: A box contains two white space
                separated latitude-longitude pairs, with each pair
                separated by whitespace. The first pair is the lower
                corner, the second is the upper corner.
            :ivar geo_location_polygon: A drawn polygon area, defined by
                a set of points and lines connecting the points in a
                closed chain.
            """

            model_config = ConfigDict(defer_build=True)
            geo_location_place: List[object] = field(
                default_factory=list,
                metadata={
                    "name": "geoLocationPlace",
                    "type": "Element",
                },
            )
            geo_location_point: List[Point] = field(
                default_factory=list,
                metadata={
                    "name": "geoLocationPoint",
                    "type": "Element",
                },
            )
            geo_location_box: List[Box] = field(
                default_factory=list,
                metadata={
                    "name": "geoLocationBox",
                    "type": "Element",
                },
            )
            geo_location_polygon: List[
                "Resource.GeoLocations.GeoLocation.GeoLocationPolygon"
            ] = field(
                default_factory=list,
                metadata={
                    "name": "geoLocationPolygon",
                    "type": "Element",
                },
            )

            class GeoLocationPolygon(BaseModel):
                model_config = ConfigDict(defer_build=True)
                polygon_point: List[Point] = field(
                    default_factory=list,
                    metadata={
                        "name": "polygonPoint",
                        "type": "Element",
                        "min_occurs": 4,
                    },
                )
                in_polygon_point: Optional[Point] = field(
                    default=None,
                    metadata={
                        "name": "inPolygonPoint",
                        "type": "Element",
                    },
                )

    class FundingReferences(BaseModel):
        """
        :ivar funding_reference: Information about financial support
            (funding) for the resource being registered.
        """

        model_config = ConfigDict(defer_build=True)
        funding_reference: List[
            "Resource.FundingReferences.FundingReference"
        ] = field(
            default_factory=list,
            metadata={
                "name": "fundingReference",
                "type": "Element",
            },
        )

        class FundingReference(BaseModel):
            """
            :ivar funder_name: Name of the funding provider.
            :ivar funder_identifier: Uniquely identifies a funding
                entity, according to various types.
            :ivar award_number: The code assigned by the funder to a
                sponsored award (grant).
            :ivar award_title: The human readable title of the award
                (grant).
            """

            model_config = ConfigDict(defer_build=True)
            funder_name: str = field(
                metadata={
                    "name": "funderName",
                    "type": "Element",
                    "required": True,
                    "min_length": 1,
                }
            )
            funder_identifier: Optional[
                "Resource.FundingReferences.FundingReference.FunderIdentifier"
            ] = field(
                default=None,
                metadata={
                    "name": "funderIdentifier",
                    "type": "Element",
                },
            )
            award_number: Optional[
                "Resource.FundingReferences.FundingReference.AwardNumber"
            ] = field(
                default=None,
                metadata={
                    "name": "awardNumber",
                    "type": "Element",
                },
            )
            award_title: Optional[object] = field(
                default=None,
                metadata={
                    "name": "awardTitle",
                    "type": "Element",
                },
            )

            class FunderIdentifier(BaseModel):
                model_config = ConfigDict(defer_build=True)
                value: str = field(
                    default="",
                    metadata={
                        "required": True,
                    },
                )
                funder_identifier_type: FunderIdentifierType = field(
                    metadata={
                        "name": "funderIdentifierType",
                        "type": "Attribute",
                        "required": True,
                    }
                )
                scheme_uri: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "schemeURI",
                        "type": "Attribute",
                    },
                )

            class AwardNumber(BaseModel):
                model_config = ConfigDict(defer_build=True)
                value: str = field(
                    default="",
                    metadata={
                        "required": True,
                    },
                )
                award_uri: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "awardURI",
                        "type": "Attribute",
                    },
                )

    class RelatedItems(BaseModel):
        """
        :ivar related_item: Information about a resource related to the
            one being registered e.g. a journal or book of which the
            article or chapter is part.
        """

        model_config = ConfigDict(defer_build=True)
        related_item: List["Resource.RelatedItems.RelatedItem"] = field(
            default_factory=list,
            metadata={
                "name": "relatedItem",
                "type": "Element",
            },
        )

        class RelatedItem(BaseModel):
            """
            :ivar related_item_identifier: The identifier for the
                related item.
            :ivar creators:
            :ivar titles:
            :ivar publication_year: The year when the item was or will
                be made publicly available.
            :ivar volume: Volume of the related item.
            :ivar issue: Issue number or name of the related item.
            :ivar number: Number of the related item e.g. report number
                of article number.
            :ivar first_page: First page of the related item e.g. of the
                chapter, article, or conference paper.
            :ivar last_page: Last page of the related item e.g. of the
                chapter, article, or conference paper.
            :ivar publisher: The name of the entity that holds,
                archives, publishes prints, distributes, releases,
                issues, or produces the resource. This property will be
                used to formulate the citation, so consider the
                prominence of the role.
            :ivar edition: Edition or version of the related item.
            :ivar contributors:
            :ivar related_item_type: The type of the related item, e.g.
                journal article, book or chapter.
            :ivar relation_type: Description of the relationship of the
                resource being registered (A) and the related resource
                (B).
            """

            model_config = ConfigDict(defer_build=True)
            related_item_identifier: Optional[
                "Resource.RelatedItems.RelatedItem.RelatedItemIdentifier"
            ] = field(
                default=None,
                metadata={
                    "name": "relatedItemIdentifier",
                    "type": "Element",
                },
            )
            creators: Optional[
                "Resource.RelatedItems.RelatedItem.Creators"
            ] = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )
            titles: Optional["Resource.RelatedItems.RelatedItem.Titles"] = (
                field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
                )
            )
            publication_year: Optional[str] = field(
                default=None,
                metadata={
                    "name": "publicationYear",
                    "type": "Element",
                    "pattern": r"[\d]{4}",
                },
            )
            volume: Optional[object] = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )
            issue: Optional[object] = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )
            number: Optional["Resource.RelatedItems.RelatedItem.Number"] = (
                field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
                )
            )
            first_page: Optional[object] = field(
                default=None,
                metadata={
                    "name": "firstPage",
                    "type": "Element",
                },
            )
            last_page: Optional[object] = field(
                default=None,
                metadata={
                    "name": "lastPage",
                    "type": "Element",
                },
            )
            publisher: Optional[object] = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )
            edition: Optional[object] = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )
            contributors: Optional[
                "Resource.RelatedItems.RelatedItem.Contributors"
            ] = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )
            related_item_type: ResourceType = field(
                metadata={
                    "name": "relatedItemType",
                    "type": "Attribute",
                    "required": True,
                }
            )
            relation_type: RelationType = field(
                metadata={
                    "name": "relationType",
                    "type": "Attribute",
                    "required": True,
                }
            )

            class RelatedItemIdentifier(BaseModel):
                """
                :ivar value:
                :ivar related_item_identifier_type: The type of the
                    Identifier for the related item e.g. DOI.
                :ivar related_metadata_scheme: The name of the scheme.
                :ivar scheme_uri: The URI of the relatedMetadataScheme.
                :ivar scheme_type: The type of the
                    relatedMetadataScheme, linked with the schemeURI.
                """

                model_config = ConfigDict(defer_build=True)
                value: str = field(
                    default="",
                    metadata={
                        "required": True,
                    },
                )
                related_item_identifier_type: Optional[
                    RelatedIdentifierType
                ] = field(
                    default=None,
                    metadata={
                        "name": "relatedItemIdentifierType",
                        "type": "Attribute",
                    },
                )
                related_metadata_scheme: Optional[object] = field(
                    default=None,
                    metadata={
                        "name": "relatedMetadataScheme",
                        "type": "Attribute",
                    },
                )
                scheme_uri: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "schemeURI",
                        "type": "Attribute",
                    },
                )
                scheme_type: Optional[object] = field(
                    default=None,
                    metadata={
                        "name": "schemeType",
                        "type": "Attribute",
                    },
                )

            class Creators(BaseModel):
                """
                :ivar creator: The institution or person responsible for
                    creating the related resource. To supply multiple
                    creators, repeat this property.
                """

                model_config = ConfigDict(defer_build=True)
                creator: List[
                    "Resource.RelatedItems.RelatedItem.Creators.Creator"
                ] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                    },
                )

                class Creator(BaseModel):
                    model_config = ConfigDict(defer_build=True)
                    creator_name: "Resource.RelatedItems.RelatedItem.Creators.Creator.CreatorName" = field(
                        metadata={
                            "name": "creatorName",
                            "type": "Element",
                            "required": True,
                        }
                    )
                    given_name: Optional[object] = field(
                        default=None,
                        metadata={
                            "name": "givenName",
                            "type": "Element",
                        },
                    )
                    family_name: Optional[object] = field(
                        default=None,
                        metadata={
                            "name": "familyName",
                            "type": "Element",
                        },
                    )

                    class CreatorName(BaseModel):
                        model_config = ConfigDict(defer_build=True)
                        value: str = field(
                            default="",
                            metadata={
                                "required": True,
                            },
                        )
                        name_type: Optional[NameType] = field(
                            default=None,
                            metadata={
                                "name": "nameType",
                                "type": "Attribute",
                            },
                        )
                        lang: Optional[Union[str, LangValue]] = field(
                            default=None,
                            metadata={
                                "type": "Attribute",
                                "namespace": "http://www.w3.org/XML/1998/namespace",
                            },
                        )

            class Titles(BaseModel):
                """
                :ivar title: Title of the related item.
                """

                model_config = ConfigDict(defer_build=True)
                title: List[
                    "Resource.RelatedItems.RelatedItem.Titles.Title"
                ] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                    },
                )

                class Title(BaseModel):
                    model_config = ConfigDict(defer_build=True)
                    value: str = field(
                        default="",
                        metadata={
                            "required": True,
                        },
                    )
                    title_type: Optional[TitleType] = field(
                        default=None,
                        metadata={
                            "name": "titleType",
                            "type": "Attribute",
                        },
                    )
                    lang: Optional[Union[str, LangValue]] = field(
                        default=None,
                        metadata={
                            "type": "Attribute",
                            "namespace": "http://www.w3.org/XML/1998/namespace",
                        },
                    )

            class Number(BaseModel):
                model_config = ConfigDict(defer_build=True)
                value: str = field(
                    default="",
                    metadata={
                        "required": True,
                    },
                )
                number_type: Optional[NumberType] = field(
                    default=None,
                    metadata={
                        "name": "numberType",
                        "type": "Attribute",
                    },
                )

            class Contributors(BaseModel):
                """
                :ivar contributor: The institution or person responsible
                    for collecting, managing, distributing, or otherwise
                    contributing to the development of the resource.
                """

                model_config = ConfigDict(defer_build=True)
                contributor: List[
                    "Resource.RelatedItems.RelatedItem.Contributors.Contributor"
                ] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                    },
                )

                class Contributor(BaseModel):
                    """
                    :ivar contributor_name:
                    :ivar given_name:
                    :ivar family_name:
                    :ivar contributor_type: The type of contributor of
                        the resource.
                    """

                    model_config = ConfigDict(defer_build=True)
                    contributor_name: "Resource.RelatedItems.RelatedItem.Contributors.Contributor.ContributorName" = field(
                        metadata={
                            "name": "contributorName",
                            "type": "Element",
                            "required": True,
                        }
                    )
                    given_name: Optional[object] = field(
                        default=None,
                        metadata={
                            "name": "givenName",
                            "type": "Element",
                        },
                    )
                    family_name: Optional[object] = field(
                        default=None,
                        metadata={
                            "name": "familyName",
                            "type": "Element",
                        },
                    )
                    contributor_type: ContributorType = field(
                        metadata={
                            "name": "contributorType",
                            "type": "Attribute",
                            "required": True,
                        }
                    )

                    class ContributorName(BaseModel):
                        model_config = ConfigDict(defer_build=True)
                        value: str = field(
                            default="",
                            metadata={
                                "required": True,
                            },
                        )
                        name_type: Optional[NameType] = field(
                            default=None,
                            metadata={
                                "name": "nameType",
                                "type": "Attribute",
                            },
                        )
                        lang: Optional[Union[str, LangValue]] = field(
                            default=None,
                            metadata={
                                "type": "Attribute",
                                "namespace": "http://www.w3.org/XML/1998/namespace",
                            },
                        )
