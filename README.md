
# AWS Data Pipeline in Cloudformation

Table of Content
=================
<!--ts-->
   * [About](#About)
   * [Architecture](#architecture)
   * [Deployment](#deployment)
   * [How to Use](#how-to-use)
      * [Settings](#settings)
   * [License](license)   
<!--te-->

## About

This project is an automated Data Pipeline in the AWS Cloud where takes a local file to an S3 bucket using a simple Python code developed using Boto3 SDK and uses a Cloudformation template written in YAML to deploy general resources needed to develop the pipeline.
The Cloudformation template deploys an active Data Pipeline that executes an Redshift Copy activity on the AWS Cloud with a VPC infrastructure and an S3 Resources.

## Architecture

This template deploys an architecture containing:
* One VPC
* Redshift Cluster
* Subnet Group
* Redshift Cluster Parameter Group
* Internet Gateway
* Security Group for the EC2 instance created in the pipeline to communicate with Redshift
* Data Pipeline
* An S3 Endpoint
* Two S3 Buckets, one for Raw Data and another for the pipeline logs

## Deployment

Recommended having preious knowledge in using AWS services, such as Cloudformation, IAM, VPC and Data Pipeline. 
The Python code must be executed from your local code runner while the stack in Cloudformation is being created. 
During the stack creation, update the YAML file and next, specify the parameters from the template, choose the 

## How to use
It's essential having an AWS account and use us-east-1 reagion or another region where Data Pipeline service is available.
You can manually reeschedule the pipeline actions by accessing de Data Pipeline console or modify the Redshift Cluster type in the cloudformation parameters

### Settings

For the pipeline attending to multiple purposes, there are a few things that you've got to manage your own, just like:
* A Security Group for the Redshift Cluster. 
* An IAM role for the Data Pipeline called "role". 
* An IAM role for the Ec2 Resource from the pipeline called "resourceRole".
* A Redshift Endpoint from the VPC console. 

## Project Status
Even though it's finished, for further enhancement, I'd like to find collaborators to help me improve even more my work. 

## License
[MIT](https://choosealicense.com/licenses/mit/)
