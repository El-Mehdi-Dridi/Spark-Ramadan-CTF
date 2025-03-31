# Welcome to 1DH4M App H4CK3R

![image](https://github.com/user-attachments/assets/6c094d08-e7b0-475d-b0a3-66a8539eb89d)


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

![image](https://github.com/user-attachments/assets/e99c7393-e7e6-431a-9e11-8a679c8e291e)

Now we have the creds 

```
1DH4M:good_job
```
After login 

![image](https://github.com/user-attachments/assets/6fa07b75-56c4-43a5-b180-42891b4ae387)

The author ask us to llok at Strings.xml file 

```XML
    <string name="part1">Nm|ovf)qqj)</string>
    <string name="part2">dnBQ--vB)iB</string>
    <string name="part3">(io,sz(`</string>
    <string name="key">1dh</string>
```

I used cyberchef to decrypt it 

![image](https://github.com/user-attachments/assets/bd3d8c57-e42e-4f19-a075-efa6c031e929)

Pwned !!!!!

    
