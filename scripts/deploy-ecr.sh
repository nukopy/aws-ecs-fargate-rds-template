#!/bin/bash

aws cloudformation deploy ${CHANGESET_OPTION} \
  --stack-name "test-app-ecr-cfn" \
  --template "./templates/single/ecr.yml" \
  --profile "admin" \
  --parameter-overrides \
    ProjectName="${ProjectName}" \
    Env="${Env}"
