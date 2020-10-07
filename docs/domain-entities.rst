============================
Domain entities
============================

The important aspects of domain analysis include identification of relevant domain concepts, the documentation of how people in the domain understand and use those concepts, and what data is collected about them or in relation to them. Specific examples of domain entities are the concepts of person, patient, study subject, diagnosis, signs and symptoms, family, and pedigree. People in the domain have a clear and intuitive understanding of these concepts but they also appropriately adjust their understanding and use of these concepts based on the domain context. This frequently leads to difficulties when it comes to data modeling and the often implicit shift of semantic meaning inhibits interoperability.

This section aims to identify these concepts and represent them as modeling entities. This process usually involves capturing the various ways these concepts exist in the domain, giving clear definitions and making clear distinctions, and creating new entities with new labels when a domain concept might be too general or vague and can imply very different entities for different people in the domain or in different domain contexts.

Although the analysis in the following pages should be based on the domain and how domain experts understand it rather than how it's modeled in any existing information model, these pages will likely refer to existing representations as a way to identify aspects of the domain that the model intended to represent. Models are usually developed for specific use cases and examining their approach will likely lead us to identifying aspects of the domain that we might not be aware of. However, we are not constrained by the specific definition and modeling decisions from those models. Also, a common modeling error is the "over fitting" of such models to the specific use case or project at hand. This over fitting leads to difficulties with reusing these models for other projects and eventually to the proliferation of over fitted models. This is a major interoperability barrier. In the following pages those models are simply looked at as a tool to identify the underlying domain they are intending to represent and provide one or more alternative representations within the FHIR framework.

\*Any workflow related comments can be `posted here <https://github.com/phenopackets/domain-analysis/issues/11>`_

..  toctree::
    :caption: Entity pages
    :titlesonly:
    :glob:

    domain-entities/*

\*Add a page to the */domain-entities* folder and it will appear in the above list.


Recommended workflow
+++++++++++++++++++++++++++++++++

#. Identify an in scope domain entity.
#. Create a page for it by copying the /domain-entities/_template.rst.off file and naming it following the pattern used by the other files in that same directory.
#. Fill in or replace the template's content
#. Create a GitHub issue for the domain entity to support ongoing discussion of the entity.#. When appropriate, add any needed mapping information according to the mapping workflow (yet to be defined) and build any needed FHIR conformance resources to implement the FHIR representations for the domain element. This is done under the `Core IG repository <https://github.com/phenopackets/core-ig>`_
#. Any newley developed content for the DAD or the Core IG should be submitted with a GitHub PR for review before merging into the GH master branch.

As part of this workflow, and to facilitate the team's ability to review source material, annotate it, have quick informal comments or questions about it, and to be able to do all this within the context of the original source material, we are copying the source material into a set of Google Docs pages in a folder dedicated for this purpose. As you read through the analysis of the domain entities listed below, you will find various links to comments in these copies as a way to identify and communicate relevant portions of the source content. For example, the Phenopackets Individual and FHIR Patient and Person resource documentation is copied to individual pages and various parts of this content is sited in the analysis of those domain entities. When following any of these links, please be patient until the linked page is fully loaded and the page is scrolled to the specified linked area or comment. 

The folder can be `found here <https://drive.google.com/drive/folders/1rXNPRq-eV4VSiWOdDRSJ3smRMvlmp1QL>`_ and any comments are viewable by all. Each page has a link at the top to the original source of the copied content. Join the project's team to be able to comment. However, anyone with a GitHub account should be able to comment on the corresponding issue if they don't have access to these docs as an alternative way for providing feedback.




