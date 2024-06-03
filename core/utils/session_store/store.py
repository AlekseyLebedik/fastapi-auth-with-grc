from core.pydantic_models.user import User

from .models import SessionNode


class SessionStore:
    def __init__(self) -> None:
        self._sessions: dict = {}
        self._cache: dict = {}

    def set_session(self, key: str, user: User, session_mark: str):
        cache_key = user.email if user.email else user.phone_token
        self.update_cache(cache_key, key)
        self._sessions[key] = SessionNode(user=user, session_mark=session_mark)
        return self._sessions

    def get_session(self, key: str):
        return self._sessions.get(key)

    def update_cache(self, key, value):
        self.__delete_cache(key)
        self.__set_cache(key, value)

    def __delete_cache(self, key):
        session_key = self._cache.get(key)
        if session_key:
            self._sessions.pop(session_key)

    def __set_cache(self, key, value):
        self._cache[key] = value

    def __repr__(self) -> str:
        return f"SessionStore({[value for value in self._cache.values()]})"


session_store = SessionStore()
