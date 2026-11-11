from setuptools import setup, find_packages

with open('README.md', 'r') as readme:
    long_description = readme.read()

setup(
    name='sclack',
    version='1.0.1',
    license='GPL3',
    description='The best CLI client for Slack, because everything is terrible',
    long_description=long_description,
    author='Marcelo Camargo',
    author_email='marcelocamargo@linuxmail.org',
    url='https://github.com/haskellcamargo/sclack',
    entry_points={
        'console_scripts': [
            'sclack=sclack.app:run',
        ],
    },
    package_data={
        'sclack': ['config.json']
    },
    packages=find_packages(),
    python_requires='>=3.8',
    install_requires=[
        'urwid>=2.0.1',
        'pyperclip',
        'requests',
        'slackclient',
        'urwid_readline'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
    ],
)
