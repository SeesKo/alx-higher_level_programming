#!/bin/bash
# Sends POST request to the URL with specified parameters and display the body of the response
curl -sX POST "$1" -d "email=test@gmail.com&subject=I will always be here for PLD"
