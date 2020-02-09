#!/bin/bash

cd codelabs
claat-darwin-amd64 export *.md

cd ..
gulp serve --codelabs-dir=codelabs
