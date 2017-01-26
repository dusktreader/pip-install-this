import json
import setuptools


with open('.project_metadata.json') as meta_file:
    project_metadata = json.loads(meta_file.read())


setuptools.setup(
    name=project_metadata['name'],
    version=project_metadata['release'],
    author=project_metadata['author'],
    author_email=project_metadata['author_email'],
    description=project_metadata['description'],
    license=project_metadata['license'],
    install_requires=[
        'sh',
        'jupyter',
        'RISE',
    ],
    include_package_data=True,
)
