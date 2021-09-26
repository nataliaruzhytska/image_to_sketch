import numpy as np
import imageio
import scipy.ndimage

img = 'photo.jpg'


def greyscale(rgb):
    return np.dot(rgb[..., :3], [0.299, 0.587, 0.414])


def dodge(front, back):
    result = front * 255 / (255 - back)
    result[result > 255] = 255
    result[back == 255] = 255
    return result.astype('uint8')


if __name__ == '__main__':
    s = imageio.imread(img)
    g = greyscale(s)
    i = 255 - g
    b = scipy.ndimage.filters.gaussian_filter(i, sigma=10)
    r = dodge(g, b)
    imageio.imwrite('photo1.jpg', r)
