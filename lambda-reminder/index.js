const axios = require("axios")
const URL = process.env.BASE_URL + process.env.TOKEN

exports.handler = (event, context, callback) => {
    axios.post(URL, {}, {})
    .then((response) => {
      callback(null, "OK");
    }).catch((e) => {
      callback(e);
    });
};
