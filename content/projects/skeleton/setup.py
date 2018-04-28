try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
    

config = {
         'description': 'My Project',
         'author': 'XueWeiHan',
         'url': 'URL to get it at.',
         'download_url': 'Where to download it.',
         'author_email': 'My email.',
         'version': '0.1',
         'install_requirse': ['nose'],
         'packages': ['NAME'],
         'scripts': [],
         'name': 'projectname'
}

setup(**config)
   
