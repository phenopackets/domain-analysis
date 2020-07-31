===========================
Driver Use Cases
===========================
The following are the driver use cases that will guide the technical deveopment during the current project period. The :doc:`community use cases <usecases-community>` are additional use cases contributed by the community and could guide community contributions to this project.  

Kids First FHIR interoperability and Phenopackets extraction
============================================================
This is a Kids First based use case to demonstrate core data interoperability between the evolving Kids First IG and the Core IG being developed during this project. Kids First initially attempted to adopt an existing Phenopackets-based FHIR IG to expose existing data through a FHIR API. This effort led to some difficulty with aligning their data, and the development of a new FHIR IG for Kids First. This use case will analyze the Kids First IG, one of the Kids First datasets being exposed with this IG, along with the existing Phenopackets IG and the Phenopackets native schema, to specify and demonstrate data interoperability for core entities represented by these different models and FHIR IGs. Specifically, the following will be implemented and tested by this use case:

- We will use the Kids First IG, one of the Kids First datasets exposed with the Kids First IG, and the Phenopackets schema to identify at least 3 core entities that will be modeled in the Core IG.
- The core entities will be documented and analyzed in the Domain Analysis Document to understand the scope of the FHIR representation in the Core IG.
- A demonstration FHIR server instance will be stood up and the Core IG will be loaded into this instance for validation of the IG, and for data validation during subsequent interactions.
- Demonstration of data exchange between the Kids First IG and server and the Core IG and its demonstration server. This could be accomplished with Jupyter notebook examples or other code snippets. This will test and document any issues around FHIR to FHIR interoperability between the two IGs and how to address them going forward.
- Write POC code to extract Phenopackets instance(s) in the native format by querying Core IG based data to test interoperability between the Core IG and the current Phenopackets schema.

This use case is primarily focused on:

- Technical interoperability
- Data exchange
- The Core IG being the core common denominator/hub for interoperability between the Kids First IG, the existing Phenopackets IG, and the Phenopackets native schema
- Help us establish and test our technical artifacts and workflow for ongoing IG development beyond the period of this project.
- This use case is focused on data representation and message exchange for few core entities. Higher level domain or application specific use cases will build on the development guided by this use case.

Phenotype-driven molecular genetic diagnostics
==============================================
This use case demonstrates the value of FHIR interoperability in a clinical setting. The goal is to enhance the communication of phenotypic information in clinical settings to support well established clinical workflows.

Clinicians and hospitals send blood or DNA samples to a laboratory for molecular diagnostics of Mendelian disorders. Traditionally, little or no detailed information about clinical phenotypes is provided. In the experience of Peter Robinson, paper entry forms were used which allowed submitters to name the suspected diagnosis or other relevant clinical information. In the NGS era, where gene panels, exomes, or genomes are used for diagnostics in cases where the underlying diagnosis is unknown, it would be highly desirable to have more information about phenotypic findings to guide interpretation of NGS findings.

We will demonstrate the exchange of phenotypic information to a hypothetical lab by using our POC Core IG FHIR server. The laboratory request, the Phenopackets file, and any native FHIR representations of the same phenotypic information for the attached Phenopackets file will be communicated to the POC server. This will simulate the submission to a real FHIR based laboratory/EHR API. We will also demonstrate how the laboratory could retrieve such a request and related clinical information from the POC server to demonstrate how an existing laboratory could still benefit for a third party FHIR server to obtain structured and computable information. We will also simulate the fulfillment of the laboratory request through the POC server. The richness of the data communicated for this use case, and through the POC server, will be limited to the extent it is modeled in the Core IG. However, we’ll also explore the possibility of additional data exchange based on the base FHIR spec when possible. We will also demonstrate how to attach any related artifacts (PDFs for example) to FHIR messages to support existing forms of communication in addition to our attempt to provide a structured form of the same information in the form of FHIR resources or Phenopackets instances.
