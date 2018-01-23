import glob
from setuptools import setup, find_packages


setup(
    name='clockwork_validate_spreadsheet',
    version='0.1.5',
    description='Checks import spreadsheet for clockwork pipeline',
    packages = find_packages(),
    author='Martin Hunt',
    author_email='mhunt@ebi.ac.uk',
    url='https://github.com/iqbal-lab-org/clockwork_validate_spreadsheet',
    scripts=glob.glob('scripts/*'),
    test_suite='nose.collector',
    tests_require=['nose >= 1.3'],
    install_requires=[
        'python-dateutil >= 2.6.1',
        'openpyxl >= 2.4.7',
    ],
    license='GPLv3',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Programming Language :: Python :: 3 :: Only',
        'License :: OSI Approved :: MIT License',
    ],
)
