from setuptools import setup, find_packages

try:
    import pypandoc
    long_description = pypandoc.convert_file('README.md', 'rst')
except(IOError, ImportError):
    long_description = open('README.md').read()

setup(
    name='passgen',
    version='1.0.0',
    description='Simple Password Generator with CLI tool.',
    long_description=long_description,
    author='Ifeanyi Nneji',
    author_email='ifeanyinneji777@gmail.com',
    url='https://github.com/Nneji123/',
    license='MIT',
    packages=find_packages('src'),
    package_dir={'passgen': 'src'},
    python_requires='>=3.6',
    scripts=['src/passgen/passgen.py'],
    classifiers=[  # see https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Topic :: Security',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS',
        'Operating System :: POSIX :: Linux',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python',
        #  'Development Status :: 4 - Beta',
        'Development Status :: 5 - Production/Stable',
    ],
)
