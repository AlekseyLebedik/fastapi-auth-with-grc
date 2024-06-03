from loguru import logger

from core.exceptions import DoNotValidCredential


def noneMethodUserDecorator(func):
    from core.pydantic_models.type import emailValidator, phoneValidator

    def wrapper(*args, **kwargs):
        phone = kwargs.get("phone")
        email = kwargs.get("email")
        try:
            if phone:
                phoneValidator(phone)
            if email:
                emailValidator(email)
            return func(*args, **kwargs)
        except Exception as ex:
            logger.warning(ex)
            raise DoNotValidCredential(". Please pass along an email or phone number")

    return wrapper
