"""
Treys: A pure Python poker hand evaluation library
"""

from setuptools import setup, find_packages


setup(
    name='treys',
    version='0.1.8',
    description='treys is a pure Python poker hand evaluation library',
    long_description=open('README.rst').read(),
    author='Will Drevo, Mark Saindon, Imran Hendley',
    url='https://github.com/ihendley/treys',
    license='MIT',
    packages=find_packages(include=['treys', 'treys.*']),
    python_requires='>=3.9',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Topic :: Games/Entertainment'
    ]
)
