import nibabel as nib
import os
from glob import glob
from joblib import delayed, Parallel

__version__ = '0.1'


def convert_nifti_to_gif(fname, direction='x', scale=1, skip=0, trim=0,
                         reorient=False, bet=False, bet_F=0.4, gifname=None,
                         delay=10, loop=0, n_proc=1):
    """ Main function to convert a 3D nifti to a gif.

    Parameters
    ----------
    fname : str
        Absolute path to 3D nifti file.
    direction : str
        Direction (orientation) of gif: should be 'x' (saggital), 'y' (coronal)
        or 'z' (axial/horizontal).
    scale : int/float
        Scaling factor of gif (higher = larger)
    skip : int
        How many slices to skip from the beginning.
    trim : int
        How many slices to trim from the end
    reorient : bool
        Whether to run 'fslreorient2st' on the nifti first.
    bet : bool
        Whether to run 'bet' (fsl skullstripping) on the nifti first.
    bet_F : float
        In case of betting, what fractional intensity threshold should be used.
    gifname : str
        Name for outputted gif.
    delay : int
        Delay between images in gif (in ms).
    loop : int
        How many times the gif should be looped (default is 0, infinite loop)
    n_proc : int
        How many CPU cores should be used for processing (default is 1).
    """

    dir_name = os.path.dirname(fname)
    base_name = os.path.basename(fname).split('.')[0]

    directions = {'x': 0, 'y': 1, 'z': 2}
    nifti = nib.load(fname)

    if len(nifti.shape) > 3:
        raise ValueError("Seems to be a 4D file! Should be 3D.")

    slices = nifti.shape[directions[direction]]

    slice_set = range(skip, slices - trim)

    if reorient:
        new_name = os.path.join(dir_name, '%s_reoriented.nii.gz' % base_name)
        if not os.path.isfile(new_name):
            os.system('fslreorient2std %s %s' % (fname, new_name))

        fname = new_name

    if bet:
        base_name = os.path.basename(fname).split('.')[0]
        new_name = os.path.join(dir_name, '%s_betted.nii.gz' % base_name)

        if not os.path.isfile(new_name):
            os.system('bet %s %s -f %.2f -R' % (fname, new_name, bet_F))

        fname = new_name

    stat = Parallel(n_jobs=n_proc)(delayed(_process_parallel)(
           fname, islice, scale, direction, dir_name) for islice in slice_set)

    if gifname is None:
        gifname = '%s_direction_%s' % (base_name, direction)

    _ = os.system('convert -delay %i -loop %i %s %s.gif' %
                  (delay, loop, os.path.join(dir_name, '*.png'),
                   os.path.join(dir_name, gifname)))
    _ = [os.remove(f) for f in glob(os.path.join(dir_name, '*png'))]


def _process_parallel(fname, slice, scale, direction, dir_name):
    """ Processes slices in parallel. """

    if (slice + 1) < 10:
        outnr = '00%i' % (slice + 1)
    elif (slice + 1) < 100:
        outnr = '0%i' % (slice + 1)
    else:
        outnr = str(slice + 1)

    out_name = os.path.join(dir_name, 'out_%s.png' % outnr)
    cmd = 'slicer %s -%s -%i %s -s %.2f' % (fname, direction, (slice + 1),
                                            out_name, scale)
    status = os.system(cmd)
    return status
