#!/bin/bash

#Fetching pokemon details using curl and parsing the JSON output
#Pokemon name is entered as parameter to the script

url="https://pokeapi.co/api/v2/pokemon/$1/"

height=`curl -s -X GET $url | jq '.height'`
weight=`curl -s -X GET $url | jq '.weight'`
abilities=`curl -s -X GET $url | jq '.abilities[].ability.name'`

echo $height
echo $weight
echo $abilities
