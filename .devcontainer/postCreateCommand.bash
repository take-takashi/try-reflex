#!/bin/bash

WORKSPACE=$PWD

# セットアップ
cd ${WORKSPACE}/sample-reflex
poetry install --no-root
poetry shell &