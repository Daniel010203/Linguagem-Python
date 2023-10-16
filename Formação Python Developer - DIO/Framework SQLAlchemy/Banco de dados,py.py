from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Criar uma instância do mecanismo de banco de dados
engine = create_engine('sqlite:///meu_banco_de_dados.db', echo=True)

# Criar uma classe de modelo
Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    email = Column(String)

# Criar o esquema do banco de dados
Base.metadata.create_all(engine)

# Criar uma sessão para interagir com o banco de dados
Session = sessionmaker(bind=engine)
session = Session()

# Inserir um novo usuário
novo_usuario = Usuario(nome='Maria', email='maria@email.com')
session.add(novo_usuario)
session.commit()

# Consultar os usuários
usuarios = session.query(Usuario).all()
for usuario in usuarios:
    print(f'ID: {usuario.id}, Nome: {usuario.nome}, Email: {usuario.email}')

# Fechar a sessão
session.close()
