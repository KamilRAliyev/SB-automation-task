#! /bin/bash

# Remove logs
rm -r ./src/outputs/logs/*
# Remove results
rm -r ./src/outputs/results/*

rm ./src/outputs/gathered_data.csv

tar -czvf app.tgz -C src .