const axios = require("axios")
const URL = process.env.BASE_URL + process.env.TOKEN

function headers() {
  return {
    "Content-Type": "application/json"
  }
}

function dateMessage() {
  const today = new Date();
  const date = today.getDate();
  let message = "Hola! Se acerca la fecha de pagar las siguientes cuentas:\n";
  if (date === 1 || date === 3 || date === 5 || true) {
    message += "- Universidad https://www12.uc.cl/MediosDePagos/jsp/mdp_inicio.jsp"
    message += "\n  Rut Juan: 18.586.535-5\n  Rut Cristian: 18.586.536-3\n"
  }
  return JSON.stringify({
    message: message,
    statusCode: 200
  });
}

exports.handler = (event, context, callback) => {
    const msg = dateMessage();
    const headers = JSON.stringify({headers: headers()});
    axios.post(URL, {"data": msg}, headers)
    .then((response) => {
      callback(null, msg);
    }).catch((e) => {
      callback(e);
    });
};
