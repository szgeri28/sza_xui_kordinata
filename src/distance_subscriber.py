import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Point
import math


class DistanceSubscriber(Node):
    def __init__(self):
        super().__init__('distance_subscriber')
        self.subscription = self.create_subscription(
            Point,
            'coordinates',
            self.listener_callback,
            10)
        self.get_logger().info("Distance Subscriber node started")

    def listener_callback(self, msg):
        distance = math.sqrt(msg.x**2 + msg.y**2)
        self.get_logger().info(
            f'Received point: ({msg.x:.2f}, {msg.y:.2f}) → Distance from origin: {distance:.2f}'
        )


def main(args=None):
    rclpy.init(args=args)
    node = DistanceSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()