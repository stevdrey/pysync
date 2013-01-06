'''
Created on 05/01/2013

@author: Steven Rey Sequeira
'''

from File import File

import argparse

if __name__ == '__main__':
    parser= argparse.ArgumentParser()
    
    parser.add_argument('-src', '--source', 
                        help='Indica la ruta del archvio o directorio fuente')
    parser.add_argument('-dst', '--destination', 
                        help='Indica la ruta del directorio de destino')
    parser.add_argument('-opt', '--option', type=int, 
                        help='''
                        Indica la operacion que se desea realizar:
                        1. Copiar
                        2. Mover
                        ''')
    parser.add_argument('-lst', '--list-file', 
                        help='Contiene la ruta de un archivo que contiene una lista de las rutas de archivos o directorios sobre los que se desea operar')
    
    args= parser.parse_args()
    
    if args != None:
        archivo= File()
        
        if args['-lst'] == '':
            # indica que se desea copiar
            if int(args['-opt']) == 1:
                archivo.copy(args['-scr'], args['-dst'], 1)
                
            # indica que se desea mover
            elif int(args['-opt']) == 2:
                archivo.move(args['-scr'], args['-dst'], 1)
                
        else:
            # indica que se desea copiar
            if int(args['-opt']) == 1:
                archivo.copy(args['-lst'], args['-dst'], 1)
                
            # indica que se desea mover
            elif int(args['-opt']) == 2:
                archivo.move(args['-lst'], args['-dst'], 1)