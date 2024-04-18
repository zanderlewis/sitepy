from setuptools import setup, find_packages

setup(
    name='sitepy',
    version='0.0.9',
    description='A simple web framework.',
    author='WolfTheDev',
    author_email='wolfthedev@gmail.com',
    url='https://github.com/WolfTheDeveloper/sitepy',
    license='Apache 2.0',
    packages=find_packages(),
    long_description=open('sitepy/README.md').read(),
    long_description_content_type='text/markdown',  # Add this line
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    python_requires='>=3.6',
)