from setuptools import setup, find_packages

setup(name='usfm',
    version='0.1.1b1',
    description='USFM Parser and Converters',
    packages=find_packages(),
    zip_safe=False,
    author='Baiju Muthukadan',
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


