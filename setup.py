from setuptools import find_packages, setup

package_name = 'my_robot'

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
    maintainer='arun',
    maintainer_email='your@email.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
        'publisher = my_robot.publisher:main',
        'subscriber = my_robot.subscriber:main',
        'turtlebot_controller = my_robot.turtlebot:main',
        'turtlebot_subscriber = my_robot.turtle_subscriber:main',
        'turtle_control = my_robot.turtle_controller:main',
        'square = my_robot.square:main',
        'star = my_robot.star:main',
        'multirobot_publisher = my_robot.multi_robot_publisher:main',
        'multirobot = my_robot.multirobot_sub:main',
        'sub = my_robot.sub:main',
        'service = my_robot.service:main',
                ],
    },
)
