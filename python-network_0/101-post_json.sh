#!/bin/bash
# Sends a JSON POST request with the contents of a file to a given URL and displays the response
curl -s -H "Content-Type: application/json" -d @"$2" "$1"
