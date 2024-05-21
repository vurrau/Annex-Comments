openssl genrsa -out jwt-private.pem 2048

openssl rsa -in jwt-private.pem -outform PEM -pubout -out jwt-public.pem

openssl genpkey -algorithm RSA -out private_key.pem -pkeyopt rsa_keygen_bits:2048
