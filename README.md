# Final idp utilities

This is a python package to use in python with pulumi automation API microservices

## [idp_args](./src/deploy_args_david_hdez/idp_args.py)

This module contains the needed classes for the deployment of resource from each microservice. \
The [ProgramArgs](./src/deploy_args_david_hdez/idp_args.py) is an abstract class to set up common values among these resources. \
Each SubClass from [ProgramArgs](./src/deploy_args_david_hdez/idp_args.py) sets up the necessary arguments for each custom resource. \

## [idp_sqs](./src/sqs_consumer_david_hdez/idp_sqs.py)

This module contains the classes needed to consume messages from custom SQS given url and the region.

## [network_utilities](./src/utilities_david_hdez/network_calculation.py)

This module the available_subnets method to calculate the CIRD block for each subnet (public, private) given \
a CIDR, number of desired public and private subnets.
