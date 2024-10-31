[![License](https://img.shields.io/badge/LICENSE-GPL3.0-blue)](https://www.gnu.org/licenses/gpl-3.0.en.html)
[![Python](https://img.shields.io/badge/python-3.11%20%7C%203.12-green)](https://www.gnu.org/licenses/gpl-3.0.en.html)
[![Tests](https://gitlab.switch.ch/eaw-rdm/ckool/badges/main/pipeline.svg)](https://gitlab.switch.ch/eaw-rdm/ckool/-/commits/main)

# Datacite-Schema

This library's code is dynamically generated using `xsdata-pydantic` and the official datacite schema definition.
The generated code is verified via the provided datacite schema examples.

To add the support for a version to this library you can generate the code like this:

```bash
export DCS_VERSION=4.4
xsdata "http://schema.datacite.org/meta/kernel-DCS_VERSION/metadata.xsd" --output pydantic --package "src.datacite_schema.schema$DCS_VERSION" 
```

## Warning
The datacite XML schema does not map one to one to the JSON data used in their rest API. For future development on this converter, it may be better to use `xsdata` rather than `xsdata-pydantic`.