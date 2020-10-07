Karyotypic sex
==============================

Karyotypic sex (KS) is the determination of sex chromosomes in an individual.

**GitHub issue**: place a link to the created GH issue for discussion like this:  `issue <https://github.com/phenopackets/domain-analysis/issues/7>`_

Phenopackets representation
++++++++++++++++++++++++++++++

Phenopackets captures KS as an `attribute on Individual <https://docs.google.com/document/d/1LkfS7RnqMCXRiioX7hy8ZVVcXtbnDJcinGxtEfYIZBI/edit?disco=AAAAKVAMNQc>`_ and provides a `value set for permissible values <https://docs.google.com/document/d/1Hb5tuEiYDruSIZ86wfoQ5PT1AnrG0Y0xJsqeyMhS1ZI/edit?disco=AAAAKVAUpdA>`_.

FHIR representation
+++++++++++++++++++++

FHIR does not have a dedicated named field for this domain element. However, it provides guidance for this and closely related domain concepts `here <https://docs.google.com/document/d/1EVzNmeWuCGl7G3Gk535pTqzSdo356Ci9GlZ3nHiAuM0/edit?disco=AAAAHDCXnWg>`_ and suggests an approach for representing this concept using observations, since there are multiple types of clinical sex (e.g., karyotypic, gonadal, ductal, phenotypic) that could be captured as coded observations.

Phenopackets IG representation
++++++++++++++++++++++++++++++++

The IG uses a FHIR extension to capture KS, as shown `here <https://docs.google.com/document/d/1mzpjsFus-XSo4EP9HE-TC9SVBrXBhNBSnRb-HXx6ewE/edit?disco=AAAAKVAMNQg>`_.

Proposed Core IG representation
+++++++++++++++++++++++++++++++++

The PP karyotypic sex is mapped to an Observation instance. The PP value set is represented with a FHIR valueset that builds on existing FHIR coding systems (assuming HPO will be one of them), or a proposed new coding system or new content for a new coding system if necessary.

Any biding declared in Observation profiles for this element should be preferred or extensible at most, not required. `See here <https://docs.google.com/document/d/1jW1l9okKi65PPYE_amt8n8Q2U9cGQBHeZZLHCbbLqIc/edit?disco=AAAAKVIE0qs>`_ As it says at the end of that section, the binding can be further constrained for project specific purposes but for wider interoperability purposes it is very harmful to have a required binding on a very specific value set. Doing this forces a profile to be “over fitted” to a specific use case and the profile will not be reusable by others and therefore the interoperability value of a profile is eliminated. 