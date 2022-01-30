# ORRGF

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
