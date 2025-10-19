import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Point
import random


class CoordinatePublisher(Node):
    def __init__(self):
        super().__init__('coordinate_publisher')
        self.publisher_ = self.create_publisher(Point, 'coordinates', 10)
        timer_period = 0.5  # másodpercenként küld egy pontot
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.get_logger().info("Coordinate Publisher node started")

    def timer_callback(self):
        msg = Point()
        msg.x = random.uniform(-10.0, 10.0)
        msg.y = random.uniform(-10.0, 10.0)
        msg.z = 0.0
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing point: x={msg.x:.2f}, y={msg.y:.2f}')


def main(args=None):
    rclpy.init(args=args)
    node = CoordinatePublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()