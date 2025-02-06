import uuid
import json

# Function to generate the UUID and create the message
def generate_order_message():
    order_id = str(uuid.uuid4())  # Generate a random UUID as a string
    
    message = {
        "orderId": order_id,
        "orderUpdateId": 0,
        "version": "2.0.0",
        "manufacturer": "OSRF",
        "serialNumber": "TB3_1",
        "nodes": [
            {
                "nodeId": "node1",
                "released": True,
                "sequenceId": 0,
                "nodePosition": {
                    "x": 2.0,
                    "y": 0.95,
                    "theta": -0.66,
                    "mapId": "map"
                },
                "actions": []
            },
            {
                "nodeId": "node2",
                "released": True,
                "sequenceId": 2,
                "nodePosition": {
                    "x": 1.18,
                    "y": -1.76,
                    "theta": 0.0,
                    "mapId": "map"
                },
                "actions": []
            },
            {
                "nodeId": "node3",
                "released": True,
                "sequenceId": 4,
                "nodePosition": {
                    "x": -0.38,
                    "y": 1.89,
                    "theta": 0.0,
                    "mapId": "map"
                },
                "actions": []
            },
            {
                "nodeId": "node4",
                "released": True,
                "sequenceId": 6,
                "nodePosition": {
                    "x": -0.17,
                    "y": 1.74,
                    "theta": -2.6,
                    "mapId": "map"
                },
                "actions": []
            },
            {
                "nodeId": "node1",
                "released": True,
                "sequenceId": 8,
                "nodePosition": {
                    "x": 2.0,
                    "y": 0.95,
                    "theta": -0.66,
                    "mapId": "map"
                },
                "actions": []
            }
        ],
        "edges": [
            {
                "edgeId": "edge1",
                "released": True,
                "sequenceId": 1,
                "startNodeId": "node1",
                "endNodeId": "node2",
                "actions": []
            },
            {
                "edgeId": "edge2",
                "released": True,
                "sequenceId": 3,
                "startNodeId": "node2",
                "endNodeId": "node3",
                "actions": []
            },
            {
                "edgeId": "edge3",
                "released": True,
                "sequenceId": 5,
                "startNodeId": "node3",
                "endNodeId": "node4",
                "actions": []
            },
            {
                "edgeId": "edge4",
                "released": True,
                "sequenceId": 7,
                "startNodeId": "node4",
                "endNodeId": "node1",
                "actions": []
            }
        ]
    }
    
    # Convert the message to a JSON string
    return json.dumps(message, indent=4)


# Generate the order message and print it
order_message = generate_order_message()
print(order_message)
