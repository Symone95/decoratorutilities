# Installing "setuptools" and "wheel" libraries
python3 -m pip install --user --upgrade setuptools wheel

rm -rf dist/

# Creating dist archives
python3 setup.py sdist bdist_wheel

# Upgrade "twine" module | --user
python3 -m pip install --upgrade twine

read -p "Enter environment to upload package[dev, pro]: " environment

if [ $environment == "dev" ]
then
  # Upload dists archives to "testpypi"
  python3 -m twine upload --repository testpypi dist/*
elif [ $environment == "pro" ]
then
  # Upload dists archives to "testpypi"
  python3 -m twine upload dist/*
else
  echo "Environment not found, choose between [\"dev\", \"pro\"]"
fi
