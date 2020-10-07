FHIR mapping
================================

The FHIR mapping workflow is focused on taking the analysis and recommendations from the :doc:`domain entities </domain-entities>` and converting it to exact mappings to FHIR resources, elements, data types, values, etc. 


The workflow is primarily based on Google Sheets, GitHub issues, and prototyping the chosen FHIR implementation in the Core IG.

- The Google Sheet `sheet <https://docs.google.com/spreadsheets/d/1zZy3cxaIztQlGk79VI1jSV2Dg5C05HB681z1JGu_vZo/edit#gid=1588933282>`_

   - The set of green columns capture domain related information regardless of its current representation in Pheopackets or FHIR
   - The next set of blue columns capture Phenopackets' representation.
   - The next set of yellow columns capture FHIR's representation.
   - A row represent a mapping from the domain to Phenopackets and/or FHIR
   - Additional columns will be used for other workflow aspects such as status, GH issue, review comments, etc.

- GitHub issues at the `Core IG issue tracker <https://github.com/phenopackets/core-ig/issues>`_
- GitHub pull requests (PRs) for changes to the Core IG. Each pull request is `built and published <https://github.com/phenopackets/core-ig/tree/gh-pages>`_ with the FHIR publisher tool. Links to these PR specific builds can be found at that page.


..  toctree::
    :caption: Domain entities and topics
    :titlesonly:
    :glob:

    fhir-mapping/*