from setuptools import find_packages
from setuptools import setup

setup(
    name='vda5050_msgs',
    version='0.0.0',
    packages=find_packages(
        include=('vda5050_msgs', 'vda5050_msgs.*')),
)
