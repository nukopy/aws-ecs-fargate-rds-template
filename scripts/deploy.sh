#!/bin/bash

# check the number of args
if [ $# -ne 1 ]; then
  echo "Please set arg: 'deploy' or 'changeset'"
  exit 1
fi

# check args
if [ $1 = "deploy" ]; then
  echo "===== deploy ====="
  CHANGESET_OPTION=""
elif [ $1 = "changeset" ]; then
  echo "===== creating changeset ====="
  CHANGESET_OPTION="--no-execute-changeset"
else
  echo "Invalid keyword."
  echo "Please set arg: 'deploy' or 'changeset'"
  exit 1;
fi

# deploy with CloudFormation
# IAM に関するリソースを作るときに --capabilities オプションを付与する必要がある（cf: https://github.com/aws/serverless-application-model/issues/51）
aws cloudformation deploy ${CHANGESET_OPTION} \
  --capabilities CAPABILITY_IAM CAPABILITY_NAMED_IAM CAPABILITY_AUTO_EXPAND \
  --stack-name "${CFN_STACK_NAME}" \
  --template "${CFN_TEMPLATE}" \
  --profile "${PROFILE_NAME}" \
  --parameter-overrides \
    ProjectName="${ProjectName}" \
    Env="${ENV}"
