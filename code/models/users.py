from pydantic import BaseModel, Field


class User(BaseModel):
    name: str = Field(max_length=25)
    email: str
    password: str = Field(min_lenght=6, max_lenght=8)
    birth_date: str = Field(min_menght=6, max_lenght=8)



class ErrorEmailAreadyExist(BaseModel):
    'Já existe um usuário cadastrado com esse email informado.'
    mensagem: str = Field(
        ...,
        description='Mensagem com a causa do erro'
    )
    class Config:
        schema_extra={
            'example': {
                'mensagem': 'Já existe um usuário cadastrado com esse email.'
            }
        }


class ErrorUserNotFound(BaseModel):
    'Não foi encontrado nenhum cadastro com este email em nosso Banco de Dados.'
    mensagem: str = Field(
        ...,
        description='Mensagem com a causa do erro'
    )
    class Config:
        schema_extra={
            'example': {
                'mensagem': 'Não foi encontrado nenhum cadastro com este email em nosso Banco de Dados.'
            }
        }