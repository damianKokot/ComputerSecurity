#   Certyfikat serwera
# openssl genrsa -des3 -out  privkeyA.pem
# openssl req -new -key privkeyA.pem -out certA.csr

#   Certyfikat podpisany (w przeglądarce)
# openssl genrsa -des3 -out privkeyB.pem
# openssl req -new -x509 -key privkeyB.pem -days 15 -out CAcert.crt

cat > certA.ext <<EOF
authorityKeyIdentifier=keyid,issuer
basicConstraints=CA:FALSE
keyUsage = digitalSignature, nonRepudiation, keyEncipherment, dataEncipherment
subjectAltName = @alt_names

[alt_names]
DNS.1 = poczta.pwr.wroc.pl
DNS.2 = www.poczta.pwr.wroc.pl
DNS.3 = poczta.pwr.edu.pl
DNS.4 = www.poczta.pwr.edu.pl
DNS.5 = www.moj.serwer.pl
DNS.6 = e.pwr.edu.pl
DNS.7 = www.e.pwr.edu.pl
EOF

openssl x509 -req -days 45 -in certA.csr -CA CAcert.crt -CAkey privkeyB.pem -set_serial 01 -extfile certA.ext -out certA.crt
