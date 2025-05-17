from aiogram.filters import BaseFilter
from aiogram.types import Message

from data.config import ADMINS

class AdminFilter(BaseFilter):
    is_admin: bool = True

    async def __call__(self, msg: Message) -> bool:
        return (str(msg.from_user.id) in ADMINS) == self.is_admin
