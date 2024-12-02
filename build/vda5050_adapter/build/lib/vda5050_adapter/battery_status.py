import rclpy
from rclpy.node import Node
from sensor_msgs.msg import BatteryState
import paho.mqtt.client as mqtt
import json

class BatteryStatusAdapter(Node):
    def __init__(self, mqtt_topic=None):
        super().__init__('battery_status_adapter')
        
        # Initialize ROS 2 publisher for battery status
        self.battery_publisher = self.create_publisher(BatteryState, '/battery_status', 10)

        # Initialize MQTT client if a topic is provided
        self.mqtt_topic = mqtt_topic
        if self.mqtt_topic:
            self.mqtt_client = mqtt.Client()
            # self.mqtt_client.username_pw_set("your_username", "your_password")  # Add authentication if needed
            self.mqtt_client.connect("localhost", 1883)
            self.mqtt_client.subscribe(self.mqtt_topic)
            self.mqtt_client.on_message = self.on_mqtt_message
            self.mqtt_client.loop_start()

        # Start a timer to publish battery status periodically (e.g., every 1 second)
        self.timer = self.create_timer(1.0, self.publish_battery_status)

    def on_mqtt_message(self, client, userdata, message):
        try:
            # Decode incoming MQTT message
            data = json.loads(message.payload.decode())
            self.get_logger().info(f"Received battery status update: {data}")

            # Assuming the message contains battery information
            voltage = data.get('voltage', 0.0)
            current = data.get('current', 0.0)
            charge = data.get('charge', 0.0)
            percentage = data.get('percentage', 0.0)

            # Publish this data to ROS 2 topic
            self.publish_battery_status(voltage, current, charge, percentage)
        except Exception as e:
            self.get_logger().error(f"Error processing MQTT message: {e}")

    def publish_battery_status(self, voltage=None, current=None, charge=None, percentage=None):
        # Create a BatteryState message
        battery_msg = BatteryState()

        # Set default values if none are provided
        if voltage is None: voltage = 12.5  # Replace with actual reading or defaults
        if current is None: current = 1.5  # Replace with actual reading or defaults
        if charge is None: charge = 50.0  # Replace with actual reading or defaults
        if percentage is None: percentage = 80.0  # Replace with actual reading or defaults

        battery_msg.voltage = voltage
        battery_msg.current = current
        battery_msg.charge = charge
        battery_msg.percentage = percentage

        # Optionally, you can add more battery parameters based on your system

        # Publish the battery status
        self.battery_publisher.publish(battery_msg)
        self.get_logger().info(f"Published battery status: Voltage={voltage}V, Current={current}A, Charge={charge}mAh, Percentage={percentage}%")

def main(args=None, mqtt_topic=None):
    rclpy.init(args=args)
    battery_adapter_node = BatteryStatusAdapter(mqtt_topic=mqtt_topic)

    # Keep the node running
    rclpy.spin(battery_adapter_node)

    # Cleanup
    battery_adapter_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    # If you want to pass the MQTT topic dynamically, you can call main with an argument.
    # Example: python3 battery_status_adapter.py "battery/status"
    import sys
    if len(sys.argv) > 1:
        main(mqtt_topic=sys.argv[1])  # Pass topic as command line argument
    else:
        main()
