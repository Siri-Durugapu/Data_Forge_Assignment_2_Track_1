const BASE_URL = "http://127.0.0.1:8000";

async function request(url, options = {}) {
    const token = localStorage.getItem("token");

    options.headers = {
        "Content-Type": "application/json",
        ...(options.headers || {})
    };

    if (token) {
        options.headers["Authorization"] = token;
    }

    try {
        const res = await fetch(url, options);

        let data = {};
        try {
            data = await res.json();
        } catch {}

        if (!res.ok) {
            return { error: data.detail || "Request failed" };
        }

        return data;

    } catch (err) {
        return { error: "Server error" };
    }
}

async function login() {
    let email = document.getElementById("email").value;
    let password = document.getElementById("password").value;

    if (!email || !password) {
        alert("Enter all fields");
        return;
    }

    let data = await request(`${BASE_URL}/login`, {
        method: "POST",
        body: JSON.stringify({ email, password })
    });

    if (data && data.session_token) {
        localStorage.setItem("token", data.session_token);
        alert("Login Successful");
        window.location.href = "dashboard.html";
    } else {
        alert("Invalid credentials");
    }
}

async function isAuth() {
    const token = localStorage.getItem("token");

    if (!token) {
        window.location.href = "login.html";
        return null;
    }

    return await request(`${BASE_URL}/isAuth`);
}

function logout() {
    localStorage.clear();
    window.location.href = "login.html";
}

async function getScholarships() {
    return await request(`${BASE_URL}/scholarships`);
}

async function applyScholarship(student_id, scholarship_id) {
    return await request(`${BASE_URL}/apply`, {
        method: "POST",
        body: JSON.stringify({ student_id, scholarship_id })
    });
}

async function verifyApplication(application_id, status, remarks) {
    return await request(`${BASE_URL}/verify`, {
        method: "PUT",
        body: JSON.stringify({ application_id, status, remarks })
    });
}

async function releasePayment(application_id, amount, bank_id) {
    return await request(`${BASE_URL}/payment`, {
        method: "POST",
        body: JSON.stringify({ application_id, amount, bank_id })
    });
}

async function createMember(data) {
    return await request(`${BASE_URL}/member`, {
        method: "POST",
        body: JSON.stringify(data)
    });
}

async function deleteScholarship(id) {
    return await request(`${BASE_URL}/scholarship/${id}`, {
        method: "DELETE"
    });
}

async function deleteMember(id) {
    return await request(`${BASE_URL}/member/${id}`, {
        method: "DELETE"
    });
}

async function getProfile() {
    return await request(`${BASE_URL}/profile`);
}