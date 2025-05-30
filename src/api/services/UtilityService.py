from datetime import timedelta

import jwt
import bcrypt
from faker import Faker
from django.utils import timezone

from src.env import jwt_config
from src.utils.svcs import Service
from src.api.models.postgres import User
from src.api.enums.CharacterCasing import CharacterCasing

DEFAULT_CHARACTER_LENGTH = 12
fake = Faker()


@Service()
class UtilityService:
    @staticmethod
    async def hash_string(input: str) -> str:
        if not input:
            return ""

        salt: bytes = bcrypt.gensalt(10)
        hashed_string: bytes = bcrypt.hashpw(input.encode(), salt)

        return hashed_string.decode()

    @staticmethod
    async def compare_hash(input: str, hash: str) -> bool:
        is_same = bcrypt.checkpw(input.encode(), hash.encode())
        return is_same

    @staticmethod
    def generate_random_string(
        length: int = DEFAULT_CHARACTER_LENGTH,
        casing: CharacterCasing = CharacterCasing.LOWER,
        numeric_only: bool = False,
    ) -> str:
        if length <= 0:
            return ""

        if numeric_only:
            return str(fake.random_number(digits=length, fix_len=True))
        else:
            string_template = "".join(
                fake.random_elements(elements=("?", "#"), length=length)
            )
            string = fake.bothify(text=string_template)

            if casing == CharacterCasing.UPPER:
                return string.upper()
            elif casing == CharacterCasing.LOWER:
                return string.lower()
            else:
                return string

    @staticmethod
    def sanitize_user_object(user: User | None = None) -> User:  # type: ignore
        if user:
            del user.password
            del user.pin
            del user.otp

            return user

    @staticmethod
    def generate_jwt(email: str, user_uuid: str) -> str:
        jwt_data = {"email": email, "user_id": user_uuid}
        jwt_claims = {
            "exp": timezone.now() + timedelta(seconds=3600),
            "iss": jwt_config["issuer"],
            "aud": email,
        }
        return jwt.encode(dict(jwt_data, **jwt_claims), jwt_config["secret"])
