from setuptools import setup
from io import open


def readme():
    with open('README.rst', encoding='utf-8') as f:
        return '\n' + f.read()


MAJOR               = 1
MINOR               = 0
MICRO               = 0
VERSION = '%d.%d.%d' % (MAJOR, MINOR, MICRO)


setup(name='ratelimitpy',
      version=VERSION,
      description='Simple rate limit decorator',
      long_description=readme(),
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: BSD License',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 3',
          'Topic :: Software Development :: Build Tools',
          'Topic :: Internet',
      ],
      keywords=[
          'ratelimit',
          'api',
      ],
      url='https://github.com/saporitigianni/ratelimitpy',
      download_url='https://pypi.python.org/pypi/ratelimitpy',
      author='Gianni Saporiti',
      author_email='saporitigianni@outlook.com',
      python_requires='>=3',
      license='BSD',
      packages=['ratelimitpy'],
      install_requires=[],
      include_package_data=True,
      zip_safe=False)
