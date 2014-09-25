from setuptools import setup, find_packages  # Always prefer setuptools over distutils


setup(
        author='vyscond',
        author_email='vyscond@gmail.com',

        name='pj',
        version='0.1.0',
        packages=['pj'],
        entry_points={
            'console_scripts': [
                'pjget=pj:pj_get',
            ],
        },
    )
