# openssl genrsa -des3 -out  privkeyA.pem
# openssl req -new -key privkeyA.pem -out certA.csr
# openssl genrsa -des3 -out privkeyB.pem
# openssl req -new -x509 -key privkeyB.pem -out CAcert.crt -days 15

cat > certA.ext <<EOF
authorityKeyIdentifier=keyid,issuer
basicConstraints=CA:FALSE
keyUsage = digitalSignature, nonRepudiation, keyEncipherment, dataEncipherment
subjectAltName = @alt_names

[alt_names]
DNS.1 = localhost
DNS.2 = www.moj.serwer.pl

EOF
openssl x509 -req -days 45 -in certA.csr -CA CAcert.crt -CAkey privkeyB.pem -set_serial 01 -extfile certA.ext -out certA.crt

