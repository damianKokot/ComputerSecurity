const bodyParser = require('body-parser')
const express = require('express');
const https = require('https');
const http = require('http');
const fs = require('fs');

function createHttpsApp(port) {
  const httpsOptions = {
    key: fs.readFileSync('./ssl/privkeyA.pem'),
    cert: fs.readFileSync('./ssl/certA.crt'),
    passphrase: "password"
  };

  const app = express();
  app.use(express.static('.'));
  app.use(bodyParser.json());
  app.use(bodyParser.urlencoded({extended: true})); 

  app.post('/iwc/signin', (req, res) => {
    console.log("HTTPS: Credentials", req.body);
    return res.redirect('/');
  });

  https.createServer(httpsOptions, app).listen(port);
  console.log(`HTTPS: server running on port ${port}`);
}


function createHttpApp(port, httpsPort) {
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
console.log("\n");