try:
    from setuptools import setup

except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'author': 'My Name',
    'url': 'URL to get it',
    'download_url': 'Where to download it',
    'author-email' : 'My email',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAMES'],
    'scripts': [],
    'name': 'projectname'
}

setup(**config)

