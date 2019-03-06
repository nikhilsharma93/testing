import numpy as np
from PIL import Image


def catalog_upload(patch_imgs, batch_ids, upload_kwargs, catalog, catalog_name):
    """Upload to DL Catalog."""
    for batch_iter in range(len(batch_imgs)):
        image_id = batch_ids[batch_iter]
        proba = batch_imgs[batch_iter]
        if proba.max() == 0:
            print ('Skipping upload')
            continue
        current_upload_kwargs = upload_kwargs[batch_iter]

        catalog.upload_ndarray(proba, catalog_name, image_id, **current_upload_kwargs)
        print ('Done with upload.')


def define_dlkeys(roi_shape, resolution, tilesize, pad):
    """Define the set of dlkeys over this ROI.
    TODO: Use https://github.com/descarteslabs/appsci_utils/blob/master/appsci_utils/geometry/tile.py#L61
    Parameters
    ----------
    roi_shape: str or shape Feature Collection
        Definition of the shape over which to gather dlkeys
        If it is a string and ends in '.geojson', the corresponding shape file is loaded
        If it does not end with '.geojson', the shape is grabbed from dl.places.shape
    resolution: float
        Per-pixel resolution [meters]
    tilesize: int
        Number of pixels on-a-side for dltiles
    pad: int
        Number of pixels to pad the sides of dltiles
    Returns
    ----------
    keys: list
        list of dltile keys
    """
    if isinstance(roi_shape, six.string_types):
        if roi_shape.endswith('.geojson'):
            with open(roi_shape, 'r') as f:
                roi_shape = json.load(f)
        else:
            roi_shape = dl.places.shape(roi_shape)

    dltiles = dl.raster.dltiles_from_shape(resolution, tilesize, pad, roi_shape)
    keys = [f['properties']['key'] for f in dltiles['features']]
    return keys


def inference_coarseseg(batch_imgs):
    """Dummy function that downsamples the input by 16x and squeezes output between 0 and 1
    to replicate model prediction."""

    batch_size, break_tilesize = batch_imgs.shape[:2]
    batch_output = np.empty((batch_size, int(break_tilesize/16), int(break_tilesize/16)), dtype=batch_imgs.dtype)
    for batch_iter, img in enumerate(batch_imgs):
        img = np.resize(img, (int(break_tilesize/16), int(break_tilesize/16)))
        img = np.clip(img, 0, 1)
        batch_output[batch_iter] = img
    return batch_output


def inference_unet(batch_imgs):
    """Dummy function that squeezes input between 0 and 1
    to replicate model prediction."""

    batch_size, break_tilesize = batch_imgs.shape[:2]
    batch_output = np.empty((batch_size, int(break_tilesize), int(break_tilesize)), dtype=batch_imgs.dtype)
    for batch_iter, img in enumerate(batch_imgs):
        img = np.clip(img, 0, 1)
        batch_output[batch_iter] = img
    return batch_output


def preprocess(batch_imgs, transforms):
    """ Preprocess the input by applying the required transforms.

    Parameters
    ----------
    batch_imgs: ndarray
        Input batch of images

    Returns
    -------
    batch_imgs: ndarray
        Output ndarray

    """
    batch_imgs = batch_imgs.astype('float32')
    for batch_iter, img in enumerate(batch_imgs):
        for transform in transforms:
            img, _ = transform(img)
        batch_imgs[batch_iter] = img
    return batch_imgs


def postprocess_coarseseg(batch_imgs, break_tilesize=2048):
    """ Postprocess the input.

    Parameters
    ----------
    batch_imgs: ndarray
        Input batch of images

    Returns
    -------
    batch_imgs: ndarray
        Output ndarray

    """
    PROB_THRESHOLD = 0.5

    batch_output = np.empty((batch_imgs.shape[0], break_tilesize, break_tilesize), dtype='uint8')

    for batch_iter, img in enumerate(batch_imgs):
        img = img.squeeze()

        # STEP 1)
        img = np.where(img < PROB_THRESHOLD, 0, 1).astype('uint8')
        img_ht, img_wd = img.shape[:2]

        current_output = img.copy().astype('uint8')
        current_output = Image.fromarray(current_output.squeeze())

        # STEP 2)
        current_output = np.asarray(current_output.resize((16*img_ht, 16*img_wd)))
        img_ht, img_wd = current_output.shape[:2]
        x_start = max(0, int((img_wd - break_tilesize)/2))
        x_end = min(img_wd, x_start + break_tilesize)
        y_start = max(0, int((img_ht - break_tilesize)/2))
        y_end = min(img_ht, y_start + break_tilesize)

        current_output = current_output[y_start:y_end, x_start:x_end]

        batch_output[batch_iter] = current_output.astype('uint8')

    return batch_output


def postprocess_unet(batch_imgs, break_tilesize=2048):
    """ Postprocess the input.

    Parameters
    ----------
    batch_imgs: ndarray
        Input batch of images

    Returns
    -------
    batch_imgs: ndarray
        Output ndarray

    """
    PROB_THRESHOLD = 0.5

    batch_output = np.empty((batch_imgs.shape[0], break_tilesize, break_tilesize), dtype='uint8')

    for batch_iter, img in enumerate(batch_imgs):
        img = img.squeeze()

        # STEP 1)
        img = np.where(img < PROB_THRESHOLD, 0, 1).astype('uint8')
        img_ht, img_wd = img.shape[:2]

        # Do some other filterting as required
        batch_output[batch_iter] = img.astype('uint8')

    return batch_output
