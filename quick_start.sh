#!/usr/bin/env bash
echo 'Run script: quick start for local development'
echo 'Install bootstrap'
yarn install
echo 'Copy vendor static files'
gulp copy
echo 'Copy media files'
mkdir -p media/products && cp -rf fixtures/products media
make migrate
make loaddata
make user
make run

open http://localhost:8000
