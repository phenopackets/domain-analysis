===========================
Driver Use Cases
===========================
The following driver use cases will guide the technical development during the current project period. Please see the :doc:`community use cases <usecases-community>` for additional use cases contributed by the community that could guide future work on this project.

A Driver Use Case represents the same content as a  Community Use Case, but it is primarily developed by the project team for the purpose of guiding the technical development and testing activities during the project period. These use cases will be based on clinical and research topics developed in coordination with the pilot sites, involve interactions with FHIR and Phenopackets technical components, and specify the data flow, goals, and outcomes of the use case. For this project, the Driver Use Cases will be largely based on existing domain models in Phenopackets and FHIR, and existing terminologies. The primary goal of these use cases is to integrate existing technical solutions rather than evolve any specific one of them. However, in pursuing integration, specific gaps and enhancements will be needed and will be proposed for future development. These use cases will be documented and analyzed within the Domain Analysis Document.

Kids First Data Resource Center (DRC): Pediatric Cancers and Structural Birth Defects
===========================================================================================

This use case illustrates the need to access knowledge bases to enable research and better clinical interpretations of patient genomic data, based on observed clinical phenotypes.  In this use case, a clinical researcher that is caring for a patient wants to learn more about the phenotypic and genomic profiles of other patients with similar clinical features.

Background and Clinical Workflow
+++++++++++++++++++++++++++++++++++

The Kids First Data Resource Center (KFDRC) has supported the integration and analysis of harmonized large-scale genomic and expression data across more than 30 studies and 30,000 whole genome sequences (WGS) through the DRC’s platforms. The datasets span a diverse cohort of pediatric cancers and structural birth defects that can be utilized to understand a wide range of diseases and disorders in the developmental context. The goal of the KFDRC is to make this data and information as widely available as possible for utilization in basic and translational research as well as in clinical care; for example, laboratory staff or medical geneticists could more seamlessly utilize FHIR with the appropriate tooling to retrieve the most up to date genomic landscape information relevant to the patient case at hand from KFDRC. Currently, many of these “databases” or data resources, require custom, ad-hoc or manual work for each relevant data resource to provide this functionality.

To be able to better support these capabilities, as well as have a common framework for representing this wide range of clinical data, the DRC has moved towards transitioning its current “Data Service” APIs and capabilities over to FHIR. They have piloted the technical implementation of a Kids First DRC FHIR server and are working with key stakeholders from the recently-established NIH Cloud-based Platform Interoperability (NCPI) effort to define the potential for FHIR-based platforms. Their pilot data set has been a cohort from the Pediatric Cardiac Genomics Consortium (PCGC), which has undergone whole genomic sequencing under the Kids First program and is currently loaded in our FHIR servers. Over the next month, they anticipate having several more of our studies represented in FHIR with the goal of having an initial production instance available by the end of the year for all of the released studies. For the purposes of this use case, PCGC spans a wide range of conditions and phenotypes and should be enough to evaluate the utility of utilizing FHIR to retrieve “bulk” or “cohort” data from a FHIR server based on attributes from a single patient in FHIR.

In order to add richer clinical interpretations adhering to molecular sequences and genetic variants, KFDRC has curated more than 6,000 diagnoses and 100,000 phenotypic features for the PCGC cohort. For enhanced interoperability, these conditions and phenotypes have been extensively harmonized with medical terminologies such as HPO, Mondo, and NCIt.

FHIR Rendering of Phenotypic Information
+++++++++++++++++++++++++++++++++++++++++++++

The KF FHIR implementation supports clinical information, including representations of pedigree information, conditions, phenotypic features, and biospecimens.  Currently, the implementation does not support discrete genomics results, although it does include links to traditional laboratory reports.

Use Case
++++++++++++

An infant with cardiac defects (abnormal atrial septum and pulmonary valve) was diagnosed with an atrial septal defect.  As part of the diagnostic process, genomic testing was performed.  No variants were found that readily explained the patient's phenotypes, but a large number of variants of unknown significance (VUS) were identified.  In an effort to establish a diagnosis, the geneticist wanted to find other patients with similar phenotypic profiles and compare the genomic profiles in an attempt to identify a causative variant in a common gene.  The data used in the query of the KFDRC are shown in Table 1.

..  raw:: html

    <table class="docutils align-default">

    <caption style="caption-side:bottom">Table 1: Example of query parameters to find patients with similar phenotypic profiles to an infant with cardiac defects
    </caption>

    <colgroup><col style="width: 30%"><col style="width: 70%"></colgroup>
    <tbody>
    <tr><th>Data Type</th><th>Value(s)</ht></tr>

    <tr>
    <td>age</td>
    <td>0-365d</td>
    </tr>

    <tr>
    <td>sex</td>
    <td>female</td>
    </tr>

    <tr>
    <td>Phenotypes</td>
    <td>Abnormal Atrial Septum (HP:0011994)<br>
    Abnormal Pulmonary Valve (HP:0001641)
    </td>
    </tr>

    <tr>
    <td>Diagnosis</td>
    <td>Atrial septal defect (MONDO:0006664; NCIT:C84473)</td>
    </tr>

    </tbody>
    </table>


The geneticist's search of the KFDRC identifies several dozen patients that have phenotypic profiles that are similar to the index case.  The geneticist retrieves the genomic results for the identified patients and looks for variants in genes that are in common with the index patient's VUS profile.

An example of the type of data returned by the query to the KFDRC is shown in Table 2.  Note that each table represents one patient, of which several could be returned.

..  raw:: html

    <table class="docutils align-default">

    <colgroup><col style="width: 30%"><col style="width: 70%"></colgroup>
    <tbody>
    <tr><th>Data Type</th><th>Value(s)</ht></tr>

    <tr>
    <td>Participant ID</td>
    <td>14999</td>
    </tr>

    <tr>
    <td>Age</td>
    <td>82d</td>
    </tr>

    <tr>
    <td>Sex</td>
    <td>female</td>
    </tr>

    <tr>
    <td>Phenotypes</td>
    <td>Abnormal Atrial Septum (HP:0011994)<br>
    Abnormal Ventriculo-arterial Connection (HP:0011563)
    </td>
    </tr>

    <tr>
    <td>Diagnoses</td>
    <td>Ventricular septal defect, single (MONDO:0002070; NCIT:C84506)<br>
    Dysplastic tricuspid valve (MONDO:0020288; NCIT:C50842)
    </td>
    </tr>


    <tr>
    <td>Specimen retrieved</td>
    <td>Composition: Blood<br>
    Tissue type: Normal (NCIT:C1416)<br>
    Analyte type: DNA</td>
    </tr>

    <tr>
    <td>Sequencing experiment strategy</td>
    <td>Whole Genome Sequencing</td>
    </tr>

    <tr>
    <td>Genetic findings</td>
    <td>Reference genome: GRCh38</td>
    </tr>

    </tbody>
    </table>

    <table class="docutils align-default">
    <caption style="caption-side:bottom">Table 2. Examples of the data types returned from the query.  Each table represents a single patient, which has a phenotypic profile that is similar to the index patient (query parameters are shown in Table 1).
    </caption>
    <colgroup><col style="width: 30%"><col style="width: 70%"></colgroup>
    <tbody>
    <tr><th>Data Type</th><th>Value(s)</ht></tr>

    <tr>
    <td>Participant ID</td>
    <td>16254</td>
    </tr>

    <tr>
    <td>Age</td>
    <td>176d</td>
    </tr>

    <tr>
    <td>Sex</td>
    <td>male</td>
    </tr>

    <tr>
    <td>Phenotypes</td>
    <td>Abnormal Atrial Septum (HP:0011994)<br>
    Abnormal Pulmonary Valve (HP:0001641)<br>
    Abnormal Ventriculo-arterial Connection (HP:0011563)
    </td>
    </tr>

    <tr>
    <td>Diagnoses</td>
    <td>Atrial septal defect (MONDO:0006664; NCIT:C84473)<br>
    Ventricular septal defect, single (MONDO:0002070; NCIT:C84506)<br>
    Atrial septal defect, secundum (MONDO:0020434; NCIT:C84473)
    </td>
    </tr>


    <tr>
    <td>Specimen retrieved</td>
    <td>Composition: Blood<br>
    Tissue type: Normal (NCIT:C1416)<br>
    Analyte type: DNA</td>
    </tr>

    <tr>
    <td>Sequencing experiment strategy</td>
    <td>Whole Exome Sequencing</td>
    </tr>

    <tr>
    <td>Genetic findings</td>
    <td>Reference genome: GRCh38</td>
    </tr>

    </tbody>
    </table>

Technical Development and Testing
++++++++++++++++++++++++++++++++++

The technical development guided by this use case will iteratively identify and profile the FHIR resources needed to represent relevant clinical data in patient-specific knowledge bases.  This will include FHIR resources such as Patient, Observation, Condition, Specimen, and Genomics Report.

The technical development in support of this use case will be based on the KF FHIR implementation guide.  The testing will demonstrate and evaluate the ability of the IG to represent the data included in the use case.  Gaps in the IG, including the representation of genomic reports and results, will be identified and solutions will be explored; these results will be fed back to HL7 FHIR developers and to the KF team.  The implementation and deployment of fixes to gaps in the specifications will not occur until later in year two of this project.

Additional details regarding the technical development and testing for this use case will be provided in the Pilot Testing Management Plan.

Phenotype-driven molecular genetic diagnostics
==============================================

This use case addresses the need to communicate relevant clinical information from the provider’s office to a laboratory and medical geneticist when an exome analysis is ordered for a patient in order to help the laboratory and medical geneticist with identifying the underlying genetic cause of the patient’s clinical features.

Background and Clinical Workflow
+++++++++++++++++++++++++++++++++

Patients with a rare disease usually present with a set of clinical features (i.e. signs and symptoms) that in most cases do not allow a precise (etiological) diagnosis without further testing. Requesting molecular testing is not the same as requesting a routine laboratory result. Most standard laboratory tests are targeted and have well defined normal values and can be readily interpreted. The case is very different for genetic testing. Molecular testing by next-generation sequencing (e.g., exome and genome sequencing) identifies variants that vast majority of which have no clinical significance or are not related to the clinical features noticed during the initial clinical visit. Simply reporting a list of variants is not useful for a clinician, and it is not what occurs in clinical care.

The interpretation of molecular findings can be improved by comparing a patient’s clinical findings with information from databases coupled with  bioinformatics tools to eliminate the molecular findings that are not associated with the clinical findings and prioritize the remaining molecular findings based on how closely they can explain the clinical findings. Occasionally, it is necessary to collect additional clinical information that was not collected during the initial visit to help with selecting a candidate variant among the few top candidates.

However, there is usually a disconnect and lack of information exchange between the requesting clinician’s office and the laboratory and medical geneticist offices. The clinical findings are usually not reported or are very limited. Frequently, just like other simpler lab requests, a paper form is used to request molecular testing, some clinical information might be provided in written form (hand written on the form, a printout of the visit summary), the testing is possibly further outsourced to another laboratory and it becomes very difficult or time consuming to collect further clinical information after the fact. Also, the lack of a standard and computable structure to capture and communicate these findings further complicates the usability of this information by the laboratory and medical geneticist.

FHIR Rendering of Phenotypic Information
+++++++++++++++++++++++++++++++++++++++++

The Phenopackets schema was developed with this use case in mind. It provides a computable representation of relevant phenotypic information to support molecular testing and analysis. It does that by modeling the relevant concepts, identifying the necessary elements for each concept (data fields), and provides recommendations for how values should be captured (i.e. terminologies or date formats)

This use case will address this clinical need and build on the knowledge gained by developing the Phenopackets schema. It will provide a set of FHIR resource profiles to enable the exchange of relevant clinical findings along with the laboratory request to provide the information needed by the medical geneticist in order to provide better and more timely clinical care for the patient.

Use Case
+++++++++++

A female patient presents to a clinician, who observes several phenotypic features: CNS hypomyelination, intellectual disability, encephalopathy, strabismus, and scoliosis.  The clinician suspects a genetic factor may be responsible and orders a clinical exome test.  The phenotypic data are sent to the laboratory along with the order for the test.  These data are shown in Table 1.

..  raw:: html

    <table class="docutils align-default">
    <caption style="caption-side:bottom">Table 1: Excerpt of information contained in an example phenopacket that is sent by a clinical unit to accompany a request for exome sequencing to a laboratory</caption>
    <colgroup><col style="width: 30%"><col style="width: 70%"></colgroup>
    <tbody>
    <tr><th>Data Type</th><th>Value(s)</ht></tr>
    <tr><td>id</td><td>Patient 36-16DG1123</td></tr>
    <tr><td>age</td><td>P10Y</td></tr>
    <tr><td>sex</td><td>female</td></tr>
    <tr><td>Phenotypic features (observed by clinician, ideally recorded in clinical system and accessible via FHIR API)</td>
    <td>CNS hypomyelination (HP:0003429)<br>
    Intellectual disability (HP:0001249)<br>
    Encephalopathy (HP:0001298)<br>
    Strabismus (HP:0000486)<br>
    Scoliosis (HP:0002650)</td></tr>
    <tr><td>Genetic test ordered</td><td>Exome</td></tr>
    </tbody>
    </table>

The laboratory uses the biospecimen to conduct the exome test, which identifies approximately 40,000 variants in the patient's genome (relative to the reference genome assembly).  Even after standard filters are applied to narrow the results to variants with known or suspected pathogenicity, several hundred variants remain to be examined manually.

The laboratory uses the phenotypic information of the patient that was provided by the clinician as an additional filter, which allows the laboratory to identify a mutation in the NKX6-2 gene, which is known to be associated with the patient's phenotypes.  The laboratory assembles a clinical report summarizing the findings and returns it to the clinician.  The clinician diagnoses the patient with Spastic ataxia 8, autosomal recessive, with hypomyelinating leukodystrophy.  The data represented in the report and the subsequent clinical note is shown in Table 2.

..  raw:: html

    <table class="docutils align-default">
    <caption style="caption-side:bottom">Table 2. Additional information included in the second phenopacket that the lab sends back to the clinical unit to report its finding (this phenopacket also contains all of the original information as shown in Table 1)</caption>
    <colgroup><col style="width: 30%"><col style="width: 70%"></colgroup>
    <tbody>
    <tr><th>Data Type</th><th>Value(s)</ht></tr>
    <tr><td>Genetic test ordered</td><td>Exome (PMID:26139844 provides a review of how exome sequencing works and why it is used for genetic diagnostics)

    https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4528311/ </td></tr>

    <tr>
    <td>Genetic results (i.e. variant calling by the lab)</td>
    <td>Usually on the order of 40,000 variants, of which up to a few hundred may require manual inspection following initial bioinformatic filtering.</td>
    </tr>

    <tr>
    <td>Genetic results/findings, most likely relevant based on observed patient phenotypic features (by the medical geneticist). Which clinical features were needed, which databases where consulted, etc.</td>
    <td>NKX6-2 mutation (GRCh37, chr:10: 134599256CG>C)</td>
    </tr>

    <tr>
    <td>Diagnosis</td>
    <td>Spastic ataxia 8, autosomal recessive, with hypomyelinating leukodystrophy (OMIM:617560)

    https://www.omim.org/clinicalSynopsis/617560 </td>
    </tr>

    <tr>
    <td></td>
    <td></td>
    </tr>

    </tbody>
    </table>

The information for this use case was taken from the publication PMID:28940097 (Expanding the genetic heterogeneity of intellectual disability). Exome sequencing was used to arrive at the diagnosis, Spastic ataxia 8, autosomal recessive, with hypomyelinating leukodystrophy (OMIM:617560), owing to a mutation in NKX6-2 (GRCh37, chr:10: 134599256CG>C). In a typical use case, the exome or genome will have 40,000 to 5 million variants, and the analysis of the sequence data will match the clinically observed phenotypic features to a database of diseases and disease associated genes, prioritizing variants in genes that are associated with diseases with similar phenotypes.

Technical Development and Testing
++++++++++++++++++++++++++++++++++++

The technical development guided by this use case will iteratively identify and profile the FHIR resources needed to communicate the clinical features from the point of care to a hypothetical laboratory FHIR endpoint. This will include FHIR resources such as Patient, Observation, Condition, ServiceRequest, Specimen, etc.  It will also attempt to identify and profile any additional profiles necessary to communicate the laboratory molecular findings along with the initial set of clinical findings to a hypothetical medical geneticist FHIR endpoint, and eventually back to the initial clinical system that initiated the request, also through a hypothetical FHIR endpoint. 

The technical development will be demonstrated by simple proof of concept tools. This will not include the building of user interfaces or modules to integrate with EHR systems. This sort of development is out of scope for this project and would come after the release of a more comprehensive Core FHIR implementation guide, which will not occur until later in year two of this project.

Additional details regarding the technical development and testing for this use case will be provided in the Pilot Testing Management Plan.
