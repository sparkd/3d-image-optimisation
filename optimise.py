import os
import sys
from imageoptim import ImageOptimAPI

dir = os.path.abspath(os.path.dirname(__file__))


def main():
  api = ImageOptimAPI('zwwpvcxnbr');
  src_dir = os.path.join(dir, 'src');
  for fn in os.listdir(src_dir):
    file_path = {
      'src': os.path.join(src_dir, fn),
      'output': os.path.join(dir, 'output', fn)
    }
    # If file does not exist, resize it
    if(os.path.isfile(file_path['output'])):
      print('File %s already exists - skipping' % fn)
    else:
      print('Optimising %s' % fn)
      options={
        'crop': True,
        # 'quality': 'high'
      }
      img = api.image_from_file_path(file_path['src'], options=options, resize_pow2=True)
      img.save(os.path.join(dir, 'output', fn))


if __name__ == "__main__":
    main()
