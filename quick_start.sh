#!/usr/bin/env bash
echo 'Run script: quick start for local development'
make migrate
make loaddata
make user
make run

open http://localhost:8000
