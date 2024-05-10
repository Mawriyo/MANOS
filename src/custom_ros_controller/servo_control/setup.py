from setuptools import setup

package_name = 'servo_control'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/srv', ['srv/SetServo.srv']),
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='your_name',
    maintainer_email='your_email@example.com',
    description='A ROS 2 package for controlling servos via services using Adafruit PCA9685.',
    entry_points={
        'console_scripts': [
            'servo_service = servo.servo_service_node:main',
        ],
    },
)
