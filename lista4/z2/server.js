const https = require('https');
const http = require('http');
const fs = require('fs');

function createHttpsApp(port) {
  const httpsOptions = {
    key: fs.readFileSync('../z1/privkeyA.pem'),
    cert: fs.readFileSync('../z1/certA.crt'),
    passphrase: "password"
  };

  https.createServer(httpsOptions, (req, res) => {
    res.writeHead(200);
    res.end('Hello World!');
  }).listen(port);

  console.log(`HTTPS: server running on port ${port}`);
}


function createHttpApp(port, httpsPort) {
  const express = require('express');
  const app = express();

  app.get('*', function(req, res) {
    console.log("HTTP: Move detected. Redirecting to port 443");
    res.redirect('https://' + req.headers.host + req.url);
  });

  http.createServer(app).listen(port);
  console.log(`HTTP: redirection from port ${port} to ${httpsPort}`)
}
const ports = {
  https: 443,
  http: 80
};

createHttpsApp(ports.https);
createHttpApp(ports.http, ports.https);
console.log()