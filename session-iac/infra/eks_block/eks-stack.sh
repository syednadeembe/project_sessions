#! /bin/bash

###############################################################################
# Name: eks-stack.sh
###############################################################################
# Description:
# Script to call the CloudFormation with eks-stack.yaml.
# This script needs IAM Admin Role attached to the server running it.
# Only one time execution of this script is needed.
###############################################################################
# Copyright (c) 2023-2024 Onestup.com
###############################################################################

# set -x
# set -e

###############################################################################
# Variable  Declaration
###############################################################################

awsRegion=us-east-1
cfStackName=eks-dev-cluster
templateLocation="file://eks-stack.yaml"

###############################################################################
# Main Declaration
###############################################################################

aws cloudformation create-stack \
  --region $awsRegion \
  --stack-name $cfStackName \
  --capabilities CAPABILITY_NAMED_IAM \
  --template-body $templateLocation 

if [ $? -eq 0 ]
then
  echo "Info: Create call to AWS CloudFormation has been made, check AWS CloudFormation stack status in AWS UI"
else
  echo "Error: Unable to call AWS CloudFormation"
fi