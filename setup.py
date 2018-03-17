from setuptools import setup

setup(name='noesis',
    version='0.2',
    description='An open source framework for network data mining that provides a large collection of network analysis techniques',
    url='http://noesis.ikor.org/',
    author='The NOESIS project team',
    author_email='noesis-support@ikor.org',
    license='MIT',
    packages=['noesis'],
    install_requires=['numpy','javabridge'],
    package_data={'noesis': ['data/*']},
    include_package_data=True,
    test_suite="noesis.tests.test",
    keywords=['noesis', 'network'],
)