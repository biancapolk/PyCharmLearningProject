import hmac
import models.user_model


def authenticate(username, password):
    user = models.user_model.UserModel.find_by_username(username)
    if user and hmac.compare_digest(user.password, password):
        return user


def identity(payload):
    user_id = payload['identity']
    return models.user_model.UserModel.find_by_id(user_id)