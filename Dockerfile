FROM ros:galactic

RUN apt-get update && apt-get install -y \
    build-essential \
    python3-colcon-common-extensions \
    python3-rosdep \
    && rm -rf /var/lib/apt/lists/*

RUN  rosdep update

WORKDIR /root/ros_ws
COPY ./src ./src

RUN rosdep install --from-paths src --ignore-src -r -y

RUN /bin/bash -c '. /opt/ros/galactic/setup.bash; colcon build'

RUN echo "hello"
