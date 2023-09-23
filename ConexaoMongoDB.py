import pymongo



from pymongo import MongoClient

# Crie uma conexão com o MongoDB
client = MongoClient()

# Obtenha informações sobre a instalação do MongoDB
mongodb_info = client.server_info()

# Acesse o caminho do executável do MongoDB
mongodb_exe_path = mongodb_info['storageEngines']['devnull']['uri']

print("Caminho do MongoDB Executable:", mongodb_exe_path)
