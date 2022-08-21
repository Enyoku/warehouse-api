from passlib.context import CryptContext

password_cxd = CryptContext(schemes='bcrypt', deprecated='auto')


class Hash:

    def bcrypt(password: str):
        return password_cxd.hash(password)

    def verify(hashed_password, plain_password):
        return password_cxd.verify(plain_password, hashed_password)
