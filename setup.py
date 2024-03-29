from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='pyvigate',
    version='0.0.3',
    author='Abhijith Neil Abraham',
    author_email='abhijithneilabrahampk@gmail.com',
    description='A brief description of what your package does',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/kindsmiles/pyvigate',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
    install_requires=requirements,
    extras_require={
        'docs': [
            'sphinx>=3.0',
            'sphinx_rtd_theme'
        ]
    },
    entry_points={

    },
)
