from setuptools import find_packages, setup
from glob import glob
import os

package_name = 'sza_xui_kordinata'

setup(
    name=package_name,
    version='0.0.1',
    packages=find_packages('src'),      # <--- itt nézze a src mappát
    package_dir={'': 'src'},            # <--- és innen vegye a csomagokat
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*launch.[pxy][yma]*')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Szabo Gergely',
    maintainer_email='szabogeri*@gmail.com',
    description='Publishes random coordinates and computes distance from origin.',
    license='GNU General Public License v3.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'coordinate_publisher = sza_xui_kordinata.coordinate_publisher:main',
            'distance_subscriber = sza_xui_kordinata.distance_subscriber:main'
        ],
    },
)