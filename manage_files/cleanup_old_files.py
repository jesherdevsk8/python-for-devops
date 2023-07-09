import os
import time

def remove_old_files(directory):
    current_time = time.time()

    for nome_arquivo in os.listdir(directory):
        file_path = os.path.join(directory, nome_arquivo)
        
        if os.path.isfile(file_path):
            modification_time = os.path.getmtime(file_path)
            time_difference = current_time - modification_time
            
            if time_difference > 864000:
                # Remove the file
                os.remove(file_path)

directory = os.getcwd()
remove_old_files(directory)