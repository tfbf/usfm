import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(name='usfm',
    version='0.1.1b1',
    author='Baiju Muthukadan',
    author_email='baiju.m.mail@gmail.com',
    description='USFM Parser and Converters',
    long_description=read('README.rst'),
    license='BSD',
    url='https://github.com/tfbf/usfm',
    packages=find_packages(),
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Text Processing :: Markup',
    ],
    install_requires=['setuptools',
                      'Jinja2',
                      'Parsley', # Requires Python 3 patch (not yet releases):
                                 # https://github.com/python-parsley/parsley
    ],
    entry_points={
        'console_scripts': [
            'usfm=usfm.main:run',
        ],
    },
)


