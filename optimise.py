import os
import sys
from imageoptim import ImageOptimAPI

dir = os.path.abspath(os.path.dirname(__file__))


FILES = [
  'PANO_20140705_mars1.jpg',
  'PANO_20150101_stars.jpg',
  # 'PANO_Dione_moon_color.jpg',
  # 'PANO_Enceladus2_ps.jpg'
]


def main():
  api = ImageOptimAPI('zwwpvcxnbr');
  src_dir = os.path.join(dir, 'src');
  for fn in os.listdir(src_dir):
    file_path = {
      'src': os.path.join(src_dir, fn),
      'output': os.path.join(dir, 'output', fn)
    }
    # If file does not exist, resize it
    if(os.path.isfile(file_path['src'])):
      print('File %s already exists - skipping' % fn)
    else:
      print('Optimising %s' % fn)
      img = api.image_from_file_path(file_path['src'], {'size': '4096x2048'})
      img.save(os.path.join(dir, 'output', fn))


if __name__ == "__main__":
    main()
