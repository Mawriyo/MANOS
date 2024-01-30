#!/bin/bash

install_ros() {
    sudo apt update && sudo apt install -y locales
    sudo locale-gen en_US en_US.UTF-8
    sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
    export LANG=en_US.UTF-8
    sudo apt install -y software-properties-common
    sudo add-apt-repository -y universe
    sudo apt update && sudo apt install -y curl
    sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg
    echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null
    sudo apt update
    sudo apt upgrade -y
    sudo apt install -y ros-galactic-desktop
    sudo apt install python3-colcon-common-extensions -y 
    source /opt/ros/galactic/setup.sh
    colcon build
    pip install cvzone mediapipe opencv-python -y
    
}

uninstall_ros() {
    sudo apt remove -y ~nros-galactic-*
    sudo apt autoremove -y
    sudo rm /etc/apt/sources.list.d/ros2.list
    sudo apt update
    sudo apt autoremove -y
    sudo apt upgrade -y
}

case "$1" in
    --install)list
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
