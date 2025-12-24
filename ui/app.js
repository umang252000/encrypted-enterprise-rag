// 1️⃣ Keep auth state globally + persist it
let token = localStorage.getItem("token") || "";
let tenant = localStorage.getItem("tenant") || "";

// ---------------- LOGIN ----------------
async function login() {
  const username = document.getElementById("username").value;
  const password = document.getElementById("password").value;

  try {
    const res = await fetch("https://scaling-fortnight-jjppvpjpvg9vfgr9-8001.app.github.dev/login", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ username, password })
    });

    if (!res.ok) {
      throw new Error("Login failed");
    }

    const data = await res.json();

    if (data.access_token) {
      token = data.access_token;
      tenant = data.tenant;

      // 2️⃣ Persist so UI never loses state
      localStorage.setItem("token", token);
      localStorage.setItem("tenant", tenant);

      document.getElementById("loginStatus").innerText =
        `Logged in as ${username} (Tenant: ${tenant})`;

      document.getElementById("queryCard").classList.remove("hidden");
    } else {
      document.getElementById("loginStatus").innerText = "Login failed";
    }
  } catch (err) {
    alert(err.message);
    console.error(err);
  }
}

// ---------------- ASK ----------------
async function ask() {
  const query = document.getElementById("query").value;

  if (!query.trim()) {
    alert("Please enter a question");
    return;
  }

  try {
    const res = await fetch("https://scaling-fortnight-jjppvpjpvg9vfgr9-8005.app.github.dev/query", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + token
      },
      body: JSON.stringify({
        tenant: tenant,
        query: query,
        encrypted_results: []   // ✅ leave empty (backend-safe)
      })
    });

    if (!res.ok) {
      throw new Error("Query failed: " + res.status);
    }

    const data = await res.json();

    document.getElementById("answer").innerText = data.answer;
    document.getElementById("answerCard").classList.remove("hidden");

  } catch (err) {
    alert(err.message);
    console.error(err);
  }
}