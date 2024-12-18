from setuptools import find_packages, setup

import os
from glob import glob

package_name = 'stm_station'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob("launch/*.py"))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='mo',
    maintainer_email='applednd2002@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "stm_serial_node_pub = stm_station.SerialPublisherNode:main",
            "stm_serial_node_pubsub = stm_station.SerialPubSubNode:main",
            "stm_serial_command_pub = stm_station.CommandPublisher:main" 
            ]
    })