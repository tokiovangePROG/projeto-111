import os
import shutil

from_dir = "./Downloads"
to_dir = "C:\\Users\\Otavio\\Music\\Arquivos_Documentos"

list_of_files = os.listdir(from_dir)
#print(list_of_files)

for x in (list_of_files):
    os.path.splitext()