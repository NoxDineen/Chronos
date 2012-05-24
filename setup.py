import os
from setuptools import setup



setup(
    name = "Chronos",
    version = "1.0",
    author = "Nox Dineen",
    author_email = "nox@freshbooks.com",
    description = ("Support team schedule"),
    license = "BSD",
    keywords = "support schedule calendar",
    url = "https://wiki.2ndsiteinc.com/display/Support/Chronos+1.0",
    packages=['timekeeper', 'tests'],
    long_description=read('README'),
)   


setup(
    name='Chronos',
    version='1.0',
    author = "Nox Dineen"
    license = "BSD",
    url = "https://wiki.2ndsiteinc.com/display/Support/Chronos+1.0",
    packages=find_packages(),
    include_package_data=True,
    long_description='Sample Django Project',
    install_requires=[
            'django',
    ]
)