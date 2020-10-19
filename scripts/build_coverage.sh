coverage run --source=decoratorutilities -m pytest ../tests/
coverage html
coverage report -m
cd ..
coveralls