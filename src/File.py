'''
Created on 05/01/2013

@author: Steven Rey Sequeira
'''

import shutil
import os

class File(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    
    def copy(self, src, dest, opcion):
        dst= os.path.join(dest, os.path.basename(src))
        
        # indica que el parametro: "src" es el paath de un archivo o un directorio
        # que se desea copiar 
        if opcion == 1:         
            if os.path.exists(src):
                if os.path.isfile(src):
                    print 'Copiando el archivo {} al destino {} \n'.format(src, dst)
                    
                    shutil.copy2(src, dst)
                
                elif os.path.isdir(src):
                    shutil.copytree(src, dst)
            else:
                print 'El archvio o directorio {}, no existe \n'.format(src)
                
                return
            
        # indica que el parametro: "src" es el path de un arhivo el cual contiene
        # los path de los archivos que se desean copiar  
        elif opcion == 2:
            with open(src, 'r') as path:
                self.copy(path, dest, 1)
                
        if opcion == 1 and os.path.isfile(src):
            print 'El archivo fue copiado satisfactoriamente \n'
            
        elif (opcion == 1 and os.path.isdir(src)) or opcion == 2:
            print 'Los arhivos fueron copiados satisfactoriamente \n'
            
    def move(self, src, dest, opcion):
        dst= os.path.join(dest, os.path.basename(src))
        
        if opcion == 1:
            if os.path.exists(src):
                if os.path.isdir(src):
                    print 'Moviendo el directorio {} al destino'.format(src, dst)
                    
                else:
                    print 'Moviendo el archivo {} al destino'.format(src, dst)
                    
                shutil.move(src, dst)
                