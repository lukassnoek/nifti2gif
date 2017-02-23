nifti2gif
---------
Simple script to transform 3D nifti files to fancy gifs!

Dependencies
~~~~~~~~~~~~
This package depends on the following Python packages:

- nibabel
- joblib (for parallel processing)

Optionally, to use the reorientation and skullstripping functionality, make
sure FSL is installed.

Installation
~~~~~~~~~~~~
Unfortunately, no pip-install (through pypi) possible (yet), but you can
install it using pip from the Github repo directly::

	$ pip install git+https://github.com/lukassnoek/nifti2gif.git@master

Or, alternatively, download the package as a zip-file from Github, unzip, and run::

	$ python setup.py install

Usage
~~~~~
Use the command-line interface as follows::

    $ nifti2gif [-h] -f FILE [-d DIRECTION] [-s SCALE] [-k SKIP] [-t TRIM]
    [-r REORIENT] [-b BET] [-F BET_F] [-g GIFNAME] [-D DELAY]
    [-l LOOP] [-n N_PROC]

The only mandatory argument is the filename (-f flag), so this is nifti2gif's basic usage::

    $ nifti2gif -f my_nifti_file.nii.gz

Optional arguments are:
  -h, --help    show this help message and exit
  -f FILE, --file FILE  Filename of nifti to process.
  -d DIRECTION, --direction DIRECTION   Direction (orientation) of gif-movie (default: x-direction/saggital)
  -s SCALE, --scale SCALE   Scale ("size") of gif-image (default: 1, i.e. no scaling)
  -k SKIP, --skip SKIP  How many slices to skip from beginning (default: 0)
  -t TRIM, --trim TRIM  How many slices to trim from the end (default: 0)
  -r REORIENT, --reorient REORIENT (default: False)
                        Whether to run reorient2std (FSL)
  -b BET, --bet BET     Whether to run bet (FSL) (default: False)
  -F BET_F, --bet_f BET_F (default: 0.4)
                        What fractional intensity (bet option) to use
  -g GIFNAME, --gifname GIFNAME (default: {filename}_direction_{x/y/z}.gif
                        How to name the gif-file
  -D DELAY, --delay DELAY (default: 10)
                        The delay (in ms) of the images in the gif
  -l LOOP, --loop LOOP (default: 0)  How many times to loop the gif (default is infite)
  -n N_PROC, --n_proc N_PROC (default: 1)
                        How many cpus (processes) to use
