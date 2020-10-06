Individual
==============================

This is an individual person in the domain independent of any role in any clinical or research setting.

**GitHub issue**: `issue 7 <https://github.com/phenopackets/domain-analysis/issues/7>`_

Phenopackets representation
++++++++++++++++++++++++++++++

The Phenopackets specification uses `Individual <https://docs.google.com/document/d/1LkfS7RnqMCXRiioX7hy8ZVVcXtbnDJcinGxtEfYIZBI/edit#heading=h.hs17po7371ca>`_ to represent a patient (the proband of the Phenopacket), but similar concepts within the specification are used to represent people in other ways. The model for this element is not focused on capturing encounters, providers, etc. and there is more focus on person to person relationships to aid interpretation of genetic data. `This language <https://docs.google.com/document/d/1LkfS7RnqMCXRiioX7hy8ZVVcXtbnDJcinGxtEfYIZBI/edit?disco=AAAAKVBBS3E>`_ supports this interpretation and the attributes also support this structure.

FHIR representation
+++++++++++++++++++++

FHIR represents the concept of individuals in many ways. The core Patient resource entity represents the role of a person as a patient in a healthcare organization, rather than representing an individual. The language that supports this interpretation is `here <https://docs.google.com/document/d/1EVzNmeWuCGl7G3Gk535pTqzSdo356Ci9GlZ3nHiAuM0/edit?disco=AAAAHDCXnWk>`_, `here <https://docs.google.com/document/d/1EVzNmeWuCGl7G3Gk535pTqzSdo356Ci9GlZ3nHiAuM0/edit?disco=AAAAHDCXnWo>`_ and few other places in the Patient documentation page.

FHIR also has a resource that represents `Person <https://docs.google.com/document/d/1mkEU5A4KLSFOLvlplHl47IW_nI-LGUtU3BJOfENzCEY/edit>`_, which is meant to be a role-neutral representation of an individual. See also `RelatedPerson <https://docs.google.com/document/d/11M-PLnnT2tYgy5AbVCWx58ZWc-0P879SqM8FhqSvHpw/edit>`_, although that resource is likely less relevant to this specification.

Phenopackets IG representation
++++++++++++++++++++++++++++++++

This IG maps a PP Individual to a `FHIR Patient <https://docs.google.com/document/d/1oYeBFgSH_HEI6S0icoiG1xvGZW-jm6UU3WTvXFU5qXs/edit>`_

Proposed Core IG representation
+++++++++++++++++++++++++++++++++

A Phenopacket "Individual" should be primarily mapped to a FHIR Person. If there is a need to also capture the Phenopacket’s instance in the context of a FHIR Patient because all the information is related to a specific Patient instance in a specific setting, then a FHIR Patient instance should also be created for this purpose. However, the primary mapping is to a FHIR Person as the representation of existence of the Individual in the world. Also, however, FHIR’s main “integration” point for most or all FHIR instances is the Patient resource so it’s almost a requirement to also instantiate a Patient to be able to capture other information with the existing FHIR resources. We should follow the guidelines described in the Patient and Person FHIR documentation pages and instantiate one or both as needed based on what other information we need to attach to them. See further discussion below.
