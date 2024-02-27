import rclpy
from rclpy.node import Node

from std_msgs.msg import Float64

from geometry_msgs.msg import Twist



class Assinante(Node):
    def __init__(self):
        super().__init__('Assinante')
        self.get_logger().info('Escutando topico')
        self._assinatura = self.create_subscription(Twist, "velocidade",self.callback,10)
        self._publicador2 = self.create_publisher(Float64, "modulo",10)
        self._publicador3 = self.create_publisher(Float64, "modulo2",10)
        pass



    def callback(self, msg):
        lx = msg.linear.x
        ly = msg.linear.y
        lz = msg.linear.z
        tl = Float64()
        tl.data = lx**2 + ly**2 + lz**2
        tl.data = tl.data**(1/2)
        ax = msg.angular.x
        ay = msg.angular.y
        az = msg.angular.z
        ta = Float64()
        ta.data = ax**2 + ay**2 + az**2
        ta.data = ta.data**(1/2)
        

        

        self._publicador2.publish(tl)
        self._publicador3.publish(ta)

       

        pass



def main(args=None):
    rclpy.init(args=args)
    assinante = Assinante()
    rclpy.spin(assinante)
    rclpy.shutdown()



    if __name__ == '__main__':
        main()