#! /bin/bash

# Remove logs
rm -r ./src/outputs/logs/*
# Remove results
rm -r ./src/outputs/results/*

tar -czvf app.tgz -C src .