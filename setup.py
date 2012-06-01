from setuptools import setup, find_packages


setup(
    name='Chronos',
    version='1.0',
    author = "Nox Dineen",
    author_email = "nox@freshbooks.com",
    license = "BSD",
    url = "https://wiki.2ndsiteinc.com/display/Support/Chronos+1.0",
    packages=find_packages(),
    include_package_data=True,
    long_description='Sample Django Project',
    install_requires=[
            'django==1.4',
            'South==0.7.5',
    ]
)
