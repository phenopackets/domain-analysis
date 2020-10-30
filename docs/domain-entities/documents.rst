Clinical documents
==============================

This represents any type of document or file that is clinically relevant. However, for this project we're primarily concerned with the following types of documents:

-   A phenopacket message, object, document, etc. in its native format.
-   Other...

**GitHub issue**: `ISSUE <https://github.com/phenopackets/domain-analysis/issues/13>`_

Phenopackets representation
++++++++++++++++++++++++++++++

Phenopackets schema has a top level entity that represents the container for the information in a phenopacket instance.

FHIR representation
+++++++++++++++++++++

FHIR allows various resources to reference a document through a `DocumentReference <https://www.hl7.org/fhir/documentreference.html>`_. This resource can be used to capture a reference to a phenopacket document in the context of a FHIR API. We'll need to determine the:

-   `DocumentReference.type <https://www.hl7.org/fhir/documentreference-definitions.html#DocumentReference.type>`_
-   `DocumentReference.content.format <https://www.hl7.org/fhir/documentreference-definitions.html#DocumentReference.content.format>`_
-   `DocumentReference.content.attachment.contentType <https://www.hl7.org/fhir/datatypes-definitions.html#Attachment.contentType>`_

The content of a phenopacket can be base64-encoded and added to `DocumentReference.content.attachment.data <https://www.hl7.org/fhir/datatypes-definitions.html#Attachment.data>`_

Phenopackets IG representation
++++++++++++++++++++++++++++++++

N/A

Proposed Core IG representation
+++++++++++++++++++++++++++++++++

Use a DocumentReference and inline a phenopacket while submitting a laboratory request for UC 2.
