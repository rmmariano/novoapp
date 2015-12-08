#!/bin/bash



pip install -r venv/requirements.txt
echo ""
echo " --> Installed the requirements."
echo ""

python tests/run_tests.py
echo ""
echo " --> Ran the tests in tests/run_tests.py"


