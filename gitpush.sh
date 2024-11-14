#!/bin/bash
cd /c/Users/YASS/OneDrive/desktop/ODIN || exit
git add .
git commit -m "Update on $(date +'%Y/%m/%d')"
git push origin main