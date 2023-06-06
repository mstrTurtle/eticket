class TokenError(BaseException):
    pass


def get_timestamp_after_xx_min(minutes=15):
    import datetime
    return (datetime.datetime.now()+datetime.timedelta(minutes=minutes)).replace(tzinfo=datetime.timezone.utc).timestamp()

def generate_token(id: int) -> str:
    # 生成一个“类JWT token”基于id。 
    import base64
    import json
    # 参见这个RFC文档的Registered Claim Names章节。
    # https://datatracker.ietf.org/doc/html/rfc7519#section-4.1
    data = {
        "iss":"turtle", # "iss" (Issuer) Claim
        "sub" : id, # "sub" (Subject) Claim
        "exp": get_timestamp_after_xx_min(minutes=15)
    }
    return base64.b64encode(json.dumps(data).encode("ascii"))

def parse_token(token: str):
    import binascii
    try:
        import base64
        import json
        return json.loads(base64.b64decode(token))
    except binascii.Error as e:
        raise TokenError('Token is Not Valid')

def get_user_id_from_token(token: str)->int:
    return parse_token(token)['sub']