import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry
from tf2_ros import Buffer, TransformListener, TransformException
import tf_transformations

from vda5050_msgs.msg import AGVPosition as VDAAGVPosition

class OdomCallbackNode(Node):
    def __init__(self):
        super().__init__("odom_callback_node")
        
        # Initialize the AGV position message
        self._agv_position = VDAAGVPosition()
        
        # Initialize TF buffer and listener
        self._tf_buffer = Buffer()
        self._tf_listener = TransformListener(self._tf_buffer, self)
        
        # Subscriber to Odometry
        self._odom_sub = self.create_subscription(
            Odometry,
            "/odom",
            self.odom_callback,
            10
        )
        
        # Store map_id (fixed to 'map' for simplicity)
        self._agv_position.map_id = "map"

    def odom_callback(self, odom_msg: Odometry):
        # Define the frames to transform between
        to_frame = "map"
        from_frame = "base_link"
        
        try:
            # Get the current transformation from base_link to map
            now = self.get_clock().now()
            trans = self._tf_buffer.lookup_transform(to_frame, from_frame, now)
            
            # Extract position from the transformation and set it in AGVPosition message
            self._agv_position.x = trans.transform.translation.x
            self._agv_position.y = trans.transform.translation.y
            
            # Extract orientation and convert to Euler angles
            q = trans.transform.rotation
            _, _, theta = tf_transformations.euler_from_quaternion((q.x, q.y, q.z, q.w))
            self._agv_position.theta = theta
            
            # Log the AGV position
            self.get_logger().info(f"AGV Position: x={self._agv_position.x}, y={self._agv_position.y}, theta={self._agv_position.theta}")
        
        except TransformException as ex:
            self.get_logger().warn(f"Could not transform {to_frame} to {from_frame}: {ex}")
            return

def main(args=None):
    rclpy.init(args=args)
    odom_callback_node = OdomCallbackNode()
    rclpy.spin(odom_callback_node)
    odom_callback_node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
