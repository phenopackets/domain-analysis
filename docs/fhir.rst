=================
HL7 FHIR
=================

The HL7 FHIR specification was mostly developed for clinical systems and is heavily focused on established clinical workflows. It is not as well developed for the research domain, or for capturing more granular clinical facts such as phenotypic level information. However, FHIR does have some foundational building blocks that could be extended (with FHIR extensions) or could be further developed to accommodate both of these areas. The analysis of FHIR to represent detailed clinical phenotypes and related data will be focused on two main areas.

--------------------
FHIR representation
--------------------
The analysis will examine and document how the FHIR framework represents clinical phenotypic information and related data, including which FHIR resources are most applicable to the representation of those data.  Particular attention will be paid to identifying gaps in the FHIR specification that need to be addressed to better support our use cases.

-----------------------
Phenopackets mapping
-----------------------
This part of the FHIR analysis will specify in detail how the Phenopackets schema maps to FHIR resources. This process will provide the mappings needed for technical development and implementation of a FHIR IG, but it will also help identity possible enhancements to the FHIR and Phenopackets specifications to bring them into better alignment in how they represent the underlying domain entities.


