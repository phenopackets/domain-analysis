Phenopacket
==============================

This page is for the analysis of a phenopacket. The term *phenopacket* here means an instance of the Phenopackets graph shown `here <https://phenopackets-schema.readthedocs.io/en/latest/_images/phenopacket-schema-v1.svg>`_ and further defined `here <https://phenopackets-schema.readthedocs.io/en/latest/phenopacket.html>`_

What is the context of a phenopacket? What does it mean to extract or submit a phenopacket from/to an EHR? Everything in an EHR is usually linked to some provider, on a specific date, during an encounter, asserted by a provider, etc. All this context is missing from the Phenopackets schema. How can this context be made up for or ignored in an EHR? Intuitively, it's not likely to be able to *enter* a phenopacket into an EHR without it being attested to by a provider, during an encounter, etc.  Also, the various components of a phenopacket as defined by the Phenopackets schema are likely to be instantiated multiple times, even in duplicate, in an EHR during various encounters for the same patient and same clinical conditions. Also, the set of instantiated parts of the phenopacket schema might vary from one encounter to another. For example, provider x on date y might say a patient has phenopacket instance p1 but on another date have a different combination of instances to form phenopacket p2. How will all this be mappable to the simpler use of Phenopackets outside the context of EHR, providers, visits, purpose, etc.? 

**GitHub issue**: `issue <https://github.com/phenopackets/domain-analysis/issues/12>`_

Phenopackets representation
++++++++++++++++++++++++++++++

Discuss...

FHIR representation
+++++++++++++++++++++

There are multiple options to group FHIR resources in FHIR. Please be familiar with the nitty gritty details of `Bundle <https://www.hl7.org/fhir/bundle.html>`_ and `Composition <https://www.hl7.org/fhir/composition.html>`_, and to a lesser degree with `Linkage <https://www.hl7.org/fhir/linkage.html>`_, `List <https://www.hl7.org/fhir/list.html>`_, before discussing FHIR options for representing Phenopackets' meaning of a phenopacket. There are few other relevant FHIR resources but the above are a good starting point.

Phenopackets IG representation
++++++++++++++++++++++++++++++++

This IG represents a phenopacket as FHIR Composition but this might not be the best choice based on the spec language for that resource. Specific justification with citations for not doing this will be added here shortly. A FHIR Bundle might be a more appropriate container but this is pending on clarifying what a phenopacket instances should stand for inside and outside an EHR, and have some of the questions at the beginning of this page answered.

Proposed Core IG representation
+++++++++++++++++++++++++++++++++

Discuss...