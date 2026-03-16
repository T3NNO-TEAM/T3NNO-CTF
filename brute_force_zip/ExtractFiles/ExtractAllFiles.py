import zipfile
import rarfile
import py7zr
import tarfile
import subprocess


def Extract(path_file):
    
    if path_file.endswith(".zip"):
        ex = zipfile.ZipFile(path_file)
        
    elif path_file.endswith(".rar"):
        if not rarfile.UNRAR_TOOL:
            subprocess.call("sudo apt install unrar", shell=True)
        ex = rarfile.RarFile(path_file)
        
    elif path_file.endswith(".7z"):
        ex = py7zr.SevenZipFile(path_file)
    
    elif path_file.endswith(".tar", ".gz", ".bz2", ".xz"):
        ex = tarfile.open(path_file)
    
    else:
        return False
    
    return ex