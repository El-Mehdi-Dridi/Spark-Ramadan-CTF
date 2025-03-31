![image](https://github.com/user-attachments/assets/5a18c7f0-0d81-469a-ba70-2b83120bf96b)

First we should start our static analysis , i used JADX to decompile the apk and analyse the source code 

![image](https://github.com/user-attachments/assets/1621d49a-9144-4838-a287-db33d49c6f59)

We found that there is a check function on the hash of the secret string,

```
840bcbee48aa77500b2d09e4ffc761b890cce99e2137c00ee8934f4d1c42a12b
```
so we should carck it

![image](https://github.com/user-attachments/assets/52ca91c5-2053-4816-adbf-5f2711df9637)

the secret string was not found 

so we should patch this app

First,

we should use apk tool to build this app 

![image](https://github.com/user-attachments/assets/b503427f-c677-4f24-a5d1-ea2872249512)

Now we should patch it 

![image](https://github.com/user-attachments/assets/9f3ed978-d207-4975-88d2-e5823a0fd17c)

![image](https://github.com/user-attachments/assets/81be7f05-1df6-4124-ad55-b3c083d421fe)

In smali code 

```
if-eqz = if
if-nez = if not
```
Now we should rebuild the apk 

![image](https://github.com/user-attachments/assets/ad8c9fb6-c898-40ec-ae00-c30c7bd02a18)

After that we should sign it 

![image](https://github.com/user-attachments/assets/59aa157f-46a9-4aae-a7a8-2869aa1b1602)

Finaly the code source was modified 

![image](https://github.com/user-attachments/assets/d36e7dcc-b665-4866-a20b-593303ae4268)

So we will put a random string 

![image](https://github.com/user-attachments/assets/5532a0eb-fe99-4ce4-9381-18fe36850f10)


Pwned !!!!!!
