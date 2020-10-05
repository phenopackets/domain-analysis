============================
Domain entities
============================

Important aspects of domain analysis include the identification of relevant domain concepts, the documentation of how people in the domain understand and use those concepts, and what data is collected about them or in relation to them. Specific examples of domain entities are the concepts of person, patient, study subject, diagnosis, signs and symptoms, family, and pedigree. People in the domain have a clear and intuitive understanding of these concepts but they also appropriately adjust their understanding and use of these concepts based on the domain context. This frequently leads to difficulties when it comes to data modeling and the often implicit shift of semantic meaning inhibits interoperability.

This section aims to identify these concepts and represent them as modeling entities. This process usually involves capturing the various ways these concepts exist in the domain, giving clear definitions and making clear distinctions, and creating new entities with new labels when a domain concept might be too general or vague and can imply very different entities for different people in the domain or in different domain contexts.

The process for developing this content will likely start as a glossary of the various concepts. Each concept will then be fully defined and contrasted with other concepts such that each has clear semantic boundaries.  In addition, specific relationships between concepts will be established, data elements will be defined, and appropriate terminologies and ontologies will be identified to support the technical development efforts that will follow.

Although the analysis in the following pages should be based on the domain and how domain experts understand it rather than how it's modeled in any existing information model, these pages likely refer to existing representations as a way to identify aspects of the domain that that model intended to represent. Models are usually developed for specific use cases and examining their approach will likely lead us to identifying aspects of the domain that we might not be aware of. However, we're not constrained by the specific definition and modeling decisions from those models. In the following pages those models are simply looked at as a tool to identify the underlying domain they are intending to represent. 

The following is a set of pages to capture any relevant analysis for any relevant domain entity. Each page will summarize and refer to elements in Phenopackets Schema, FHIR, and other existing resources if relevant to the entity or topic.

Add a page to the "domain-entities" folder and it will appear in this list.

..  toctree::
    :caption: Domain entities and topics
    :titlesonly:
    :glob:

    domain-entities/*
