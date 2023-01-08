"""Setup Battery Status Notifier module."""

from setuptools import find_packages, setup


with open('requirements.txt', encoding='utf-8') as requirements_file:
    install_requires = requirements_file.read().splitlines()


with open('README.md', encoding='utf-8') as readme_file:
    readme = readme_file.read()


setup(
    name='bsnotifier',
    version='1.0.2',
    packages=find_packages(exclude=['tests*']),
    include_package_data=True,
    zip_safe=False,
    description='Command line application that shows a popup window when the battery is low',
    author="Erik Ccanto",
    author_email='ccanto.erik@gmail.com',
    url='https://github.com/eccanto/battery-status-notifier',
    license='MIT',
    long_description=readme,
    long_description_content_type='text/markdown',
    install_requires=install_requires,
    classifiers=[
        'Environment :: Console',
        'Operating System :: Unix',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
    python_requires='>=3.7.15, <4',
    entry_points={
        'console_scripts': [
            'bsnotifier = bsnotifier.main:main',
        ]
    },
    keywords=['battery', 'notifier', 'gui', 'popup'],
)
