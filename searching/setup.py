from setuptools import setup, find_packages


def readme():
  with open('README.md', 'r') as f:
    return f.read()


setup(
  name='site_crawler',
  version='0.0.1',
  author='dperevertkin',
  author_email='fixpcvrn@mail.ru',
  description='This is the simplest module for quick work with site files.',
  long_description=readme(),
  long_description_content_type='text/markdown',
  url='https://github.com/Belk1nn/Site_of_vsu.ru',
  packages=find_packages(),
  install_requires=[],
  classifiers=[ 
    'Programming Language :: Python :: 3.11',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent'
  ],
  keywords='files site ',
  project_urls={
    'GitHub': 'Belk1nn'
  },
  python_requires='>=3.6'
)