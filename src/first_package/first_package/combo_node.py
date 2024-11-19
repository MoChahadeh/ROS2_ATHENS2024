import rclpy
from rclpy.node import Node
from std_msgs.msg import String  # Import the String message type


class MinimalSubPub(Node):

    def __init__(self): 

        super().__init__("node_combo")
        
        
        self.publisher_ = self.create_publisher(String, 'topic_combo', 10)  # <-- Replace '10'
        
        # Step 3: Set a timer to publish messages at a chosen frequency
        # Modify 'timer_period' to control how often messages are published (e.g., 2.0 for every 2 seconds)
        # timer_period = 2.0  # <-- You can change this to another value like 1.5 or 3.0
        # self.timer = self.create_timer(timer_period, self.timer_callback)
        
        # Step 4: Initialize a counter to keep track of message numbers
        self.i = 0  # Starts counting from 0


        self.subscription = self.create_subscription(
            String,             # Message type used by the publisher
            'topic_publisher',  # <-- Replace 'ID10' with the specific topic name for your group
            self.listener_callback,  
            10)  # Queue size for incoming messages
        self.subscription  # Prevent unused variable warning
        
        self.sub_msg = ""
        
    def listener_callback(self, msg):
        # Log the received message to the console
        self.sub_msg = msg
        self.get_logger().info(f'Received: "{msg.data}"')
        self.timer_callback()


    # Step 5: Define the callback function that will be called by the timer
    def timer_callback(self):
        # Create a new String message
        msg = String()
        
        # Customize the message data with a unique message
        # Modify the message content to include your group number and a custom message
        msg.data = f"This is the combo node and I heard this: {self.sub_msg.data} #{self.i}"  # <-- Replace '10'
        
        # Publish the message
        self.publisher_.publish(msg)
        
        # Log the published message to the console
        self.get_logger().info(f'Publishing: "{msg.data}"')
        
        # Increment the message counter
        self.i += 1


# Step 6: Define the main function to run the node
def main(args=None):
    # Initialize the ROS2 Python client library
    rclpy.init(args=args)
    
    # Create an instance of the MinimalPublisher node
    minimal_publisher = MinimalSubPub()

    try:
        # Run the node until interrupted
        rclpy.spin(minimal_publisher)
    except KeyboardInterrupt:
        # Gracefully handle shutdown when Ctrl+C is pressed
        pass
    finally:
        # Destroy the node and shutdown the ROS2 Python client library
        minimal_publisher.destroy_node()
        rclpy.shutdown()

# Entry point of the script
if __name__ == '__main__':
    main()




    
