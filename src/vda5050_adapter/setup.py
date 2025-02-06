from glob import glob
from setuptools import find_packages, setup

package_name = 'vda5050_adapter'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + "/launch", glob('launch/*launch.[pxy][yma]*')),
        ('share/' + package_name + "/config", glob('config/*.yaml')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Arvin Ravindran',
    maintainer_email='arvin19112002@gmail.com',
    description='VDA5050 adapter for Monkey Robotics',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'adapter = vda5050_adapter.adapter:main',
            'odometry = vda5050_adapter.odom_position:main',
            'goal = vda5050_adapter.goal_adapter:main'
        ],
    },
)
