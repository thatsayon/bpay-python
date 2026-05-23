from pydantic import BaseModel


class BkashCredentials(BaseModel):
    username: str
    password: str
    app_key: str
    app_secret: str


class BkashTokenResponse(BaseModel):
    id_token: str
    refresh_token: str
    token_type: str
    expires_in: int
