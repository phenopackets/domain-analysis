Clinical impression
==============================

This is an entity related to a high level clinical assessment and workflow/summary. It is distinct from but closely related to the more granular observations, diagnoses, investigations entities.

FHIR does a fairly good job defining and modeling this entity with `the ClinicalImpression resource <https://www.hl7.org/fhir/clinicalimpression.html>`_.

The FHIR ClinicalImpression model is good knowledge to keep in mind while we go through the analysis and modeling of the smaller supporting entities. However, a full analysis and modeling of this domain entity is premature at this point, and not clearly needed by year 1 use cases, so it will be deferred until it is clearly needed and we have resolved and implemented most of the other supporting entities needed for this entity.

There are aspects of the Phenopackets schema modeling that can be refactored into the FHIR ClinicalImpression resource, or the other FHIR related resources referenced by ClinicalImpression. This could be a year 2 analysis topic, or it can also be left to downstream IGs to model along with any reporting or document modeling. The Core IG can focus on providing a well defined set of building blocks for those downstream IGs.

**GitHub issue**: `ISSUE <https://github.com/phenopackets/domain-analysis/issues/16>`_

Phenopackets representation
++++++++++++++++++++++++++++++

Discuss...

FHIR representation
+++++++++++++++++++++

Discuss...

Phenopackets IG representation
++++++++++++++++++++++++++++++++

Discuss....

Proposed Core IG representation
+++++++++++++++++++++++++++++++++

Discuss...
