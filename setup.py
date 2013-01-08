from setuptools import setup, find_packages

setup(
  name='NoseGntp',
  version='0.1',
  author='Bogdan Gaza',
  author_email = 'bc.gaza@gmail.com',
  description = 'nose plugin for Growl notifications',
  install_requires=['nose>=1.2.1', 'gntp'],
  url = "http://",
  license = "MIT",
  packages = find_packages(exclude=['tests']),
  zip_safe = False,
  include_package_data = True,
  package_data = { 
    '': ['*.png'], 
  },
  entry_points = {
    'nose.plugins': [
      'gntp = nose_gntp.notifier:NoseGntp'
    ]
  }
)
