#!/bin/bash
cd /c/Users/YASS/OneDrive/Desktop/ODIN || exit
git add .
git commit -m "Update on $(date +'%Y/%m/%d')"
git push origin main