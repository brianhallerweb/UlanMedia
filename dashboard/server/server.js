const express = require("express");
const app = express();
const path = require("path");


app.get("/yesterday", (req, res) =>
  res.sendFile(path.join(__dirname, "../reports/yesterday_campaigns_data.html"))
);

app.get("/7days", (req, res) =>
  res.sendFile(path.join(__dirname, "../reports/seven_campaigns_data.html"))
);

app.get("/30days", (req, res) =>
  res.sendFile(path.join(__dirname, "../reports/thirty_campaigns_data.html"))
);

app.get("/90days", (req, res) =>
  res.sendFile(path.join(__dirname, "../reports/ninety_campaigns_data.html"))
);

app.get("/180days", (req, res) =>
  res.sendFile(path.join(__dirname, "../reports/oneeighty_campaigns_data.html"))
);

app.get("*", (req, res) =>
  res.sendFile(path.join(__dirname, "../public/index.html"))
);

app.listen("3000", () => {
  console.log(`dashboard running on port 3000...`);
});

