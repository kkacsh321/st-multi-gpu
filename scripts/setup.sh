#!/usr/bin/env bash

set -o errexit -o errtrace

header() {
    echo
    echo "------ $*"
}

header "Installing brew dependencies"

brew bundle

header "Running Pre-commit Install"

pre-commit install

pip install -r requirements.txt

header "Done."