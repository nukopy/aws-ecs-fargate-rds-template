#!/bin/bash

echo "deleting stack..."
aws cloudformation delete-stack \
  --stack-name ${CFN_STACK_NAME} \
  --profile ${PROFILE_NAME}
echo "Done."
