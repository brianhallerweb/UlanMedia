const mongoose = require("mongoose");

mongoose
  .connect(process.env.MONGODB_URI)
  .then(() => {
    console.log("connected to db");
  })
  .catch(err => console.log("error connecting to db", err));

module.exports = mongoose;
