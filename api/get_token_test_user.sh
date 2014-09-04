#!/bin/bash
. ./env.sh

curl -i   -H "Content-Type: application/json"   -d '
{ "auth": {
    "identity": {
      "methods": ["password"],
      "password": {
        "user": {
          "name": "test_user",
          "domain": { "id": "default" },
          "password": "root"
        }
      }
    }
  }
}' $ENDPOINT/v3/auth/tokens ; echo
