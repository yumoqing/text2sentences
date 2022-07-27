try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup
from text2sentences.version import __version__
#with open('README.rst', 'r') as f:
#	long_description = f.read()

setup(
	name='text2sentences',
	packages=['text2sentences'],
	version=__version__,
	description='convert a long text to sentences',
	long_description='',
	summary='build sentence from a long text',
	author='Yu Moqing',
	url='https://github.com/yumoqing/text2sentences',
	author_email='yumoqing@gmail.com',
	# install_requires=install_requires ,
	keywords=['text' , 'sentence'],
	classifiers = [
		  'Intended Audience :: End Users/Desktop',
		  'Intended Audience :: Developers',
		  'Intended Audience :: Information Technology',
		  'Intended Audience :: System Administrators',
		  'Operating System :: android :: android TV',
		  'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)',
		  'Programming Language :: Python :: 3'
	],
)
