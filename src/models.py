from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True)
    nome = Column(String)
    email = Column(String)
    senha = Column(String)
    data_criacao = Column(DateTime, default=datetime.utcnow)

    investimentos = relationship("Investimento", back_populates="usuario")
    transacoes = relationship("Transacao", back_populates="usuario")

class Investimento(Base):
    __tablename__ = 'investimentos'

    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuarios.id'))
    valor_inicial = Column(Float)
    data_investimento = Column(DateTime, default=datetime.utcnow)
    data_retorno = Column(DateTime)
    valor_retorno = Column(Float)

    usuario = relationship("Usuario", back_populates="investimentos")
    transacoes = relationship("Transacao", back_populates="investimento")

class Transacao(Base):
    __tablename__ = 'transacoes'

    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuarios.id'))
    investimento_id = Column(Integer, ForeignKey('investimentos.id'))
    valor = Column(Float)
    tipo = Column(String)
    data_transacao = Column(DateTime, default=datetime.utcnow)

    usuario = relationship("Usuario", back_populates="transacoes")
    investimento = relationship("Investimento", back_populates="transacoes")
