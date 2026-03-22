from fastapi import APIRouter, Depends, HTTPException
from app.auth import get_current_user
from app.db import get_db
from app.utils.logger import log_action

router = APIRouter()

@router.post("/member")
def create_member(data: dict, user=Depends(get_current_user)):

    if user["Role"] != "Admin":
        log_action(f"UNAUTHORIZED: {user['Role']} {user['MemberID']} tried to create a member")
        raise HTTPException(status_code=403, detail="Access denied")

    log_action(f"{user['Role']} {user['MemberID']} started creating member {data['email']}")

    db = get_db()
    cursor = db.cursor()

    cursor.execute("""
        INSERT INTO member (Name, Email, PhoneNo, Age, Role)
        VALUES (%s, %s, %s, %s, %s)
    """, (data["name"], data["email"], data["phone"], data["age"], data["role"]))

    db.commit()

    log_action(f"{user['Role']} {user['MemberID']} successfully created member {data['email']}")

    return {"message": "Member created"}


@router.delete("/member/{email_id}")
def delete_member(email_id: str, user=Depends(get_current_user)):

    if user["Role"] != "Admin":
        log_action(f"{user['Role']} {user['Email']} started deleting member {email_id}")
        raise HTTPException(status_code=403, detail="Only admin can delete members")

    db = get_db()
    cursor = db.cursor()

    # prevent self delete (optional but good)
    if user["Email"] == email_id:
        raise HTTPException(status_code=400, detail="Cannot delete yourself")

    log_action(f"{user['Role']} {user['Email']} started deleting member {email_id}")
    
    cursor.execute("DELETE FROM member WHERE Email=%s", (email_id,))
    db.commit()

    log_action(f"{user['Role']} {user['Email']} deleted member {email_id}")

    return {"message": "Member deleted"}


@router.get("/profile")
def get_profile(user=Depends(get_current_user)):

    db = get_db()
    cursor = db.cursor(dictionary=True)

    # STUDENT → only own profile
    if user["Role"] == "Student":
        cursor.execute("""
            SELECT MemberID, Name, Email, PhoneNo, Role, Age
            FROM member
            WHERE MemberID=%s
        """, (user["MemberID"],))
        return cursor.fetchone()

    # ADMIN or AUTHORITY → all profiles
    elif user["Role"] in ["Admin", "Authority"]:
        cursor.execute("""
            SELECT MemberID, Name, Email, PhoneNo, Role, Age
            FROM member
        """)
        return cursor.fetchall()

    else:
        log_action(f"UNAUTHORIZED: Invalid role {user['Role']} accessing profile")
        raise HTTPException(status_code=403, detail="Invalid role")

# from fastapi import APIRouter, Depends, HTTPException
# from app.auth import get_user_from_session
# from app.db import get_db

# router = APIRouter()

# def get_current_user(token: str):
#     user = get_user_from_session(token)
#     if not user:
#         raise HTTPException(status_code=401, detail="Unauthorized")
#     return user


# @router.post("/member")
# def create_member(data: dict, token: str):
#     user = get_current_user(token)

#     if user["Role"] != "Admin":
#         raise HTTPException(status_code=403, detail="Access denied")

#     db = get_db()
#     cursor = db.cursor()

#     cursor.execute("""
#         INSERT INTO member (Name, Email, PhoneNo, Age, Role)
#         VALUES (%s, %s, %s, %s, %s)
#     """, (data["name"], data["email"], data["phone"], data["age"], data["role"]))

#     db.commit()

#     return {"message": "Member created"}