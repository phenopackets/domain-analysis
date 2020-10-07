FHIR mapping
================================

The FHIR mapping workflow is focused on taking the analysis and recommendations from the :doc:`/domain-entities` 

- :doc:`DE </domain-entities>` 


The workflow is based on Google Sheets, GitHub issues, and prototyping the chosen FHIR implementation in the Core IG.

- A Google Sheets `sheet <https://docs.google.com/spreadsheets/d/1zZy3cxaIztQlGk79VI1jSV2Dg5C05HB681z1JGu_vZo/edit?usp=sharing>`_

   - The set of green columns capture domain related information regardless of its current representation in Pheopackets or FHIR
   - The next set of blue columns capture Phenopackets' representation.
   - The next set of yellow columns capture FHIR's representation.
   - A row represent a mapping from the domain to Phenopackets and/or FHIR

- GitHub issues at the `Core IG issue tracker <https://github.com/phenopackets/core-ig/issues>`_
- GitHub pull requests (PRs) for changes to the Core IG. Each pull request is `built and published <https://github.com/phenopackets/core-ig/tree/gh-pages>`_ with the FHIR publisher tool. Links to these PR specific builds can be found at that page.

The following are various types of entities, data elements, or topics relevant to the development of FHIR artifacts in the Core IG


..  toctree::
    :caption: Domain entities and topics
    :titlesonly:
    :glob:

    fhir-mapping/*