from fastapi import Header, HTTPException, Depends
import uuid
from app.db import get_db
from fastapi.security import APIKeyHeader

def create_session(member_id):
    db = get_db()
    cursor = db.cursor()

    session_id = str(uuid.uuid4())

    cursor.execute("""
        INSERT INTO session (SessionID, MemberID, ExpiresAt)
        VALUES (%s, %s, NOW() + INTERVAL 1 DAY)
    """, (session_id, member_id))

    db.commit()
    return session_id


api_key_header = APIKeyHeader(name="Authorization")

def get_current_user(token: str = Depends(api_key_header)):
    from app.db import get_db

    db = get_db()
    cursor = db.cursor(dictionary=True)

    cursor.execute("""
        SELECT m.*
        FROM session s
        JOIN member m ON s.MemberID = m.MemberID
        WHERE s.SessionID = %s AND s.ExpiresAt > NOW()
    """, (token,))

    user = cursor.fetchone()

    if not user:
        raise HTTPException(status_code=401, detail="Invalid session")

    return user


# def get_current_user(Authorization: str = Header(None)):
#     if not Authorization:
#         raise HTTPException(status_code=401, detail="No token provided")

#     db = get_db()
#     cursor = db.cursor(dictionary=True)

#     cursor.execute("""
#         SELECT m.*
#         FROM session s
#         JOIN member m ON s.MemberID = m.MemberID
#         WHERE s.SessionID = %s AND s.ExpiresAt > NOW()
#     """, (Authorization,))

#     user = cursor.fetchone()

#     if not user:
#         raise HTTPException(status_code=401, detail="Invalid session")

#     return user


# import uuid
# from app.db import get_db

# def create_session(member_id):
#     db = get_db()
#     cursor = db.cursor()

#     session_id = str(uuid.uuid4())

#     cursor.execute("""
#         INSERT INTO session (SessionID, MemberID, ExpiresAt)
#         VALUES (%s, %s, NOW() + INTERVAL 1 DAY)
#     """, (session_id, member_id))

#     db.commit()
#     return session_id


# def get_user_from_session(token):
#     db = get_db()
#     cursor = db.cursor(dictionary=True)

#     cursor.execute("""
#         SELECT m.*
#         FROM session s
#         JOIN member m ON s.MemberID = m.MemberID
#         WHERE s.SessionID = %s AND s.ExpiresAt > NOW()
#     """, (token,))

#     return cursor.fetchone()
