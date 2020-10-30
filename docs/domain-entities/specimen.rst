Specimen
==============================

Both driver use cases have a need to represent a specimen of type blood, the specific analyte, and possibly a tissue type or specimen type qualifier. 

**GitHub issue**: `ISSUE <https://github.com/phenopackets/domain-analysis/issues/21>`_

Phenopackets representation
++++++++++++++++++++++++++++++

Phenopackets models this with `the Biosample entity <https://phenopackets-schema.readthedocs.io/en/latest/biosample.html>`_. Its definition is focused on molecular analysis of an extracted analyte/substrate. 

FHIR representation
+++++++++++++++++++++

FHIR models this with `the Specimen resource <https://www.hl7.org/fhir/specimen.html>`_. 

Phenopackets IG representation
++++++++++++++++++++++++++++++++

Creates `a FHIR Specimen profile <https://aehrc.github.io/fhir-phenopackets-ig/StructureDefinition-Biosample.html>`_ and adds several extensions to capture related clinical facts (as modeled in Phenopackets) as extensions on Specimen.

Proposed Core IG representation
+++++++++++++++++++++++++++++++++

This analysis is still incomplete but it is likely that this can be captured with a combination of FHIR Specimen, along with references to related Condition, Observation, etc., to refactor the various aspects of the Phenopackets Biosample entity instead of needing the many custom extensions. For our driver use cases for year 1 we will not need these clinical aspects of Phenopackets Biosample so the mapping in this case will only involve profiling Observation. Other aspects will be dealt with as they arise in use cases.