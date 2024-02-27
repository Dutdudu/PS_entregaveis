import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist

from std_msgs.msg import Float64


class Publicador(Node):
    def __init__(self):
        super().__init__('publicador')
        self.get_logger().info('Publicador iniciado')
        
        self._publicador = self.create_publisher(Twist, "velocidade",10)
        self._assinatura2 = self.create_subscription(Float64, "modulo",self.callback2,10)
        self._assinatura3 = self.create_subscription(Float64, "modulo2",self.callback3,10)

        self.create_timer(1, self.callback)



    def callback(self):
        msg = Twist()
        msg.linear.x = 1.7
        msg.linear.y = 1.5
        msg.linear.z = 2.2
        msg.angular.x = 0.3
        msg.angular.y = 2.7
        msg.angular.z = 3.7
        
        self._publicador.publish(msg)

    def callback3(self,tl):
      
        print(f'A velociade linear eh: {tl.data:.2f}')

    def callback2(self,ta):
      
        print(f'A velociade angular eh: {ta.data:.2f}')





def main(args=None):
    rclpy.init(args=args)
    publicador = Publicador()
    rclpy.spin(publicador)
    rclpy.shutdown()



    if __name__ == '__main__':
        main()



