#!/bin/bash
# UPDATE PELICAN CONTENT
# PUSH TO GITHUB PAGES BRANCH


echo -n "updating pelican site..."
sleep 2s
. "`pipenv --venv`/bin/activate"
update () {
	
	pelican content -o output -s pelicanconf.py
	ghp-import output
	git push origin gh-pages
  	# update and push
}


update




