from setuptools import setup, find_packages
import yaml


data = yaml.load(open('recipe/meta.yaml', 'rb'))
name, version = data['package']['name'], data['package']['version']

setup(
    name=name,
    version=version,
    packages = find_packages(),
)

