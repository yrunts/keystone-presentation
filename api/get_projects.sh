#!/bin/bash
. ./env.sh

# should be admin token
TOKEN=""

curl -i -s \
  -H "X-Auth-Token: $TOKEN" \
  $ENDPOINT/v3/projects; echo
