import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32MultiArray
from random import random, randint

class CommandPublisher(Node):
    
    def __init__(self):
        super().__init__("stm_command_publisher")
        
        
        self.command_publisher = self.create_publisher(Float32MultiArray, "stm_control", 10)
        
        self.timer = self.create_timer(5, self.timer_callback)

        
    
    def publish_data(self, msg:Float32MultiArray):
        
        self.command_publisher.publish(msg=msg)
        self.get_logger().info("Publishing: "+str(msg.data))
        
        
    def timer_callback(self):
        
        msg = Float32MultiArray()
        
        # format: {control_type, goal_position, Kp, PWM}
        control_type = float(randint(0,2))
        goal_position = float(randint(0, 250)) if control_type == 1 else float(0)
        Kp = float(random()*5) if control_type == 1 else float(0)
        pwm = float(randint(-250, 250)) if control_type == 2 else float(0)
        
        msg.data = [control_type, goal_position, Kp, pwm]
        
        print(msg.data)
        
        self.publish_data(msg)
        
        
def main(args=None):
    rclpy.init(args=args)
    node = CommandPublisher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()

        