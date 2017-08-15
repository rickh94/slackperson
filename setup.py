from setuptools import setup

version = '0.1'
with open('README.md', 'r') as f:
    long_description = f.read()

setup(name='slackperson',
      version=version,
      description='Simple class for storing slack profile information.',
      long_description=long_description,

      author='Rick Henry',
      author_email='fredericmhenry@gmail.com',
      url='https://github.com/rickh94/slackperson.git',

      tests_require=['pytest'],

      license='GPLv3',
      python_requires='>=3',

      py_modules=['slackperson'],
      )
