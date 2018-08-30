from setuptools import setup
from noesis import __version__

with open('README.pipy.md', 'r') as f:
    long_description = f.read()

setup(name='noesis',
    version=__version__,
    description='An open source framework for network data mining that provides a large collection of network analysis techniques',
    url='http://noesis.ikor.org/',
    author='The NOESIS project team',
    author_email='noesis-support@ikor.org',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='MIT',
    packages=['noesis'],
    install_requires=['numpy','javabridge'],
    package_data={'noesis': ['data/*']},
    include_package_data=True,
    test_suite="noesis.tests.test",
    keywords=['noesis', 'network'],
)