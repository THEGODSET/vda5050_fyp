####################
### Utility File ###
####################

# Timestamp, assigning parameters, text conversion, vda5050 ros2 and mqtt topic
# Recoded to reduce functions and increase capabilities

from datetime import datetime, timezone
import re
import json
from rclpy.node import Node
from rcl_interfaces.msg import ParameterDescriptor
from rcl_interfaces.msg import ParameterType
from rosidl_runtime_py import message_to_ordereddict


# Get timestamp in VDA5050 format

def get_vda5050_ts():
    """
    Generate timestamp string using VDA5050 required format.

    The timestamp is in format ISO 8601 (UTC)
    YYYY-MM-DDTHH:mm:ss.ssZ (e.g.“2017-04-15T11:40:03.12Z”)

    Returns
    -------
        str: ISO 8601 UTC timestamp YYYY-MM-DDTHH:mm:ss.ssZ

    """
    ts = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3]+'Z'

    return ts

# Read and assign parameter

def read_parameter(node: Node, param_name: str, alternative, param_type: type):
    """Declare and read parameter."""

    type_map = {
        bool: ParameterType.PARAMETER_BOOL,
        int: ParameterType.PARAMETER_INTEGER,
        float: ParameterType.PARAMETER_DOUBLE,
        str: ParameterType.PARAMETER_STRING,
        list: ParameterType.PARAMETER_STRING_ARRAY,
    }

    if param_type not in type_map:
        raise ValueError(f"Unsupported parameter type: {param_type}")
    
    # Check if the parameter has already been declared
    if not node.has_parameter(param_name):
        descriptor = ParameterDescriptor(type=type_map[param_type])
        node.declare_parameter(param_name, alternative, descriptor)

    
    
    param = node.get_parameter(param_name).get_parameter_value()
    
    if param_type == bool:
        return param.bool_value
    elif param_type == int:
        return param.integer_value
    elif param_type == float:
        return param.double_value
    elif param_type == str:
        return param.string_value
    elif param_type == list:
        return param.string_array_value

# Camel / Snake Case Conversion

def json_camel_to_snake_case(s):
    """
    Convert camel case JSON message to snake case.

    Converts all JSON message keys recursively from camel case to snake
    case e.g. camelCase to camel_case. Used to transform VDA5050 messages
    from MQTT topics to ROS2 vda5050_msgs

    Args:
    ----
        s (str|bytes): JSON message as string or bytes

    """
    def snake_case_dict(obj):
        """
        Replace dict camelCase keys by its snake case equivalent.

        Args
        ----
        obj (dict): dict object to replace keys

        Returns
        -------
        str: dictionary with all snake case keys

        """
        for key in obj.copy():
            new_key = re.sub(r"(?<!^)(?=[A-Z])", "_", key).lower()
            if new_key != key:
                obj[new_key] = obj[key]
                del obj[key]
        return obj

    return json.loads(s, object_hook=snake_case_dict)

def json_snake_to_camel_case(s):
    """
    Convert snake case JSON message to camel case.

    Converts all JSON message keys recursively from snake case to camel
    case e.g. snake_case to snakeCase. Used to transform ROS2 vda5050_msgs
    messages to VDA5050 MQTT messages.

    Args:
    ----
        s (str|bytes): JSON message as string or bytes

    """
    def to_camel_case(snake_str):
        """
        Convert snake case string to camel case.

        Args
        ----
            snake_str (str): snake case string.

        Returns
        -------
            str: camel case string.

        """
        components = snake_str.split("_")
        # Capitalize the first letter of each component except the first
        # one with the 'title' method and join them together.
        return components[0] + "".join(x.title() for x in components[1:])

    def camel_case_dict(obj):
        """
        Replace dict snake_case keys by its camel case equivalent.

        Args
        ----
            obj (dict): dict object to replace keys

        Returns
        -------
            str: dictionary with all camel case keys

        """
        for key in obj.copy():
            new_key = to_camel_case(key)
            if new_key != key:
                obj[new_key] = obj[key]
                del obj[key]
        return obj

    return json.loads(s, object_hook=camel_case_dict)

# ROS to JSON

def convert_ros_message_to_json(msg):
    """
    Convert a ROS2 message into a JSON for MQTT publishing.

    Args:
    ----
        msg (Any): VDA5050 ROS2 message

    Returns
    -------
        dict: JSON representation of the ROS2 msg

    """
    json_msg = json.dumps(message_to_ordereddict(msg))
    return json.dumps(json_snake_to_camel_case(json_msg))

# VDA MQTT / ROS Topic

def vda5050_topic(
    version_protocol, manufacturer, serial_number, topic, platform):
    """
    Return suggested VDA5050 MQTT topics.

    Even though the topic structure is not strictly defined, the
    VDA5050 standard suggests topic levels as follows:

    ``interfaceName/majorVersion/manufacturer/serialNumber/topic``
    Example: uagv/v2/KIT/0001/order

    Note: Since the ``/`` character is used to define topic hierarchies, it
    must not be used in any of the aforementioned fields. The ``$`` character
    is also used in some MQTT brokers for special internal topics, so it should
    not be used either.

    Args
    ----
        manufacturer (string): Robot manufacturer
        serial_number (string): Unique robot serial number consisting of the following
            characters: ``A-Z a-z 0-9 _ - . :``
        topic (string): Subtopic for communication.
        interface_name (str, optional): Name of the used interface. Defaults to "uagv".
        major_version (str, optional): Major version number, preceded by "v". Defaults to "v1".

    Raises
    ------
        ValueError: on invalid ``topic``
        ValueError: on invalid ``major_version``

    Returns
    -------
        string: MQTT topic

    """
    if topic not in [
        "order",
        "state",
        "visualization",
        "instantActions",
        "connection",
        "factsheet",
    ]:
        raise ValueError(f"Invalid VDA5050 topic: {topic}")

    major_version = "v" + str(version_protocol).split(".")[0]

    # if len(major_version) != 2 or not major_version.startswith("v"):
    #     raise ValueError(
    #         "Invalid protocol major version. Expected an integer"
    #         f" preceded by 'v', but got {major_version}"
    #     )

    if platform not in [
        "mqtt",
        "ros2",
    ]:
        raise ValueError(f"Invalid VDA5050 Platform: {platform}")
    
    if platform == "mqtt":
        platform_topic = f"{major_version}/{manufacturer}/{serial_number}/{topic}"
    elif platform == "ros2":
        platform_topic = f"/{major_version}/{manufacturer}/{serial_number}/{topic}"
    
    return platform_topic

############################################
####                                     ###
#### Removed codes from Script Version 1 ###
####                                     ###
############################################

# def read_bool_parameter(node: Node, param_name: str, alternative: bool) -> bool:
#     """Declare and read a bool parameter."""
#     node.declare_parameter(
#         param_name,
#         descriptor=ParameterDescriptor(type=ParameterType.PARAMETER_BOOL),
#         value=alternative,
#     )
#     param = node.get_parameter(param_name)
#     return param if type(param) == bool else param.get_parameter_value().bool_value

# def read_int_parameter(node: Node, param_name: str, alternative: int) -> int:
#     """Declare and read a int parameter."""
#     node.declare_parameter(
#         param_name,
#         descriptor=ParameterDescriptor(type=ParameterType.PARAMETER_INTEGER),
#         value=alternative,
#     )
#     param = node.get_parameter(param_name)
#     return param if type(param) == int else param.get_parameter_value().integer_value


# def read_double_parameter(node: Node, param_name: str, alternative: float) -> float:
#     """Declare and read a double (float) parameter."""
#     node.declare_parameter(
#         param_name,
#         descriptor=ParameterDescriptor(type=ParameterType.PARAMETER_DOUBLE),
#         value=alternative,
#     )
#     param = node.get_parameter(param_name)
#     return param if type(param) == float else param.get_parameter_value().double_value


# def read_str_array_parameter(node: Node, param_name: str, alternative: list) -> list:
#     """Declare and read a string array parameter."""
#     node.declare_parameter(
#         param_name,
#         descriptor=ParameterDescriptor(type=ParameterType.PARAMETER_STRING_ARRAY),
#         value=alternative,
#     )
#     param = node.get_parameter(param_name)
#     return param if type(param) == list else param.get_parameter_value().string_array_value


# def get_vda5050_ros2_topic(
#     manufacturer, serial_number, topic, version_protocol):
#     """
#     Return ROS2 topics used for communication between controller and adapter.

#     Note that these topics follow the same structure as the one defined on the
#     VDA5050 standard, but preceded by ``/``.

#     Example: /uagv/v2/KIT/0001/order


#     Args
#     ----
#         manufacturer (string): Robot manufacturer
#         serial_number (string): Unique robot serial number consisting of the following
#             characters: ``A-Z a-z 0-9 _ - . :``
#         topic (string): Subtopic for communication.
#         interface_name (str, optional): Name of the used interface. Defaults to "uagv".
#         major_version (str, optional): Major version number, preceded by "v". Defaults to "v1".

#     Raises
#     ------
#         ValueError: on invalid ``topic``
#         ValueError: on invalid ``major_version``

#     Returns
#     -------
#         string: MQTT topic

#     """
#     mqtt_topic = get_vda5050_mqtt_topic(
#         manufacturer, serial_number, topic, major_version, interface_name)
#     return (
#         f"/{mqtt_topic}"
#     )
