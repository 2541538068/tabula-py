from setuptools import setup, find_packages

__author__ = 'Michiaki Ariga'

setup(
  name='tabula',
  version='0.1',
  description='Simple wrapper for tabula, read tables from PDF into DataFrame',
  author=__author__,
  url='https://github.com/chezou/tabula-py',
  classifiers=[
    'Development Status :: 4 - Beta',
    'Topic :: Text Processing :: General',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3 :: Only',
  ],
  packages=find_packages(),
  license='MIT License',
  keywords=['data frame', 'pdf', 'table'],
  install_requires=[
    'pandas'
  ],
)
