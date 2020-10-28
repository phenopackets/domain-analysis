Sex
==============================

PP Definition: Observed (phenotypic) apparent sex of the individual.

**GitHub issue**: `ISSUE <https://github.com/phenopackets/domain-analysis/issues/9>`_

Phenopackets representation
++++++++++++++++++++++++++++++

Phenopackets captures Sex as an attribute on Individual and provides a value set for permissible values. The description specifies this is an observation rather than a self-reported value.


FHIR representation
+++++++++++++++++++++

FHIR provides a field for gender, with an associated value set for Administrative Gender.  It should be noted that the concept of sex is distinct from that of gender, as the former is physiological and the latter describes self-identified behaviors and roles.  FHIR does not support the concept of sex in FHIR 4.0.1.

Phenopackets IG representation
++++++++++++++++++++++++++++++++

The IG appears to map the concept of Sex to FHIR Patient.gender. FHIR has the same values in the required ValueSet as Phenopackets has.

Proposed Core IG representation
+++++++++++++++++++++++++++++++++

FHIR suggests either an extension, as provided by US Core, or an Observation instance for capturing this apparent sex in a clinical setting as opposed to an administrative settings. See `this language <https://docs.google.com/document/d/1EVzNmeWuCGl7G3Gk535pTqzSdo356Ci9GlZ3nHiAuM0/edit?disco=AAAAHDSTPtk>`_  The extension approach is limited compared to an observation asserted by a provider or a Patient in a specific context. Capturing it as an extension is straightforward if there are on doubts clinically but for situations where the assignment is difficult, or later medical care is necessary to determine it, Observation instances become more appropriate. It is also possible to represent it both ways. The extension on Patient holds the same value as the latest Observation of this feature.