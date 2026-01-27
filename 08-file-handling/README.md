#  File Handling

## Purpose:
- Evaluate file upload, download, and storage mechanisms for security weaknesses.

-------

## Tools & Techniques:
- curl
- File extension testing
- MIME type validation

--------

## Methodology:
- Test file upload restrictions
- Validate file storage paths
- Check execution permissions
- Test download authorization

## Commands:
# Step 1:
- Upload Test:

curl -F "file=@shell.php" https://target.com/upload

-------

### Step 2:
- MIME Bypass:

curl -F "file=@test.jpg;type=application/php" https://target.com/upload

-----

#### Step 3:
- File Access:

curl https://target.com/uploads/test.jpg

-----

#### Output:
- Upload bypasses
- Executable files
- Storage weaknesses

-------

### Security Impact:
- Prevents remote code execution
- Protects file storage
- Reduces malware risk
