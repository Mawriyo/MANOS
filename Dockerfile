# Use ROS Galactic official base image
FROM ros:galactic

# Install build tools
RUN apt-get update && apt-get install -y \
    build-essential \
    python3-colcon-common-extensions \
    python3-rosdep \
    && rm -rf /var/lib/apt/lists/*

# Initialize rosdep
RUN  rosdep update

# Create a workspace
WORKDIR /root/ros_ws
COPY ./src ./src

# Your custom packages list
RUN rosdep install --from-paths src --ignore-src -r -y

# Build the workspace
RUN /bin/bash -c '. /opt/ros/galactic/setup.bash; colcon build'

# Setup entrypoint
#CMD ["/bin/bash", "-c", "source /opt/ros/galactic/setup.bash && source /root/ros_ws/install/setup.bash && ros2 launch your_package your_launch_file.launch"]
RUN echo "hello"
