import setuptools

_requires = [
    'six',
    'setuptools-scm',
    'ebs-linuxnode-core',
    'appdirs',
]

setuptools.setup(
    name='ebs-linuxnode-exim',
    url='https://github.com/ebs-universe/ebs-linuxnode-exim',

    author='Chintalagiri Shashank',
    author_email='shashank.chintalagiri@gmail.com',

    description='Export Import Infrastructure for EBS Linuxnode Applications',
    long_description='',

    packages=setuptools.find_packages(),
    install_requires=_requires,

    setup_requires=['setuptools_scm'],
    use_scm_version=True,

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Operating System :: POSIX :: Linux',
    ],
)