import rclpy

from rclpy.node import Node



class Parametros(Node):
    def __init__(self):
        super().__init__('Parametros')
        self.get_logger().info('Parametros iniciado')
        #self.declare_parameter('parametro_inteiro', rclpy.Parameter.Type.INTEGER)
        self.declare_parameters(
            namespace ='',
            parameters=[
                ('nome_da_estrela',rclpy.Parameter.Type.STRING),
                ('nome_do_planeta',rclpy.Parameter.Type.STRING),
                ('raio_da_orbita',rclpy.Parameter.Type.INTEGER),
            ]
        )
        self.parametro_string = self.get_parameter('nome_da_estrela').get_parameter_value().string_value
        self.parametro_string = self.get_parameter('nome_do_planeta').get_parameter_value().string_value
        self.parametro_integer = self.get_parameter('raio_da_orbita').get_parameter_value().integer_value
        self.get_logger().info(f'Primeiro parametro {self.parametro_string}')
        self.get_logger().info(f'Segundo parametro {self.parametro_integer}')
        


def main(args=None):
    rclpy.init(args=args)
    parametros = Parametros()
    rclpy.spin(parametros)
    rclpy.shutdown()



    if __name__ == '__main__':
        main()