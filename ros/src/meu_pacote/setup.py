from setuptools import find_packages, setup

package_name = 'meu_pacote'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='dutdudu',
    maintainer_email='dudunassif2004@gmail.com',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "ola = meu_pacote.ola:main",
            "publicador = meu_pacote.publisher:main",
            "assinante = meu_pacote.subscriber:main"
        ],
    },
)
