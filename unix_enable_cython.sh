#!/usr/bin/env bash

ORIGINAL_DIR=${PWD}
cd ./deep_sort/deep/reid/torchreid/metrics/rank_cylib/ || exit
python3.7 setup.py build_ext --inplace
cd "${ORIGINAL_DIR}" || exit