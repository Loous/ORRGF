import sys
import os
import os.path
import shutil
import pathlib

class ChangeFile:
        
    def organizateFiles(self):
        """
        it create new directories depending of file suffix that it find in the path, once created the
        directory all files that they have the suffix, for example: .txt, .exe, etc. They will be stored
        in their directories correspondent.
        
        The parameter it's the path of the directory where you want that it organizates the files.
        
        --------------------------------------------------------------------------------------------------
        
        Crea nuevos directorios dependiendo de los sufijos de los archivos que se encuentren
        en la ruta dada, una vez creado el directorio todos los archivos que tengan el sufijo
        por ejemplo: .txt, .exe etc, se almacenaran en sus directorios correspondientes.
        
        Ejemplo: si al analizar una ruta se encuentra un archivo con el sufijo o extensión; .txt,
        entonces se creara un directorio con el nombre; txt y el archivo con el sufijo; .txt se movera
        al directorio creado.
        
        
        Si existen directorios en la ruta dada con el nombre de una extensión por ejemplo para txt para los
        archivos con el sufijo .txt, entonces no se generara ningún directorio y los archivos con el sufijo
        dado no se moveran al directorio ya existente porque se mezclaría con otros archivos que existan
        en el directorio previamente creado. 
        """
        
        path = sys.argv
        
        if len(path) == 2:
            path2 = path[1]
            
            if os.path.exists(path2):
                files = os.listdir(path2)
                
                suffix = []
                
                for n in files:     
                    try:
                    
                        index = n.index(".")
                        fileType = n[index: len(n)]
                        
                        suffix.append(fileType)
                        
                    except ValueError:
                        continue
                    
                if len(suffix) > 0:
                    
                    suffix = set(suffix)
                    c = 0
                    directorycreated = []
                    filessuffix = []
                    
                    for n2 in suffix:
                        n3 = n2.replace(".", "")
                        
                        if n3 in files:
                            print(f'The directory "{n3}" already exists in the path')
                            continue
                            
                        else:
                            print(f'The directory was created: "{n3}", in the path: {path2}')
                            
                            directorycreated.append(n3)
                            filessuffix.append(n2)
                    
                            k = pathlib.Path(n3)
                            k.mkdir()
                                
                            x2 = os.path.join(os.getcwd(), k)
                            
                            if os.path.exists(x2):
                                try:
                                    shutil.move(x2, path2)
                                    
                                except shutil.Error:
                                    print(f'The directory: "{n3}" already exists in the path')
                                    continue
                                
                            else:
                                print(f'The path "{n3}" doesn\'t exist')
                                
                        
                    else:
                        for n3, d in zip(filessuffix, directorycreated):
                            for n4 in files:
                                if n4.endswith(n3):
                                    path3 = os.path.join(path2, n4)
                                    drt = os.path.join(path2, d)
                                    
                                    try:
                                        shutil.move(path3, drt)
                                        
                                    except shutil.Error:
                                        continue
                                    
                else:
                    print("it was not found any path with some suffix")
            
                            
if __name__ == "__main__":
    ChangeFile().organizateFiles()
                   
                            
    
                
    
                
                
                
                
                
                
                
                
                
                
                
            
            
            
            
        
        
        
        
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        