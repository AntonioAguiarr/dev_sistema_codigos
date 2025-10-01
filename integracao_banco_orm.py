from sqlalchemy import create_engine,\ 
Column, Integer,String 
from sqlalchemy.orm import declarative_base,\
sessionmaker

# method factory (fabrica de classes)
base = declarative_base()

# criar classe "real"(vai ser a tabela pelo orm)
class Aluno (Base):
    __tablename__ = 'alunos'

    id = Column(Integer, primary_Key=true,) \
    nome = Column(String(62),nullable=False)
    email = Column(String(62), unique=true, nullable=False)




    # metodo magico (printar um objeto)
    def __repr__(self):
        return F"Aluno(id={self.id},nome='{self.nome}', idade={self.idade}, email='{self.email}')>"
    



    # criar engine (cria conexão com o BD)
    engine = create_engine("sqlite://teste_com_orm.db",echo=true, future=true)


    # criar a sessão (isso conecta o engine ao ORM)
    session = sessionmaker(bind=engine,future=true)
     






