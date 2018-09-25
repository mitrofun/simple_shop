#!/usr/bin/env bash
echo 'Run script: quick start for local development'
make migrate
mkdir -p media/products && cp -rn fixtures/products media
make loaddata
make user
make run

open http://localhost:8000
