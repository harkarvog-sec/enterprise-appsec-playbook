# Cryptography Review

## Purpose:
- Validate encryption usage, key management, and secure storage.

------

## Tools & Techniques:
- openssl
- Key inspection
- Hash analysis

------

## Methodology:
- Identify encryption usage
- Check algorithms
- Validate key length
- Review storage

-----

## Commands:
# Step 1:
- TLS Check:

openssl s_client -connect target.com:443

-----

### Step 2:
- Hash Test:

echo "password" | sha256sum

-----

###  Output:
- Weak algorithms
- Poor key management
- Insecure storage

------

#### Security Impact:
- Protects sensitive data
- Prevents breaches
- Ensures compliance
