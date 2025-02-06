import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
import math
import paho.mqtt.client as mqtt

class TurtleBotController(Node):
    def __init__(self):
        super().__init__('turtlebot_controller')
        self.publisher = self.create_publisher(Twist, '/turtlebot0/cmd_vel', 10)
        self.create_subscription(Odometry, '/turtlebot0/odom', self.odom_callback, 10)
        
        self.target_x = None
        self.target_y = None

        # MQTT Client Setup
        self.mqtt_client = mqtt.Client()
        self.mqtt_client.on_connect = self.on_connect
        self.mqtt_client.on_message = self.on_message
        self.mqtt_client.connect("broker.hivemq.com", 1883, 60)  # Replace with your broker
        self.mqtt_client.loop_start()

    def on_connect(self, client, userdata, flags, rc):
        self.get_logger().info("Connected to MQTT broker")
        client.subscribe("turtlebot/target")  # MQTT topic for target coordinates

    def on_message(self, client, userdata, msg):
        try:
            data = msg.payload.decode('utf-8').split(',')
            self.target_x = float(data[0])
            self.target_y = float(data[1])
            self.get_logger().info(f"Received target: x={self.target_x}, y={self.target_y}")
        except Exception as e:
            self.get_logger().error(f"Error parsing MQTT message: {e}")

    def odom_callback(self, msg):
        if self.target_x is None or self.target_y is None:
            return

        # Current position
        current_x = msg.pose.pose.position.x
        current_y = msg.pose.pose.position.y

        # Distance to target
        distance = math.sqrt((self.target_x - current_x)**2 + (self.target_y - current_y)**2)

        # If the robot is close enough to the target, stop
        if distance < 0.1:
            self.stop_robot()
            return

        # Velocity command
        cmd = Twist()
        cmd.linear.x = min(0.5, distance)  # Cap speed at 0.5 m/s
        cmd.angular.z = math.atan2(self.target_y - current_y, self.target_x - current_x)
        self.publisher.publish(cmd)

    def stop_robot(self):
        self.target_x = None
        self.target_y = None
        stop_cmd = Twist()
        self.publisher.publish(stop_cmd)

def main():
    rclpy.init()
    controller = TurtleBotController()
    rclpy.spin(controller)
    controller.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
