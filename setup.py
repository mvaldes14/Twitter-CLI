from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()


setup(
    name='Twitter CLI Client',
    description='Twitter CLI Client',
    version='0.1.0',
    author='Miguel Valdes',
    author_email='elxilote@gmail.com',
    packages=find_packages('twittercli'),
    entry_points="""
        [console_scripts]
        twcli=twittercli.cli:main
        """
)
