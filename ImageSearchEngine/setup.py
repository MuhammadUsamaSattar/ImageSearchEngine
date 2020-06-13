from setuptools import setup

setup(name='ImageSearchEngine',
      version='1.0.',
      description='Python program to find relevant images online',
      url='https://github.com/Triosus/ImageSearchEngine',
      author='Usama Sattar',
      author_email='usamasattar.3347@gmail.com',
      license='',
      packages=['ImageSearchEngine'],
      install_requires = [
          "icrawler",
          "PySide2",
          "opencv-contrib-python",
          "numpy"
          ],
      zip_safe=False)
