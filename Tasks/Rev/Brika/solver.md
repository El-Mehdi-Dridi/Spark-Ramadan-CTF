![image](https://github.com/user-attachments/assets/8c059acb-cf45-45b1-8e8d-733b8ba40d51)

First we should start our static analysis , i used JADX to decompile the apk and analyse the source code 

![image](https://github.com/user-attachments/assets/bbd66f3a-6a47-4abc-994e-955ed32c7b20)

We found that there is a check function on the hash of the secret string,

```
840bcbee48aa77500b2d09e4ffc761b890cce99e2137c00ee8934f4d1c42a12b
```
so we should carck it

![image](https://github.com/user-attachments/assets/c2c28cd1-bfef-4a9b-b598-12178530a8ea)

the secret string was not found 

so we should patch this app

First,

we should use apk tool to build this app 

![image](https://github.com/user-attachments/assets/aac93491-5e22-4cfc-b431-ede3b2e90068)

Now we should patch it 

![image](https://github.com/user-attachments/assets/ded652aa-4818-4eec-b2a8-beb1fb1a3b47)

![image](https://github.com/user-attachments/assets/7cb92774-e1bd-4d98-bb28-210cb2f7d061)

In smali code 

```
if-eqz = if
if-nez = if not
```
Now we should rebuild the apk 

![image](https://github.com/user-attachments/assets/dab21f80-8bd0-46b8-b62f-b2e8902d032f)

After that we should sign it 

![image](https://github.com/user-attachments/assets/a55337d2-8902-4a8a-8f08-d244dad14688)

Finaly the code source was modified 

![image](https://github.com/user-attachments/assets/2e7960a0-d15f-421c-9185-1ce15f023e5b)

So we will put a random string 

![image](https://github.com/user-attachments/assets/c5757079-74ff-4b89-9ea9-0d5173c683db)


Pwned !!!!!!
