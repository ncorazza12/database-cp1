from pymongo import MongoClient

# Conexão com o MongoDB local
MONGO_URI = "mongodb://localhost:27017"

client = MongoClient(MONGO_URI)

# Banco de dados "escola"
db = client["escola"]

# Coleção "alunos"
alunos_collection = db["alunos"]

# Garante que não existam dois alunos com o mesmo e-mail
alunos_collection.create_index("email", unique=True)
