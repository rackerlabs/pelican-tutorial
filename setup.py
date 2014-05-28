from distutils.core import setup

setup(
    name='pelican-tutorial',
    version='0.8',
    packages=['pelican_tutorials'],
    url='https://github.com/rackerlabs/pelican-tutorial',
    license='AGPL',
    author='Bill Anderson',
    author_email='bill.anderson@rackspace.com',
    description='A pelican tutorials plugin',
    install_requires = ['pelican',]
)
