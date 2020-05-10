import setuptools

setuptools.setup(
    name='openvpn-test',
    version='0.0.1',
    author='Ilya Lyaukin',
    author_email='kzerby@gmal.com',
    description='A script to test openvpn connections',
    url='https://github.com/ilyaukin/openvpn-test',
    packages=setuptools.find_packages(),
    scripts=['openvpn_test/openvpn-test'],
    python_requires='>=3.6'
)