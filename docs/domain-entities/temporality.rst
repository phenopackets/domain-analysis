Temporality
==============================

This page discusses the representation of all concepts related to time, including discrete time points, periods, quantities, and codes that represent any of those.

**GitHub issue**: `ISSUE <https://github.com/phenopackets/domain-analysis/issues/22>`_

Phenopackets representation
++++++++++++++++++++++++++++++

The Phenopackets specification refers to time-based data elements in many places and represents time data in many different ways, including:

+-------------------+---------------+----------------------------+
| Class             |   Attribute   | Datatype(s)                |
+===================+===============+============================+
| Age               | age           | string                     |
+-------------------+---------------+----------------------------+
| AgeRange          | start         | Age                        |
+-------------------+---------------+----------------------------+
| AgeRange          | end           | Age                        |
+-------------------+---------------+----------------------------+
| Disease           | onset         | Age|AgeRange|OntologyClass |
+-------------------+---------------+----------------------------+
| Individual        | date_of_birth | timestamp                  |
+-------------------+---------------+----------------------------+
| Individual        | age           | Age|AgeRange               |
+-------------------+---------------+----------------------------+
| MetaData          | created       | timestamp                  |
+-------------------+---------------+----------------------------+
| PhenotypicFeature | onset         | OntologyClass              |
+-------------------+---------------+----------------------------+
| Update            | timestamp     | timestamp                  |
+-------------------+---------------+----------------------------+

Some elements of the Phenopackets specification capture time as a primitive datatype (string, timestamp) with additional formatting constraints. Other elements capture time in complex datatype objects (Age, AgeRange, OntologyClass) and may be polymorphic (permitting any one of several types to be used). Due to this heterogeneity within the specification, we must analyze each type individually.

string
------

**Used by:** Age.age

This string conforms to the format specified by `ISO8601 <https://en.wikipedia.org/wiki/ISO_8601>`_ Duration:

  Durations define the amount of intervening time in a time interval and are represented by the format P[n]Y[n]M[n]DT[n]H[n]M[n]S or P[n]W. In these representations, the [n] is replaced by the value for each of the date and time elements that follow the [n]. Leading zeros are not required, but the maximum number of digits for each element should be agreed to by the communicating parties. The capital letters P, Y, M, W, D, T, H, M, and S are designators for each of the date and time elements and are not replaced.

  * P is the duration designator (for period) placed at the start of the duration representation.
  
    * Y is the year designator that follows the value for the number of years.
    * M is the month designator that follows the value for the number of months.
    * W is the week designator that follows the value for the number of weeks.
    * D is the day designator that follows the value for the number of days.

  * T is the time designator that precedes the time components of the representation.

    * H is the hour designator that follows the value for the number of hours.
    * M is the minute designator that follows the value for the number of minutes.
    * S is the second designator that follows the value for the number of seconds.

Age
---

**Used by:** AgeRange.start, AgeRange.end, Disease.onset, Individual.age

This complex datatype has a single attribute (age), which is a formatted string (see above).

AgeRange
--------

**Used by:** Disease.onset, Individual.age

This complex datatype has two attributes (start and end), which are of type Age (see above).

OntologyClass
-------------

**Used by:** Disease.onset, PhenotypicFeature.onset

This complex datatype is used to capture concept codes. It is comprised of two required attributes: an id in `CURIE <https://www.w3.org/TR/curie/>`_ format (where the *prefix* portion of the CURIE is mapped to a Resource through the `MetaData class <https://phenopackets-schema.readthedocs.io/en/latest/metadata.html#rstmetadata>`_ and a label that represents the name of the concept from the Resource. OntologyClass could be used to represent coded periods of time.

timestamp
---------

**Used by:** Individual.date_of_birth, MetaData.created, Update.timestamp

The timestamp type is a string that conforms to the format specified by `ISO8601 <https://en.wikipedia.org/wiki/ISO_8601>`_ with time zone support (UTC).

FHIR representation
+++++++++++++++++++++

FHIR supports a number of datatypes that support capturing dates and times, which are summarized below.

string
------

The primitive `string <https://www.hl7.org/fhir/datatypes.html#string>`_ is a sequence of Unicode characters that shall not exceed 1024*1024 characters in length. There are additional restrictions regarding whitespace.

instant
-------

The primitive `instant <https://www.hl7.org/fhir/datatypes.html#instant>`_ represents a timestamp in YYYY-MM-DDThh:mm:ss.sss+zz:zz format that has a precision of at least seconds and includes a time zone.

time
----

The primitive `time <https://www.hl7.org/fhir/datatypes.html#time>`_ is a string in hh:mm:ss format. Additional minor constraints are specified.

date
----

The primitive `date <https://www.hl7.org/fhir/datatypes.html#date>`_ is a string in YYYY, YYYY-MM, or YYYY-MM-DD format, without time zone.

dateTime
--------

The primitive `dateTime <https://www.hl7.org/fhir/datatypes.html#dateTime>`_ is a string in YYYY, YYYY-MM, YYYY-MM-DD or YYYY-MM-DDThh:mm:ss+zz:zz format. If hours and minutes are present then a time zone must be specified. Additional minor constraints are specified.

Period
------

The complex type `Period <https://www.hl7.org/fhir/datatypes.html#Period>`_ specifies a range of times that is defined by a start and end time, both of the dateTime type.

Duration
--------

The complex type `Duration <https://www.hl7.org/fhir/datatypes.html#Duration>`_ is constrained from `Quantity <https://www.hl7.org/fhir/datatypes.html#quantity>`_. It captures a value (type: decimal) and a code that specifies a unit (of time). If the system that defines the code is present, it must be UCUM.

Age
---

The complex type `Age <https://www.hl7.org/fhir/datatypes.html#Age>`_ is constrained from `Quantity <https://www.hl7.org/fhir/datatypes.html#quantity>`_. It captures a value (type: decimal) and a code that specifies a unit (of time) that is appropriate for Age. If the system that defines the code is present, it must be UCUM.

Other types
-----------

FHIR supports other datatypes that could represent time, which are not discussed here.  CodeableConcept and Coding are discussed elsewhere, generically. SimpleQuantity and Quantity are less appropriate than the alternative specialized types described above. Timing describes the occurrence of an event that may occur multiple times and is not relevant to Phenopackets.

Phenopackets IG representation
++++++++++++++++++++++++++++++++

Discuss....

Proposed Core IG representation
+++++++++++++++++++++++++++++++++

Discuss...
