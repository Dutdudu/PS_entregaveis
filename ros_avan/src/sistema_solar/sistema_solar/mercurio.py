import rclpy
import random
import math

from rclpy.node import Node

from tf2_ros import TransformBroadcaster

from geometry_msgs.msg import TransformStamped


class Mercurio(Node):
    def __init__(self):
        super().__init__('Mercurio')
        self.get_logger().info('Mercurio iniciado')
        self._broadcaster = TransformBroadcaster(self)
        
        self.declare_parameters(
            namespace ='',
            parameters=[
                ('nome_da_estrela',rclpy.Parameter.Type.STRING),
                ('nome_do_planeta',rclpy.Parameter.Type.STRING),
                ('raio_da_orbita',rclpy.Parameter.Type.INTEGER),
            ]
        )

        self.timer = self.create_timer(0.125,self.callback)
        #self.inicio_no = self.get_clock().now()

        self.angulo = 0
        self.raio = self.get_parameter('raio_da_orbita').get_parameter_value().integer_value
    def callback(self):

        #time = self.get_clock().now().seconds_nanoseconds()
        #seconds = time[0] - self.inicio_no.seconds_nanoseconds()[0]
        
        

        x = self.raio * math.cos(self.angulo)
        y = self.raio * math.sin(self.angulo)

        
        self.parametro_string = self.get_parameter('nome_da_estrela').get_parameter_value().string_value
        self.parametro_string2 = self.get_parameter('nome_do_planeta').get_parameter_value().string_value
        t = TransformStamped()

        t.header.stamp = self.get_clock().now().to_msg()
        t.header.frame_id = self.parametro_string
        t.child_frame_id = self.parametro_string2
        t.transform.translation.x = x
        t.transform.translation.y = y
        t.transform.translation.z = 0.0

        t.transform.rotation.x = 0.0
        t.transform.rotation.y = 0.0
        t.transform.rotation.z = 0.0
        t.transform.rotation.w = 1.0
        self._broadcaster.sendTransform(t)

        self.angulo += 0.1
       
            


        


def main(args=None):
    rclpy.init(args=args)
    mercurio = Mercurio()
    rclpy.spin(mercurio)
    rclpy.shutdown()



    if __name__ == '__main__':
        main()