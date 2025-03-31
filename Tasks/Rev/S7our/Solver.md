# Welcome to 1DH4M App H4CK3R

![image](https://github.com/user-attachments/assets/54c5e6c2-4964-479a-a3be-958170759fcf)


First You must read the code source 

```Java
String obj = this.UsernameInput.getText().toString();
        String obj2 = this.PasswordInput.getText().toString();
        if (obj.equals("1DH4M") && sha1(obj2).equals("d1b68d768881963e63332b0ef751874b49e3a9a0")) {
            startActivity(new Intent(this, (Class<?>) FlagActivity.class));
            finish();
        } else {
            Toast.makeText(this, "Invalid username or password", 0).show();
        }
    }
```
The username = "1DH4M"

The password hash (sha1) = "d1b68d768881963e63332b0ef751874b49e3a9a0"

We should crack this hash 

![image](https://github.com/user-attachments/assets/0bead4f4-ddbf-4884-b445-74bf37690578)

Now we have the creds 

```
1DH4M:good_job
```
After login 

![image](https://github.com/user-attachments/assets/36c0ed55-9a08-4778-8d39-9a69622f2e2a)

The author ask us to llok at Strings.xml file 

```XML
    <string name="part1">Nm|ovf)qqj)</string>
    <string name="part2">dnBQ--vB)iB</string>
    <string name="part3">(io,sz(`</string>
    <string name="key">1dh</string>
```

I used cyberchef to decrypt it 

![image](https://github.com/user-attachments/assets/0ebf7ce5-98a5-4444-bd49-5c7bc8f1292b)


Pwned !!!!!

    
