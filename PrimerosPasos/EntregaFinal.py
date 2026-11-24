# Este es un programa sobre el escape del Chapo Guzman
import random

# Inicio del juego
_mensaje_inicial = 'Eres el Chapo Guzmán y acabas de entrar a prisión'
print('\n' + _mensaje_inicial + '\n' + ('-' * len(_mensaje_inicial) + '\n'))
print('Quieres escapar de prisión, así que piensas en diferentes planes')

# Se muestran los dos caminos posibles
_option1 = int(input('Tienes dos opciones: \n'
                     '0 - Negociar con los políticos para una salida legal\n'
                     '1 - Sobornar a los guardias para que te dejen escapar\n'
                     '\n'
                     '>> Ingresa tu respuesta (0/1): '))

# Camino 0
_soborno = False
_fin_juego = False
if _option1 == 0:
    print('\n' + 'Ya pasaron 5 años y no te dan resultados los políticos. Solo haz gastado recursos y tiempo en este proceso')
    _cambio_de_planes = int(input('Tus socios te recomiendan empezar a sobornar a los guardias para que te ayuden a escapar\n'
                                  '0 - Decides sobornar a los guardias y buscar una salida\n'
                                  '1 - Continuar esperando a que los políticos te den una respuesta\n'
                                  '\n'
                                  '>> Ingresa tu respuesta (0/1): '))
    if _cambio_de_planes == 0:
        _soborno = True
    else:
        _ahorros_Chapo_Guzman = random.randint(100000, 10000000)
        print('\n' + 'Estos son los ahorros del Chapo: {} dólares'.format(_ahorros_Chapo_Guzman))
        _dinero_voluntad = int(input('Cuánto dinero estás dispuesto a dar para escapar?\n'
                                     '>> '))
        _cantidad_empleados = random.randint(10, 100)
        _sueldo_empleados = random.randint(50000, 100000)
        _dinero_requerido = _cantidad_empleados * _sueldo_empleados
        print('\n' + 'La cantidad requerida de dinero para salir es: ${}, ya que son {} empleados con un sueldo de ${} anuales'.format(_dinero_requerido, _cantidad_empleados, _sueldo_empleados))
        if _dinero_voluntad > _dinero_requerido:
            _fin_juego = True
            print('\n' + 'Puedes salir de la carcel! Sí te alcanza el dinero' + '\n' + 'El juego ha terminado')
        else:
            _fin_juego = True
            print('\n' + 'NO puedes salir de la carcel!' + '\n' + 'Tu condena ha aumentado y los políticos vieron tu falta de recursos. Haz perdido el poder!\n'
                  'Fin del juego')
# Camino 1
if _option1 == 1 or _soborno:
    print('\n' + 'Han pasado 3 meses y los sobornos están dando resultados\n'
          'Ahora los guardias te dan el desayuno con cubiertos de metal')
    _cubiertos = int(input('Quieres guardar los cubiertos?\n'
                           '0 - No\n'
                           '1 - Sí\n'
                           '\n'
                           '>> Ingresa tu respuesta (0/1): '))
    print('\n' + 'Tus abogados consiguieron sobornar al camión que trae comida a la prisión')
    print('\n' + 'Llegó el día del escape' + '\n' + 'Haz llegado al camión, pero el conductor es nuevo y no sabía del plan')
    if _cubiertos == 1:
        _fin_juego = True
        print('\n' + 'Puedes salir de la carcel! Con los cubiertos que tenías guardados pudiste matar al guardia' + '\n' + 'El juego ha terminado')
    else:
        _fin_juego = True
        print('\n' + 'NO puedes salir de la carcel!' + '\n' + 'El guardia ha llamado a sus superiores para notificarles\n'
              'Te han encerrado de por vida!')
