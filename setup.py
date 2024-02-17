from setuptools import setup, find_packages

setup(
    name='pyvigate',
    version='0.0.2',
    author='Abhijith Neil Abraham',
    author_email='abhijithneilabrahampk@gmail.com',
    description='A brief description of what your package does',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/pyvigate/pyvigate',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',  # Minimum version requirement of Python
    install_requires=[

    ],
    entry_points={

    },
)
