from setuptools import setup, find_packages

setup(
    name='kotprog',
    version='1.0',
    packages=find_packages(),
    install_requires=open("requirements.txt").read().splitlines(),
    author='Albert',
    description='Covid adatvizualizáció',
    include_package_data=True
)
