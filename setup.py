from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()


setup(
    name='Twitter CLI Client',
    version='0.1.0',
    author='Miguel Valdes',
    author_email='elxilote@gmail.com',
    description='Twitter CLI Client',
    packages=find_packages()
)
