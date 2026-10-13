#!/bin/bash
# Double-click to record any narration that changed in narration/clips.json.
cd "$(dirname "$0")"
python3 narration/generate.py
echo
read -n 1 -s -r -p "Press any key to close."
