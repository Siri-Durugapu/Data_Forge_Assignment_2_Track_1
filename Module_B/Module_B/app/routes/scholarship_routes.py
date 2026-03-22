from fastapi import APIRouter, Depends, HTTPException
from app.auth import get_current_user
from app.db import get_db
from app.utils.logger import log_action

router = APIRouter()

@router.get("/scholarships")
def get_scholarships():
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM scholarship")
    return cursor.fetchall()


@router.post("/apply")
def apply_scholarship(data: dict, user=Depends(get_current_user)):

    if user["Role"] != "Student":
        log_action(f"UNAUTHORIZED: {user['Role']} {user['MemberID']} tried to apply scholarship")
        raise HTTPException(status_code=403, detail="Only students can apply")

    log_action(f"{user['Role']} {user['MemberID']} started applying for scholarship {data['scholarship_id']}")

    db = get_db()
    cursor = db.cursor()

    cursor.execute("""
        INSERT INTO scholarship_application
        (StudentID, ScholarshipID, ApplicationDate, Status)
        VALUES (%s, %s, CURDATE(), 'Pending')
    """, (data["student_id"], data["scholarship_id"]))

    db.commit()

    log_action(f"{user['Role']} {user['MemberID']} applied for scholarship {data['scholarship_id']}")

    return {"message": "Application submitted"}


@router.put("/verify")
def verify_application(data: dict, user=Depends(get_current_user)):

    if user["Role"] != "Admin": 
        log_action(f"UNAUTHORIZED: {user['Role']} {user['MemberID']} tried to verify application")
        raise HTTPException(status_code=403, detail="Only admin can verify")
    
    log_action(f"{user['Role']} {user['MemberID']} started verifying application {data['application_id']}")

    db = get_db()
    cursor = db.cursor() 

    # Insert verification record
    cursor.execute("""
        INSERT INTO verification
        (ApplicationID, AdminID, VerificationDate, VerificationStatus, Remarks)
        VALUES (%s, %s, CURDATE(), %s, %s)
    """, (data["application_id"], user["MemberID"], data["status"], data["remarks"]))

    # Update application
    cursor.execute("""
        UPDATE scholarship_application
        SET Status=%s
        WHERE ApplicationID=%s
    """, (data["status"], data["application_id"]))

    db.commit()

    log_action(f"{user['Role']} {user['MemberID']} verified application {data['application_id']}")

    return {"message": "Verification done"}


@router.delete("/scholarship/{scholarship_id}")
def delete_scholarship(scholarship_id: int, user=Depends(get_current_user)):

    if user["Role"] != "Authority":
        log_action(f"UNAUTHORIZED: {user['Role']} {user['MemberID']} tried to delete scholarship")
        raise HTTPException(status_code=403, detail="Only authority can delete scholarship")

    log_action(f"{user['Role']} {user['MemberID']} started deleting scholarship {scholarship_id}")
    
    db = get_db()
    cursor = db.cursor()

    cursor.execute("DELETE FROM scholarship WHERE ScholarshipID=%s", (scholarship_id,))
    db.commit()

    log_action(f"{user['Role']} {user['MemberID']} deleted scholarship {scholarship_id}")

    return {"message": "Scholarship deleted"}


# from fastapi import APIRouter, HTTPException
# from app.db import get_db

# router = APIRouter()

# @router.get("/scholarships")
# def get_scholarships():
#     db = get_db()
#     cursor = db.cursor(dictionary=True)

#     cursor.execute("SELECT * FROM scholarship")
#     return cursor.fetchall()