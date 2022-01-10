#! /bin/bash

# Remove logs
rm -r ./src/outputs/logs/*
# Remove results
rm -r ./src/outputs/results/*

rm -r ./src/outputs/plot/*

rm ./src/outputs/gathered_data.csv
rm ./src/outputs/report.pdf

tar -czvf app.tgz -C src .