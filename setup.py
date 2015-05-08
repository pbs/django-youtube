import os
from setuptools import setup, find_packages


README = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'README.md')


DEPENDENCIES = [
    'django >=1.4',
    'google-api-python-client'
]


DEPENDENCY_LINKS = [
    # Add externally hosted packages like so:
    #    e.g. http://github.com/[USERNAME]/[REPO]/tarball/[BRANCH]#egg=[EGG_NAME]
]


setup(
    name='django-youtube',
    version='0.1.0',
    description='Youtube API for Django',
    long_description = open(README, 'r').read(),
    author='Alexandru Pirjol',
    author_email='alex.pirjol@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    install_requires=DEPENDENCIES,
    dependency_links=DEPENDENCY_LINKS,
    setup_requires=[],
    classifiers=[]
)
