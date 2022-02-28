@echo off
set ORIGINAL_DIR=%CD%
cd ./deep_sort/deep/reid/torchreid/metrics/rank_cylib/
python setup.py build_ext --inplace
cd %ORIGINAL_DIR%