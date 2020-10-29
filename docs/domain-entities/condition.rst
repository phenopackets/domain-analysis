Condition, diagnosis, etc.
====================================

This entity represents the usual sense of a clinical diagnosis, a patient having a condition that requires medical care, etc. The line between a phenotype and a diagnosis is not always clear. However, FHIR does provide some guidance and this entity is meant to be aligned with FHIR's definition of `the Condition resource <https://www.hl7.org/fhir/condition.html>`_.

The first two sections of the FHIR documentation for Condition (`scope <https://www.hl7.org/fhir/condition.html#scope>`_ and `boundaries <https://www.hl7.org/fhir/condition.html#bnr>`_)provides a good overview of Condition vs other similar FHIR resources and we will adopt that analysis here.

In addition to the FHIR language to clarify condition vs phenotype, a condition should be considered as a conclusion or inference that is based on some other information or observations, usually simpler or more granular. Practitioners in the domain are intuitively aware these distinctions and act accordingly even if our written definitions give the impression that there is no clear boundaries between a phenotype and a condition. For example, if we only have a fact that there is a low body temperature, is this a medical condition that needs attention or is it just a simple phenotype of a body? In clinical practice it is a medical emergency that needs immediate treatment but during an autopsy it is just a characteristic of the body that needs no intervention but the fact can still be used to make other inferences that are still clinically relevant such as time of death. So, in this case, the first scenario the low body temperature is a hypothermia condition but in the latter case it would be in appropriate to make that inference. The hypothermia condition, in addition to needing to have a phenotype of low body temperature, also implies that there is an expect body temperature, the patient is alive, and the hypothermia assertion is made by a qualified practitioner as opposed to an informal inference by any other type of observer.

Also, this page is not primarily focused on documents, reporting, etc. It is focused on the underlying meaning and structure of the various entities referenced in such reports and documents.

**GitHub issue**: `ISSUE <https://github.com/phenopackets/domain-analysis/issues/17>`_

Phenopackets representation
++++++++++++++++++++++++++++++

It is represented by `the Disease entity <https://phenopackets-schema.readthedocs.io/en/latest/disease.html>`_. It is focused on capturing the coded type of the condition, onset in the form of an age related quantity or a coded value for an onset category, and staging related information. There are two dedicated fields for staging like information. The "disease_stage" appears to be general and can be used for any disease as long as there is some coded staging for it, and a "tnm_finding" that is specifically for tumor related stating. The documentation page gives further guidance for these fields, how they should be used, and suggest a subset of NCIT codes for each field.

In the Phenopackets `schema diagram <https://phenopackets-schema.readthedocs.io/en/latest/schema.html>`_  and in `the Interpretation top level element <https://phenopackets-schema.readthedocs.io/en/latest/interpretation.html>`_ there is a sense of a higher level interpretation in addition to the Disease modeling. This seems to be dedicated to a genomics analysis interpretation, not a general overall interpretation of what's in a phenopackets instance. 

The Interpretation model also nests `a Diagnosis entity <https://phenopackets-schema.readthedocs.io/en/latest/interpretation.html#rstdiagnosis>`_ that appears to capture a relationship between a Disease and a `GenomicInterpretation <https://phenopackets-schema.readthedocs.io/en/latest/interpretation.html#genomicinterpretation>`_, which is another nested Entity within Interpretation. There is also a `GenomicInterpretation Status enumeration <https://phenopackets-schema.readthedocs.io/en/latest/interpretation.html#genomicinterpretation-status>`_ within Interpretation.

FHIR representation
+++++++++++++++++++++

The basic sense of a condition or diagnosis is represented with `the Condition resource <https://www.hl7.org/fhir/condition.html>`_. FHIR Condition provides modeling to capture all of the issues described above for Phenopackets Disease. It also has a .staging complex structure that allows for multiple yet distinct entries for stating related information. It is also able to capture severity, related body sites, etc.  It also has `a .onset[x] field <https://www.hl7.org/fhir/condition-definitions.html#Condition.onset_x_>`_ that allows for Age (i.e. Quantity) and Range values (in addition to few other value types) to specify the onset. However, it does not allow for a coded type of onset, i.e. no onsetCodableConcept.

Further discussion of Phenopackets modeling of Disease, Diagnosis, Interpretation is needed but with a superficial understanding of those Phenopackets entities, it appease that some aspects of those Phenopackets entities can be subsumed by FHIR Condition or ClinicalImpression. There is also the DiagnosticReport resource if a more formal document like model with an author is needed.

It appears that we will need to perform some significant amount of analysis here that will clarify and align the relevant parts of Phenopackets and FHIR to cover this aspect of the domain. It is also likely that we will be able to generalize the Phenopackets representation in a way that will make it easier to reuse the idea of an Interpretation, Diagnosis, etc. in a way that is not so closely tied or constrained to genomics.  :TODO:move this language to some other part of this page.

Phenopackets IG representation
++++++++++++++++++++++++++++++++

It models Phenopackets Disease with a FHIR Condition as `can be seen here <https://aehrc.github.io/fhir-phenopackets-ig/StructureDefinition-Disease.html>`_. It also provides two extensions to capture coded onset and tumor staging, i.e. the Phenopackets Disease.tnm_finding field.

It models Phenopackets Interpretation, `as seen here <https://aehrc.github.io/fhir-phenopackets-ig/StructureDefinition-Interpretation.html>`_, `as a GenomicsReport <http://hl7.org/fhir/uv/genomics-reporting/STU1/genomics-report.html>`_ from the `Genomics Reporting IG <http://hl7.org/fhir/uv/genomics-reporting/STU1/index.html>`_, which in turn is based on `FHIR DiagnosticReport <https://hl7.org/fhir/diagnosticreport.html>`_.

We still need to explore how this IG captures the other Phenopackets Interpretation related modeling described above. :TODO:

Proposed Core IG representation
+++++++++++++++++++++++++++++++++

We will model the disease/condition part of the above analysis with a FHIR Condition. Also:

- All staging related information will be modeled with the built in Condition.stage complex structure.
- Onset with be captured with Conditin.onset[x]
  - If a coded onset is needed we'll use an Observation over the Condition instance to capture that information. In this case, it is likely that the Observation can be used as Condition.evidence. For example, for a type 1 diabetes condition instance, it would be possible to have an Observation of a coded onset value and have that Observation be a Condition.evidence for the diagnosis of type 1 diabetes. We'll have to see if this can not be done consistently.
- We will need to develop ValueSet resources to represent or subsume the Phenopackets Disease recommendation for terminology bindings.

The other aspects of Phenopackets described in this page are pending further analysis but the FHIR Condition resource is a basic building block towards capturing the overall Phenopackets modeling of this part of the domain. The ClinicalImpression resource is another closely related model that needs further analysis along with the Phenopackets modeling.

A tentative thought is that we should stay away from the idea of capturing information in this Core IG in document like FHIR resources. Other downstream IGs can implement this use case, or we can prototype few types of documents in this Core IG if needed. However, basic facts, relationship, information objects, etc. should not be directly or primarily be captured in a document like FHIR resource. The Core IG should be focused on A FHIR information graph rather than also embedding parts of that graph in documents.
