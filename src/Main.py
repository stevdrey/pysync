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
    parser.add_argument('-dst', '--destination', required=True,
                        help='Indica la ruta del directorio de destino')
    parser.add_argument('-opt', '--option', type=int, required=True,
                        help='''
                        Indica la operacion que se desea realizar:
                        1. Copiar
                        2. Mover
                        ''')
    parser.add_argument('-lst', '--list-file', 
                        help='Contiene la ruta de un archivo que contiene una lista de las rutas de archivos o directorios sobre los que se desea operar')
    
    args= parser.parse_args()
    
    print args
    
    if args:
        archivo= File()
        
        if args.list_file == None and args.source != None:
            # indica que se desea copiar
            if int(args.option) == 1:
                archivo.copy(args.source, args.destination, 1)
                
            # indica que se desea mover
            elif int(args.option) == 2:
                archivo.move(args.source, args.destination, 1)
                
        elif args.list_file != None and args.source == None:
            # indica que se desea copiar
            if int(args.option) == 1:
                archivo.copy(args.list_file, args.destination, 2)
                
            # indica que se desea mover
            elif int(args.option) == 2:
                archivo.move(args.list_file, args.destination, 2)