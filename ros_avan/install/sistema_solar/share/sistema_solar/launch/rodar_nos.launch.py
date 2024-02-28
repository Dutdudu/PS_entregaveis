import os
from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():
    config = os.path.join(
        get_package_share_directory('sistema_solar'),
        'config',
        'param.yaml'
    )

    return LaunchDescription([


        #Node(
         #   package="sistema_solar",
          # executable="parametros",
           #name="parametros",
           #parameters =[
            #   {"nome_da_estrela":"sol"},
             #  {"nome_do_planeta":"terra"},
              # {"raio_da_orbita": 5}
           #]
        #),

        Node(
            package="sistema_solar",
            executable="frame_fixo",
            name="frame_fixo",
            parameters = [
                {"nome_da_estrela":"sol"},
                {"raio_da_orbita": 5}
            ]
        ),
        Node(
            package="sistema_solar",
           executable="frame_dinamico",
           name="frame_dinamico",
           parameters =[
               {"nome_da_estrela":"sol"},
               {"nome_do_planeta":"terra"},
               {"raio_da_orbita": 4}
           ]
        ),
        Node(
            package="sistema_solar",
           executable="satelite",
           name="satelite",
           parameters =[
               {"nome_do_planeta":"terra"},
               {"nome_do_satelite":"lua"},
               {"raio_da_orbita": 1}
           ]
        ),
        Node(
            package="sistema_solar",
           executable="mercurio",
           name="mercurio",
           parameters =[
               {"nome_da_estrela":"sol"},
               {"nome_do_planeta":"mercurio"},
               {"raio_da_orbita": 2}
           ]
        ),
    
       

    ])
    