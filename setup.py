from setuptools import setup, find_packages


setup(
    name='chronos',
    version='0.9',
    author = "Nox Dineen",
    author_email = "nox@freshbooks.com",
    license = "BSD",
    url = "https://wiki.2ndsiteinc.com/display/Support/Chronos+1.0",
    packages=find_packages(),
    include_package_data=True,
    long_description='Support team scheduling',
    install_requires=open('requirements.txt').readlines()
)
