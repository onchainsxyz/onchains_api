import setuptools

install_requires = [
    'pandas',
    'requests'
]

setuptools.setup(
    name='onchains',
    version='0.0.1',
    author='Phillip Park',
    author_email='onchainsxyz@gmail.com',
    py_modules=['onchains'],
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=install_requires,
)
