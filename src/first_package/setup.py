from setuptools import find_packages, setup

package_name = 'first_package'

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
    maintainer='mo',
    maintainer_email='mo@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "simple_publisher_node = first_package.simple_publisher:main",
            "simple_subscriber_node = first_package.simple_subscriber:main",
            "simple_subpub_node = first_package.combo_node:main"
        ],
    },
)
