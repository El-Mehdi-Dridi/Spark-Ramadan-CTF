## Infra Analysis Walkthrough

### Network Infrastructure Overview

After analyzing the infrastructure:

![image](https://github.com/user-attachments/assets/03791327-77a1-444b-adec-d80c4991e985)


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

![image](https://github.com/user-attachments/assets/7de58bcf-8298-4d22-857e-79653069a22d)


We discovered an important message:


This indicates that we need to locate a Python file.

### Investigating the FTP Server

Since an FTP server is available, we should check it first.

![image](https://github.com/user-attachments/assets/6d056361-4d22-476b-a522-624251e5a47c)


We attempted to connect to the FTP server from the Agent's host but were denied access.

### Discovering the Hint Button

There is a **Hint** button on the webpage, so we should explore it.

![image](https://github.com/user-attachments/assets/006c0a52-fa3c-48bd-b47e-4f2a271900b8)


The hint reveals that **only one host** can connect to the FTP server.

### Identifying the Allowed Host

![image](https://github.com/user-attachments/assets/744386f5-d45d-4401-be79-5ae898f927e1)


This section looks suspicious, so we attempt the FTP connection from the **CEO’s host**.

![image](https://github.com/user-attachments/assets/6256a53e-befe-4113-bff1-6168b2c46337)


Success! We are now connected to the FTP server.

### Accessing the FTP Server

After reading the task description, we found a hint stating that:
- **Username:** `spark`
- **Password:** `spark`

![image](https://github.com/user-attachments/assets/150fbaa0-6b00-4533-8f5b-f34b1abc1616)


### Listing Available Files

Now, we list the files on the FTP server.

![image](https://github.com/user-attachments/assets/40a771b9-6e46-45b5-8d05-a55f2c6246fb)


We found the Python file: **`flag.py`**.

### Retrieving and Running `flag.py`

We download and execute `flag.py` to get the final flag.

![image](https://github.com/user-attachments/assets/1a2bff4a-9a8a-4077-8d94-867bc29a9be9)


### Conclusion

By following the clues and utilizing the right host for FTP access, we successfully retrieved and executed the Python script, ultimately obtaining the flag.
