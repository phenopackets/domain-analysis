Clinical findings
==============================

This represents any type of observation of clinically relevant things or situations. However, the analysis in this page is primarily focused on:

-  phenotypic features

**GitHub issue**: `ISSUE <https://github.com/phenopackets/domain-analysis/issues/15>`_

Phenopackets representation
++++++++++++++++++++++++++++++

The Phenopackets schema represents phenotypic features with the `PhenotypicFeature <https://phenopackets-schema.readthedocs.io/en/latest/phenotype.html>`_ entity. It captures various aspects of a clinical characteristic of a subject, usually an abnormality. It also dedicates few fields to capture different types of qualifiers including negation, severity, and phenotype specific qualifiers. There is also a representation of the age of onset of the feature.

For our current exome analysis use case we area primarily concerned with capturing the type of a phenotype and a positive vs negative assertion. Other aspects of the Phenopackets PhenotypicFeature will be addressed based on future driver use cases.

It appears that the .severity field's recommended values are a subset of the .modifier field's recommended values.

FHIR representation
+++++++++++++++++++++

This will be a FHIR `Observation <https://www.hl7.org/fhir/observation.html>`_. It captures phenotypes and other sorts of observations.

A FHIR Observation, in its most general sense, is a key/value pair with possible key/value components to capture parts of the overall observation.

The use of this very flexible key/value model can lead to several patterns and this complicates interoperability. The FHIR specification recognizes this and give guidance as `described here <https://www.hl7.org/fhir/observation.html#code-interop>`_. 

The language regarding the `use of Observation components <https://www.hl7.org/fhir/observation.html#gr-comp>`_ is also relevant to our usecase(s).

Phenopackets IG representation
++++++++++++++++++++++++++++++++

It uses FHIR Observation however it models the various types of PhenotypicFeature qualifiers with Extension profiles instead of using the Observation components approach.

Proposed Core IG representation
+++++++++++++++++++++++++++++++++

We will:

- Represent PhenotypicFeature with Observation. One to one instance.
- Represent PhenotypicFeature.type as .code and follow the item 2 `FHIR guidance here <https://www.hl7.org/fhir/observation.html#guidance>`_
- Represent PhenotypicFeature.severity and .modifier as Observation.component entries as justified by `this language <https://www.hl7.org/fhir/observation.html#gr-comp>`_ as opposed to needing Extension profiles.
- Possibly represent PhenotypicFeature.onset as a component. The Observation examples page has an example of an observation that has time built into the code. The Apgar score examples. We can argue that our PhenotypicFeature are time dependent but we don't have onset precomposed into our coding system. However, a PhenotypicFeature will post compose the onset indexed phenotype with Observation components. We believe there are several value[x] available to accommodate the representation of onset.

Given that the PhenotypicFeature.severity is a subset of codes for .modifier, we can represent this with a single modifier component profile that can be instantiated as many times as needed to add the needed qualifiers. The value set for .code will be a small set of very different types of qualifiers, and the value set for .valueCodeableConcept will be the subtree of those codes.

The PhenotypicFeature `example here <https://phenopackets-schema.readthedocs.io/en/latest/phenotype.html>`_ can be represented with this Observation instance but other minor variations (especially for the use of .code and .value[x]) are possible.

.. code-block:: JSON

   {
      "resource": {
        "resourceType": "Observation",
        "code": {
          "coding": [
            {
              "code": "HP:0000520",
              "system": "http://HP",
              "display": "Proptosis"
            }
          ]
        },
        "valueBoolean": true,
        "component": [
          {
            "code": {
              "coding": [
                {
                  "code": "HP:0012824",
                  "display": "Severity",
                  "system": "http://HP"
                }
              ]
            },
            "valueCodeableConcept": {
              "coding": [
                {
                  "code": "HP:0012825",
                  "display": "Mild",
                  "system": "http://HP"
                }
              ]
            }
          },
          {
            "code": {
              "coding": [
                {
                  "code": "HP:0012823",
                  "display": "Clinical modifier",
                  "system": "http://HP"
                }
              ]
            },
            "valueCodeableConcept": {
              "coding": [
                {
                  "code": "SomeAppropriateModifier",
                  "display": "Some appropriate modifier",
                  "system": "http://HP"
                }
              ]
            }
          },
          {
            "code": {
              "coding": [
                {
                  "code": "HP:0003674",
                  "display": "Onset",
                  "system": "http://HP"
                }
              ]
            },
            "valueCodeableConcept": {
              "coding": [
                {
                  "code": "HP:0003577",
                  "display": "Congenital onset",
                  "system": "http://HP"
                }
              ]
            }
          }
        ]
      }
    }

