# 🤖 ROS 2 Python Learning Repository

A hands-on **ROS 2 learning repository** focused on understanding the fundamentals of robot software development using **Python**.

This repository contains progressively organized examples covering ROS 2 nodes, publishers, subscribers, services, TurtleBot control, robot communication, and multi-robot concepts.

The main ROS 2 Python package used in this repository is:

```text
my_robot
```

---

## 📚 What I Am Learning

This repository is being developed while learning the core concepts of **ROS 2**.

The main topics include:

* ROS 2 workspace and package structure
* Python ROS 2 packages
* Nodes
* Publishers and Subscribers
* Topics
* Services
* Robot control
* TurtleBot communication
* Multi-robot communication
* ROS 2 executable entry points
* Building and running ROS 2 Python packages

The goal is to understand how individual ROS 2 components communicate and how these concepts can later be applied to autonomous robotics systems.

---

## 🗂️ Package Structure

The main package is:

```text
my_robot/
├── publisher.py
├── subscriber.py
├── turtlebot.py
├── turtle_subscriber.py
├── turtle_controller.py
├── square.py
├── star.py
├── multi_robot_publisher.py
├── multirobot_sub.py
├── sub.py
├── service.py
├── package.xml
├── setup.py
└── resource/
```

The exact implementation of each Python file may evolve as the learning exercises progress.

---

## ⚙️ ROS 2 Package Configuration

The package is configured as a Python package using `setuptools`.

The package name is:

```text
my_robot
```

The `setup.py` configuration registers multiple ROS 2 command-line executables, including:

```text
publisher
subscriber
turtlebot_controller
turtlebot_subscriber
turtle_control
square
star
multirobot_publisher
multirobot
sub
service
```

These are exposed through ROS 2's `console_scripts` entry points.

---

## 🛠️ Requirements

You need a working ROS 2 installation with Python support.

Recommended environment:

```text
Ubuntu
ROS 2
Python 3
colcon
ament_python
```

Make sure ROS 2 is sourced before building or running the package.

For example:

```bash
source /opt/ros/<your_ros2_distribution>/setup.bash
```

Replace `<your_ros2_distribution>` with the ROS 2 distribution installed on your system.

---

## 📦 Create a ROS 2 Workspace

If you are starting from scratch:

```bash
mkdir -p ~/ros2_ws/src
cd ~/ros2_ws/src
```

Clone this repository inside the `src` directory:

```bash
git clone <YOUR_REPOSITORY_URL>
```

Then return to the workspace:

```bash
cd ~/ros2_ws
```

---

## 🔨 Build the Package

Build the ROS 2 workspace using:

```bash
colcon build
```

After a successful build, source the workspace:

```bash
source install/setup.bash
```

It is useful to source the workspace again whenever you open a new terminal:

```bash
source ~/ros2_ws/install/setup.bash
```

---

## ▶️ Running the Examples

After building and sourcing the workspace, ROS 2 executables can be launched using:

```bash
ros2 run my_robot <executable>
```

### Publisher

```bash
ros2 run my_robot publisher
```

### Subscriber

```bash
ros2 run my_robot subscriber
```

### TurtleBot Controller

```bash
ros2 run my_robot turtlebot_controller
```

### Turtle Subscriber

```bash
ros2 run my_robot turtlebot_subscriber
```

### Turtle Control

```bash
ros2 run my_robot turtle_control
```

### Square

```bash
ros2 run my_robot square
```

### Star

```bash
ros2 run my_robot star
```

### Multi-Robot Publisher

```bash
ros2 run my_robot multirobot_publisher
```

### Multi-Robot

```bash
ros2 run my_robot multirobot
```

### Subscriber Example

```bash
ros2 run my_robot sub
```

### Service Example

```bash
ros2 run my_robot service
```

These executable names are defined in the package's `setup.py`.

---

## 🧠 ROS 2 Concepts

### 1. Nodes

A **node** is an individual process in a ROS 2 system responsible for performing a particular task.

Examples in this repository are implemented as Python executables.

---

### 2. Topics

Topics allow ROS 2 nodes to communicate using a publish/subscribe model.

A typical communication flow is:

```text
Publisher Node
      │
      │ Topic
      ▼
Subscriber Node
```

For example:

```text
publisher.py  →  Topic  →  subscriber.py
```

---

### 3. Publishers

A publisher sends messages to a ROS 2 topic.

Example execution:

```bash
ros2 run my_robot publisher
```

---

### 4. Subscribers

A subscriber receives messages from a ROS 2 topic.

Example:

```bash
ros2 run my_robot subscriber
```

---

### 5. Services

ROS 2 services provide request/response communication.

This repository includes a service example exposed as:

```bash
ros2 run my_robot service
```

---

### 6. Robot Control

The repository also contains Python examples related to TurtleBot control:

```text
turtlebot.py
turtle_subscriber.py
turtle_controller.py
```

These examples are intended for learning how ROS 2 communication can be connected to robot movement and control.

---

### 7. Multi-Robot Communication

The repository contains examples for experimenting with communication between multiple robots:

```text
multi_robot_publisher.py
multirobot_sub.py
```

The corresponding executables are:

```bash
ros2 run my_robot multirobot_publisher
```

and

```bash
ros2 run my_robot multirobot
```

---

## 🔍 Useful ROS 2 Commands

### List available nodes

```bash
ros2 node list
```

### List topics

```bash
ros2 topic list
```

### Inspect a topic

```bash
ros2 topic info /topic_name
```

### Echo topic messages

```bash
ros2 topic echo /topic_name
```

### List services

```bash
ros2 service list
```

### List available packages

```bash
ros2 pkg list
```

### Check package

```bash
ros2 pkg executables my_robot
```

This is particularly useful for verifying that the Python executables have been correctly installed.

---

## 🔄 Typical Development Workflow

The basic workflow I am following while learning ROS 2 is:

```text
Write Python Node
       ↓
Add Node to ROS 2 Package
       ↓
Configure setup.py
       ↓
Build with colcon
       ↓
Source workspace
       ↓
Run ROS 2 executable
       ↓
Inspect nodes/topics/services
       ↓
Test communication
       ↓
Modify and experiment
```

---

## 🎯 Learning Roadmap

This repository will gradually expand as I learn more ROS 2 concepts.

### Completed / Practicing

* [x] ROS 2 workspace basics
* [x] Python package structure
* [x] `setup.py`
* [x] ROS 2 executable entry points
* [x] Publisher concepts
* [x] Subscriber concepts
* [x] Topic communication
* [x] Service concepts
* [x] TurtleBot examples
* [x] Basic multi-robot communication

### Next Steps

* [ ] Launch files
* [ ] Parameters
* [ ] Custom ROS 2 messages
* [ ] Custom services
* [ ] TF2
* [ ] URDF
* [ ] RViz2
* [ ] Gazebo / simulation
* [ ] ROS 2 navigation
* [ ] Nav2
* [ ] SLAM
* [ ] Sensors and LiDAR
* [ ] Autonomous navigation
* [ ] ROS 2 + AI/Computer Vision

---

## 🧪 Purpose of This Repository

This is primarily a **learning and experimentation repository**.

The objective is to build a strong foundation in ROS 2 before moving toward more advanced robotics topics such as:

```text
ROS 2
 ↓
Simulation
 ↓
Sensors
 ↓
TF2
 ↓
SLAM
 ↓
Navigation
 ↓
Autonomous Robots
 ↓
AI + Robotics
```

---

## 👨‍💻 Author

**Arun M.**

B.Tech Robotics & Automation

Interested in:

* Robotics
* ROS 2
* Autonomous Systems
* Robot Navigation
* Computer Vision
* Physical AI
* Robot Learning

---

## ⭐ Repository Status

🚧 **Learning in Progress**

This repository will continue to evolve as new ROS 2 concepts, experiments, and robotics projects are added.
