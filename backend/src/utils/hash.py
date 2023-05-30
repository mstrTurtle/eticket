def hash(password):
    # 哈希算法来自fastapi文档：
    # https://fastapi.tiangolo.com/tutorial/sql-databases/#review-all-the-files
    fake_hashed_password = password + "notreallyhashed"
    return fake_hashed_password