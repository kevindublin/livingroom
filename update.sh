#!/bin/bash
# UPDATE PELICAN CONTENT
# PUSH TO GITHUB PAGES BRANCH


pelican content -o output -s pelicanconf.py
ghp-import output
git push origin gh-pages

