const http = require("http");
const fs = require("fs");
const { execFile } = require("child_process");

http.createServer((req, res) => {
  const url = new URL(req.url, "http://localhost:3000");

  if (url.pathname === "/calc") {
    const a = url.searchParams.get("a");
    const op = url.searchParams.get("op");
    const b = url.searchParams.get("b");
    res.setHeader("Content-Type", "application/json");

    if (!a || !op || !b) {
      return res.end(JSON.stringify({ error: "Fill in both numbers" }));
    }

    const PYTHON = process.platform === "win32" ? "python" : "python3";
    execFile(PYTHON, ["calculator.py", a, op, b], (err, stdout) => {
      res.end(JSON.stringify(err
        ? { error: stdout.trim() || "Something went wrong" }
        : { result: stdout.trim() }));
    });
  } else {
    res.setHeader("Content-Type", "text/html; charset=utf-8");
    res.end(fs.readFileSync("index.html"));
  }
}).listen(process.env.PORT || 3000, () => console.log("Server running"));