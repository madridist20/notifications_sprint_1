from pydantic import Field
from enum import Enum
from models.base import BasePydanticModel
from models.user import UserModel


class NotificationType(str, Enum):
    sms = 'sms'
    email = 'email'
    push = 'push'
    etc = 'etc'


class ResponseEventModel(BasePydanticModel):
    user: UserModel
    template: str

    # Email, push, SMS, etc
    type: NotificationType = NotificationType.email
    data: dict


class RequestEventModel(BasePydanticModel):
    notification_name: str
    priority: int = Field(default=0, ge=0, le=3)
    data: dict
    type: NotificationType = NotificationType.email
