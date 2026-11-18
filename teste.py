import numpy as np
import scipy.ndimage
from PIL import Image
from skimage import filters
from skimage import feature

a = Image.open('./imagens_moedas/WhatsApp Image 2026-06-05 at 20.42.54.jpeg').convert('L')
k = np.ones((5,5))/25
b = scipy.ndimage.filters.convolve(a, k)
b = Image.fromarray(b)
b.save('media.png')
c = scipy.ndimage.filters.median_filter(a, 5)
c = scipy.ndimage.filters.median_filter(c, 5)
c = Image.fromarray(c)
c.save('median.png')
z = Image.open('./imagens_moedas/WhatsApp Image 2026-06-05 at 20.42.54.jpeg').convert('L')
z = np.array(z)
d = filters.sobel(z)
d = (d * 255).astype(np.uint8)
d = Image.fromarray(d)
d.save('sobel.png')
e = filters.prewitt(z)
e = (e * 255).astype(np.uint8)
e = Image.fromarray(e)
e.save('prewitt.png')

f = feature.canny(z)
f = (f * 255).astype(np.uint8)
f = Image.fromarray(f)
f.save('canny.png')

g = 255 - z
g = Image.fromarray(g)
g.save('inversao.png')
print(z)