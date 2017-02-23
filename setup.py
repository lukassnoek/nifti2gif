import nifti2gif
from setuptools import setup, find_packages

def readme():
    with open('README.rst') as f:
        return f.read()

VERSION = nifti2gif.__version__

REQUIREMENTS = [
    'nibabel',
    'joblib',
    'argparse'
]

setup(
    name='nifti2gif',
    version=VERSION,
    description='Tool to make gifs from 3D nifti files.',
    long_description=readme(),
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Science/Research',
        'Operating System :: POSIX :: Linux',
        'Operating System :: MacOS :: MacOS X',
        'Programming Language :: Python :: 2.7',
        'Topic :: Scientific/Engineering :: Bio-Informatics'],
    keywords="MRI nifti gif",
    url='https://github.com/lukassnoek/nifti2gif',
    author='Lukas Snoek',
    author_email='lukassnoek@gmail.com',
    license='MIT',
    platforms=['Linux', 'Mac OSX'],
    packages=find_packages(),
    install_requires=REQUIREMENTS,
    scripts=['bin/nifti2gif'],
    include_package_data=True,
    zip_safe=False)
