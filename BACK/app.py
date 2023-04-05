from pydantic import BaseModel

class User(BaseModel):
    id_user: int
    name_user: str
    surname_user: str
    username: str
    pass_user: str
    status_user: int

user_list = [
    User(id_user=100, name_user="admin", surname_user="Administrador", username="admin", pass_user="admin", status_user=1),
    User(id_user=101, name_user="admin", surname_user="Administrador", username="admin", pass_user="admin", status_user=1),
    User(id_user=102, name_user="admin", surname_user="Administrador", username="admin", pass_user="admin", status_user=1),
    User(id_user=103, name_user="admin", surname_user="Administrador", username="admin", pass_user="admin", status_user=1),
    User(id_user=104, name_user="admin", surname_user="Administrador", username="admin", pass_user="admin", status_user=1),
    User(id_user=105, name_user="admin", surname_user="Administrador", username="admin", pass_user="admin", status_user=1),
    User(id_user=106, name_user="admin", surname_user="Administrador", username="admin", pass_user="admin", status_user=1),
    User(id_user=107, name_user="admin", surname_user="Administrador", username="admin", pass_user="admin", status_user=1),
    User(id_user=108, name_user="admin", surname_user="Administrador", username="admin", pass_user="admin", status_user=1),
    User(id_user=109, name_user="admin", surname_user="Administrador", username="admin", pass_user="admin", status_user=1)
]