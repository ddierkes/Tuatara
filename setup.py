import pathlib

import setuptools


REPO = pathlib.Path(__file__).parent


setuptools.setup(
    name='turatara',
    description='A simple IIIF image server',
    author='Daron Dierkes',
    url='https://github.com/ddierkes/Tuatara',
    license='MIT',
    packages=['tuatara'],
    package_data={
        'tuatara': ['static/*', 'templates/*']
    },
    python_requires='>=3.7',
    install_requires=REPO.joinpath('requirements.txt').read_text(),
    entry_points={
        'console_scripts': ['tuatara=tuatara.app:main']
    },
    setup_requires=['setuptools_scm'],
    use_scm_version=True
)
