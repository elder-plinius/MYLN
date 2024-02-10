from setuptools import setup, find_packages

setup(
    name='myln',
    version='0.1.1',
    author='Pliny',
    author_email='plinius8@proton.me',
    description='A simple text compression package for Python.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/elder-plinius/MYLN',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    python_requires='>=3.6',
)
