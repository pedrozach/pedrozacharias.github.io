## Project Overview

This project is a data product validation tool designed to validate YAML data product specifications against JSON schemas. The tool ensures that data products conform to predefined structures and rules, facilitating consistency and reliability in data management.

## Project Structure

    data_product_validator/
    ├── main.py
    ├── schemas/
    │   ├── v1/
    │   │   ├── components/
    │   │   │   ├── outputports/
    │   │   │   │   ├── redshift.json
    │   │   │   │   ├── trino.json
    │   │   │   │   ├── s3.json
    │   │   │   │   └── outputport_specification.json
    │   │   │   ├── workloads/
    │   │   │   │   ├── workload_specification.json
    │   │   │   │   ├── airflow.json
    │   │   │   │   └── ...
    │   │   │   ├── component_specification.json
    │   │   │   └── ...
    │   │   ├── data_product_specification.json
    │   │   ├── examples/
    │   │   │   ├── redshift_output_example.yaml
    │   │   │   ├── trino_output_example.yaml
    │   │   │   ├── s3_output_example.yaml
    │   │   │   └── ...
    │   │   └── tests/
    │   │       └── test_schemas.py
    │   └── v2/
    │       └── data_product_specification.cue
    ├── sample_data_product.yaml
    ├── Pipfile
    ├── Pipfile.lock
    └── README.md



# Data Product Specification Framework
## Overview
This project aims to develop a comprehensive framework for defining, validating, and managing data product specifications using the CUE language. The framework provides an abstraction layer that simplifies the creation and maintenance of data product specification files, ensuring consistency, scalability, and adaptability over time.

By leveraging CUE's powerful schema definition and data validation capabilities, the project enables strict adherence to data contracts and promotes best practices in data governance. The framework originates from the need to standardize data product definitions and facilitate seamless integration with various data processing technologies within the organization.

## Objectives
The main objectives of this project are:

- **Create an Abstraction Layer:** Simplify the process of fulfilling data product specification files by abstracting underlying complexities and providing clear, concise schemas.

- **Ensure Scalability and Maintainability:** Structure the framework to allow for easy extension and modification over time, accommodating new components and technologies as they emerge.

- **Promote Technology-Agnostic Design:** Define fixed structures that are technology-agnostic, enabling consistent handling of data products regardless of the underlying technologies.

- **Support Technology-Specific Configurations:** Allow for technology-specific details within designated sections, ensuring flexibility and adaptability to specific use cases.

## Components
The data product is composed of a general section containing data product-level information and four substructures describing components:

1. **Workloads:** Internal jobs and processes that feed the data product and perform housekeeping tasks such as GDPR compliance, regulation adherence, auditing, and data quality checks.

2. **Output Ports:** Interfaces through which the data product exposes data to consumers, including databases, APIs, message queues, and file systems.

3. **Storage Areas:** Internal data storages where the data product is deployed, not directly exposed to consumers.

4. **Observability:** Components providing transparency to data consumers about the data product's current state and performance, exposing runtime data.

Each component has a well-defined fixed structure (technology-agnostic) and a specific section to handle technology-specific configurations. The fixed structure ensures consistency across the organization, while the specific section allows for flexibility and adaptation to particular technologies.

## Workloads
Workloads represent internal processes and jobs responsible for feeding the data product and performing maintenance tasks. Examples include:

- **Airflow DAGs:** Orchestrated workflows using Apache Airflow to run tasks such as Spark jobs, AWS Batch jobs, or Trino queries.

- **Spark Operators:** Tasks executing data transformations using Apache Spark through PySpark.

- **AWS Batch Operators:** Tasks managing batch processing workloads using AWS Batch.

Trino Operators: Tasks executing SQL queries using Trino (formerly PrestoSQL).

## Output Ports
Output Ports define the interfaces through which data is exposed to consumers. Examples include:

- **Trino Tables:** Providing interactive SQL query capabilities over large datasets via Trino.

- **Redshift Tables:** Exposing data through Amazon Redshift for business intelligence and reporting.

- **APIs:** Offering RESTful or GraphQL APIs for data access.

- **Message Queues:** Publishing data to Kafka topics or AWS Kinesis streams for real-time consumption.

## Storage Areas
Storage Areas represent the internal data storage solutions used by the data product, such as:

- **Amazon S3 Buckets:** Storing data files in S3.

- **Databases:** Internal databases not directly exposed to consumers.

## Observability
Observability components provide insights into the data product's operation, including:

- **Monitoring Dashboards:** Visualizing performance metrics and system health.

- **Logging Systems:** Capturing logs for auditing and debugging purposes.

- **Alerting Mechanisms:** Notifying stakeholders of critical events or issues.