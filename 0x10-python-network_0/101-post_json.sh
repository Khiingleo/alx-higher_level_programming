#!/bin/bash
# sends a JSON request and displays the body of the response
curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"
