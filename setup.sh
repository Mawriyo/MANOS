#!/bin/bash

# Function to install ROS 2
install_ros() {
    # Set locale
    sudo apt update && sudo apt install locales
    sudo locale-gen en_US en_US.UTF-8
    sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
    export LANG=en_US.UTF-8

    # Setup sources
    sudo apt install software-properties-common
    sudo add-apt-repository universe
    sudo apt update && sudo apt install curl
    sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg
    echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null

    # Install ROS 2 packages
    sudo apt update
    sudo apt upgrade
    sudo apt install ros-galactic-desktop
}

# Function to uninstall ROS 2
uninstall_ros() {
    sudo apt remove ~nros-galactic-* && sudo apt autoremove
    sudo rm /etc/apt/sources.list.d/ros2.list
    sudo apt update
    sudo apt autoremove
    sudo apt upgrade
}

# Main script logic
case "$1" in
    --install)
        install_ros
        ;;
    --uninstall)
        uninstall_ros
        ;;
    *)
        echo "Usage: $0 --install | --uninstall"
        exit 1
        ;;
esac
