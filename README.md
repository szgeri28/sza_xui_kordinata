# sza_xui_kordinata

## Leírás

Ez a ROS 2 Python package két node-ból áll:

* **coordinate_publisher**: Véletlenszerű koordinátákat generál egy `geometry_msgs/Point` típusú topicra.
* **distance_subscriber**: Feliratkozik a koordinátákat tartalmazó topicra, és kiszámolja a távolságot az origótól.

---

## Követelmények

* ROS 2 Humble
* Python 3.10+
* `rclpy`, `geometry_msgs` csomagok

---

## Telepítés

1. Helyezd a package-et a ROS 2 workspace `src` mappájába:

```bash
cd ~/ros2_ws/src
# Másold ide a sza_xui_kordinata mappát
```

2. Buildeld a package-et:

```bash
cd ~/ros2_ws
colcon build --packages-select sza_xui_kordinata --symlink-install
source install/setup.bash
```

---

## Futtatás

### Parancssori futtatás

```bash
ros2 run sza_xui_kordinata coordinate_publisher
ros2 run sza_xui_kordinata distance_subscriber
```

### Launch fájllal (ha létrehozol egyet)

```bash
ros2 launch sza_xui_kordinata coords_launch.py
```

---

## Node-ok és topic kapcsolat

```mermaid
graph LR
    coordinate_publisher -->|geometry_msgs/Point| distance_subscriber
```

* `coordinate_publisher` küldi a véletlenszerű koordinátákat
* `distance_subscriber` figyeli a topicot és számolja a távolságot




---

## Megjegyzés

* A `coordinate_publisher` node véletlenszerű koordinátákat generál.
* A `distance_subscriber` folyamatosan figyeli a topicot, és logolja a távolságot az origótól.
