## Infra Analysis Walkthrough

### Network Infrastructure Overview

After analyzing the infrastructure:

![Infra Overview](https://github.com/user-attachments/assets/93f81624-9f41-46a3-b81a-984805bde414)

We identified the following components:
- **1 Router**
- **5 Switches**
- **Multiple Hosts**
- **3 Servers**:
  - HTTP Server (`Spark.com`)
  - DNS Server
  - FTP Server

### Checking `Spark.com`

Our first step is to check `Spark.com` from a random host’s browser.

![Browser Check](https://github.com/user-attachments/assets/e46cb9b9-9c6d-4437-8a9c-2afadaf90a5b)


We discovered an important message:


This indicates that we need to locate a Python file.

### Investigating the FTP Server

Since an FTP server is available, we should check it first.

![FTP Access Denied](https://github.com/user-attachments/assets/fd5ff749-8da7-414b-8c91-09b9f4bcff76)

We attempted to connect to the FTP server from the Agent's host but were denied access.

### Discovering the Hint Button

There is a **Hint** button on the webpage, so we should explore it.

![Hint Button](https://github.com/user-attachments/assets/f0e8a497-395f-4387-af7f-5043d7d27afb)

The hint reveals that **only one host** can connect to the FTP server.

### Identifying the Allowed Host

![Suspicious Section](https://github.com/user-attachments/assets/a7f24365-07fd-4e96-8041-66aab593e75a)

This section looks suspicious, so we attempt the FTP connection from the **CEO’s host**.

![FTP Connection Success](https://github.com/user-attachments/assets/0598cc71-7483-4a37-910a-c77fdb29ded6)

Success! We are now connected to the FTP server.

### Accessing the FTP Server

After reading the task description, we found a hint stating that:
- **Username:** `spark`
- **Password:** `spark`

![Login Credentials](https://github.com/user-attachments/assets/f93c818e-e8d2-4f7e-887b-9051156ec1fb)

### Listing Available Files

Now, we list the files on the FTP server.

![File List](https://github.com/user-attachments/assets/581d42fd-eb87-4b6d-89b6-1f2ca7f36ae9)

We found the Python file: **`flag.py`**.

### Retrieving and Running `flag.py`

We download and execute `flag.py` to get the final flag.

![Flag Retrieved](https://github.com/user-attachments/assets/d3a9c99f-f61e-4d77-b080-a88bcb120a8b)

### Conclusion

By following the clues and utilizing the right host for FTP access, we successfully retrieved and executed the Python script, ultimately obtaining the flag.
