import numpy as np
from PIL import Image


def preprocessing_func1(p1, p2):
    # actual implementation
    print('p1 and p2 areee: ', p1, p2)
    return p1 + p2 + 5


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


def postprocess(batch_imgs, break_tilesize=2048):
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


def coarse_seg_inference(batch_imgs):
    """Dummy function that downsamples the input by 16x and squeezes output between 0 and 1
    to replicate model prediction."""

    batch_size, break_tilesize = batch_imgs.shape[:2]
    batch_output = np.empty((batch_size, int(break_tilesize/16), int(break_tilesize/16)), dtype=batch_imgs.dtype)
    for batch_iter, img in enumerate(batch_imgs):
        img = np.resize(img, (int(break_tilesize/16), int(break_tilesize/16)))
        img = np.clip(img, 0, 1)
        batch_output[batch_iter] = img
    return batch_output
