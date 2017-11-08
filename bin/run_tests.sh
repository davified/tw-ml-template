#!/usr/bin/env bash
# Note: call this from the project directory, using bin/run_tests.sh

set -e

PROJ_DIR="$(pwd)"

echo "Running unit tests with nose"
nosetests -w "${PROJ_DIR}/app/tests"
