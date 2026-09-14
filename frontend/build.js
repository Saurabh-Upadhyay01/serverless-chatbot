const fs = require("fs");

const apiUrl = process.env.CHATBOT_API_URL;

if (!apiUrl) {
    throw new Error("CHATBOT_API_URL environment variable is missing");
}

fs.writeFileSync(
    "config.js",
    `window.CHATBOT_API_URL = ${JSON.stringify(apiUrl)};\n`
);

console.log("config.js generated successfully.");