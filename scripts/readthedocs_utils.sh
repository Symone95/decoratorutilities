# Cancello il contenuto della docs_build e lo ricreo
rm -rf docs_build/*
cd docs
pipenv run make html