const BASE_URL = "http://localhost:8000";

// ➕ Save User (POST)
document.getElementById("userForm").addEventListener("submit", async function (e) {
    e.preventDefault();

    const username = document.getElementById("username").value;
    const designation = document.getElementById("designation").value;
    const tasks = document.getElementById("tasks").value;

    try {
        await fetch(`${BASE_URL}/users/`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ username, designation, tasks })
        });

        alert("User saved successfully!");
        document.getElementById("userForm").reset();

    } catch (error) {
        console.error("Error saving user:", error);
    }
});


// 👇 Show Users Button Click
document.getElementById("showUsersBtn").addEventListener("click", loadUsers);


// 📋 Load Users (GET)
async function loadUsers() {
    try {
        const response = await fetch(`${BASE_URL}/users/`);
        const users = await response.json();

        const userList = document.getElementById("userList");
        userList.innerHTML = ""; // Clear old list

        if (users.length === 0) {
            userList.innerHTML = "<li>No users found</li>";
            return;
        }

        users.forEach(user => {
            const li = document.createElement("li");
            li.textContent = `${user.username} (${user.designation}) → ${user.tasks}`;
            userList.appendChild(li);
        });

    } catch (error) {
        console.error("Error loading users:", error);
    }
}
