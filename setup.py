try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup
#with open('README.rst', 'r') as f:
#	long_description = f.read()

with open('text2sentences/version.py', 'r') as f:
	x = f.read()
	y = x[x.index("'")+1:]
	z = y[:y.index("'")]
	version = z
with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
	name='text2sentences',
	packages=['text2sentences'],
	version=version,
	description='convert a long text to sentences',
	long_description=long_description,
	long_description_content_type="text/markdown",
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
		  'Operating System :: OS Independent',
		  'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)',
		  'Programming Language :: Python :: 3'
	],
)
