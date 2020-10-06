Identifier and identity
==============================

Identifiers are a critical part of linking an information system to entities in the real world that the information system is intended to capture. Identifiers are also needed for the information system itself to be able to link the various information objects with each other to maintain the information graph.  These two types of identification are very different. FHIR has a good discussion of this issue `here <https://docs.google.com/document/d/1KN87im3Ei92sNxRX5nZ_qIl4mh12B0k8RindX3Y0uWI/edit?disco=AAAAKVBBS3U>`_ and `here <https://docs.google.com/document/d/1KN87im3Ei92sNxRX5nZ_qIl4mh12B0k8RindX3Y0uWI/edit?disco=AAAAKVBBS3Y>`_



**GitHub issue**: `issue <https://github.com/phenopackets/domain-analysis/issues/8>`_

Phenopackets representation
++++++++++++++++++++++++++++++

Phenopackets describes identifiers in several places, including `here <https://docs.google.com/document/d/1LkfS7RnqMCXRiioX7hy8ZVVcXtbnDJcinGxtEfYIZBI/edit?disco=AAAAKVIEyKU>`_, `here <https://docs.google.com/document/d/1LkfS7RnqMCXRiioX7hy8ZVVcXtbnDJcinGxtEfYIZBI/edit?disco=AAAAKVIEyKY>`_, `here <https://docs.google.com/document/d/1jwYBm30g3wpBM8_gLcCWU2p03BBMAtaGyqsb42hRixo/edit?disco=AAAAKVIEyLI>`_, and `here <https://docs.google.com/document/d/1jwYBm30g3wpBM8_gLcCWU2p03BBMAtaGyqsb42hRixo/edit?disco=AAAAKVIEyLQ>`_.  Identifiers are used in Phenopackets to define object identity and as cross-references defined by external systems. Phenopackets also uses identifiers as foreign keys to other parts of a Phenopackets message, maintaining links between objects, rather than as true domain business identifiers.  Phenopackets also defines the `alternate_ids field <https://docs.google.com/document/d/1LkfS7RnqMCXRiioX7hy8ZVVcXtbnDJcinGxtEfYIZBI/edit?disco=AAAAKVIEyKY>`_, appears to be more of a business identifier, or is able to accommodate that function to some degree.

Within the PP Individual structure, the id field is defined as "the primary identifier for the individual and SHOULD be used in other parts of a message when referring to this individual - for example in a Pedigree or Biosample. The contents of the element are context dependent, and will be determined by the application."

The type of the identifier attribute is "string", with no limitations on length or character set.


FHIR representation
+++++++++++++++++++++

FHIR models logical or resource instance identity with `the “id” field <https://docs.google.com/document/d/1KN87im3Ei92sNxRX5nZ_qIl4mh12B0k8RindX3Y0uWI/edit?disco=AAAAKVBBS3c>`_.   The value of this id field is a simple type, i.e. a `simple string value with some limitations <https://docs.google.com/document/d/1fi53GQuGGpSsPXjiupGzr6DVL07Fg_iTGfVrIH5LIKw/edit?disco=AAAAKVBBS3g>`_.

Identifiers for business identifiers are represented with the `Identifier data type <https://docs.google.com/document/d/1m2E4ueImkF2Qu2gfmql6nEn8EKmQjGoS5VGOEX_89zM/edit>`_ and usually the `“identifier” field <https://docs.google.com/document/d/1EVzNmeWuCGl7G3Gk535pTqzSdo356Ci9GlZ3nHiAuM0/edit?disco=AAAAHDCmD50>`_ holds instances of that data type. The identifier field is used on various resources that are likely to have a business identity, where the "system" attribute . It is not available on all resources the way the “id” field is.  The Identifier data type captures not only the value of an identifier, but also the system or namespace that assigned the identifier and its type and intended use.  Therefore, this datatype is an elegant approach to encapsulating relevant metadata related to an identifier so that a consuming system can computationally determine how it might be used.

The type of the Identifier.value field is "string", but FHIR restricts the value of strings by length (1024x1024 characters) and content (Unicode, with restrictions).

 This is similar to the `FHIR logical id field <https://docs.google.com/document/d/1KN87im3Ei92sNxRX5nZ_qIl4mh12B0k8RindX3Y0uWI/edit?disco=AAAAKVBBS3c>`_ and it also matches the simple string based representation of this value

Phenopackets IG representation
++++++++++++++++++++++++++++++++

The IG doesn’t clearly describe how the PP are mapped. However, it does add a “must support” to the FHIR identifier field.

Proposed Core IG representation
+++++++++++++++++++++++++++++++++

The PP Individual.id attribute is mappable to the FHIR id type.  However, because PP places heavy emphasis on the context and business use of this value, the Identifier type (which captures system, type, and use) is more appropriate.  The Identifier type would also better support the use of multiple identifiers for an Individual, and its use is more consistent with FHIR recommendations.  Furthermore, the use of Identifier allows for preserving object identities when objects are moved between systems and the message-specific “logical id” is lost. The language supporting this is `here <https://docs.google.com/document/d/1RX7uFn-ioEK6LglVmothCBz0FwMrNYjJMs-6rm-WHVU/edit?disco=AAAAKVIEyNA>`_.

The alternative identifier has to be captured in the FHIR identifier field whenever possible to be consistent with identity representation in FHIR.

Giving a set of alternative identifiers in some phenopackets instance, the identifiers could clarify which FHIR resources to instantiate for a PP Individual. For example, if one of those alternate identifiers is a medical record number, this clearly implies some FHIR Patient aspect to the phenopacket. However, if one of the identifiers is a SSN, or something like that, this implies a FHIR Person aspect to the PP instance. An identifier that is not clearly related to a Patient role/context should canonically be mapped to a Person instance. However, it is also possible to duplicate the representation of this identifier on the Patient instance as well if and when needed. FHIR provides guidelines for how to update information between the different FHIR resources that represent people in the world and their role specific instances, `here <https://docs.google.com/document/d/1mkEU5A4KLSFOLvlplHl47IW_nI-LGUtU3BJOfENzCEY/edit?disco=AAAAKVIZlQY>`_, `here <https://docs.google.com/document/d/1mkEU5A4KLSFOLvlplHl47IW_nI-LGUtU3BJOfENzCEY/edit?disco=AAAAKVIZlQg>`_, etc.