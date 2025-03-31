
![image](https://github.com/user-attachments/assets/e607985f-f970-4fe7-8167-d133a2c1d270)

First we should do our Static analysis 

i used JADX to decompile the APK file 

![image](https://github.com/user-attachments/assets/9a80cc80-4ecc-4abc-8854-98c37b1f2848)

we found that there is a check on the username : it should be equal to 1DH4M

and there is a nativ function that check the PIN loaded from a native-lib called "loggie"

![image](https://github.com/user-attachments/assets/2fee4476-972e-4899-b9de-37944936d7d0)

So i used apktool then ida to analyse the native-lib

````C
_BOOL4 __cdecl f1(char *s)
{
  return strlen(s) == 4;
} //check if the PIN's length is 4


_BOOL4 __cdecl f2(char *s)
{
  size_t v1; // edi
  unsigned int v2; // ebp

  if ( !*s )
    return 1;
  v1 = 0;
  do
  {
    v2 = s[v1] - 48;
    if ( v2 >= 0xA )
      break;
    ++v1;
  }
  while ( v1 < strlen(s) );
  return v2 < 0xA;
}  // check if the 4 digits are numeric


int __cdecl f3(char *s)
{
  int result; // eax
  size_t v2; // esi
  size_t v3; // eax
  size_t v4; // ebp
  char v5; // [esp+7h] [ebp-15h]
  size_t v6; // [esp+8h] [ebp-14h]

  result = 1;
  if ( *s )
  {
    v2 = 0;
    v6 = strlen(s);
    while ( 1 )
    {
      v3 = v2++;
      if ( v2 < v6 )
        break;
LABEL_3:
      if ( v2 >= strlen(s) )
        return 1;
    }
    v5 = s[v3];
    v4 = v2;
    while ( v5 != s[v4] )
    {
      if ( ++v4 >= strlen(s) )
        goto LABEL_3;
    }
    return 0;
  }
  return result;
} check if the 4 digits are Distinct


_BOOL4 __cdecl f4(char *nptr)
{
  return (atoi(nptr) & 1) == 0;
} // check if the pin is even


_BOOL4 __cdecl f5(char *nptr)
{
  return (unsigned int)(-1431655765 * atoi(nptr) + 715827882) < 0x55555555;
} // check PIN mod 3


_BOOL4 __cdecl f6(char *nptr)
{
  return (atoi(nptr) & 3) == 0;
} //check PIN mod 4


_BOOL4 __cdecl f7(char *nptr)
{
  return (unsigned int)(-1227133513 * atoi(nptr) + 306783378) < 0x24924925;
} //check PIN mod 7



_BOOL4 __cdecl f8(char *s)
{
  size_t v1; // edi
  size_t v2; // eax
  int v3; // ecx

  if ( !*s )
    return 0;
  v1 = 0;
  v2 = strlen(s);
  v3 = 0;
  do
    v3 = s[v1++] + v3 - 48;
  while ( v1 < v2 );
  return v3 == 21;
} //check if the sum of pin digit is equal to 21



_BOOL4 __cdecl f9(const char *a1, char *s)
{
  size_t v2; // ebp
  size_t v3; // eax
  int v4; // ecx
  int v5; // ecx

  if ( *s )
  {
    v2 = 0;
    v3 = strlen(s);
    v4 = 0;
    do
      v4 += s[v2++];
    while ( v2 < v3 );
    v5 = v4 % 10;
  }
  else
  {
    v5 = 0;
  }
  return v5 == *a1 - 48;
} //Checksum validation based on username's ASCII sum modulo 10 matching the PIN's first digit.
`````
here is the solver with python 

```Python
import itertools

# ===================== PIN Format Checks =====================

# Check 1: PIN length should be 4 digits
def check_length(pin):
    return len(pin) == 4

# Check 2: PIN contains only numeric digits
def check_numeric(pin):
    return pin.isdigit()

# Check 10: PIN should have all distinct digits
def check_distinct_digits(pin):
    return len(set(pin)) == len(pin)

# ===================== Mathematical Checks =====================

# Check 3: PIN divisible by 2 (PIN should be even)
def check_even(pin):
    return int(pin) % 2 == 0

# Check 4: PIN divisible by 3
def check_modulo_3(pin):
    return int(pin) % 3 == 0

# Check 5: PIN divisible by 4
def check_modulo_4(pin):
    return int(pin) % 4 == 0

# Check 6: PIN divisible by 7
def check_modulo_7(pin):
    return int(pin) % 7 == 0

# Check: Sum of digits of the PIN should be 21
def check_sum_21(pin):
    return sum(int(digit) for digit in pin) == 21

# ===================== Character Checks =====================

# Check 7: First character of the PIN is greater than the last character
def check_first_greater_than_last(pin):
    return pin[0] > pin[-1]

# Check 8: Second and last digits should be even
def check_second_and_last_even(pin):
    return int(pin[1]) % 2 == 0 and int(pin[-1]) % 2 == 0

# ===================== Username and PIN Relationship Checks =====================

# Check 9: Sum of ASCII values of the username's first character affects the PIN
def check_username_ascii_sum(username, pin):
    ascii_sum = sum(ord(char) for char in username)
    return ascii_sum % 10 == int(pin[0])

# ===================== Main Guesser Function =====================

def guess_pin(username):
    # List to store all valid PINs
    valid_pins = []

    # Generate all 4-digit PIN combinations (0000 to 9999)
    for pin_tuple in itertools.product('0123456789', repeat=4):
        pin = ''.join(pin_tuple)
        
        # Check the conditions
        if (check_length(pin) and
            check_numeric(pin) and
            check_distinct_digits(pin) and
            check_even(pin) and
            check_modulo_3(pin) and
            check_modulo_4(pin) and
            check_modulo_7(pin) and
            check_first_greater_than_last(pin) and
            check_second_and_last_even(pin) and
            check_username_ascii_sum(username, pin) and
            check_sum_21(pin)):
            valid_pins.append(pin)

    # Print all valid PINs
    if valid_pins:
        print("Valid PINs found:")
        for pin in valid_pins:
            print(pin)
    else:
        print("No valid PIN found.")

# Example usage:
username = "1DH4M"  # Replace this with the actual username
guess_pin(username)
```
The valid Pin is : 8652

```
1DH4M:8652
```

![image](https://github.com/user-attachments/assets/2cd74d80-44cc-4cad-abfa-7e9669505794)

Now we should use `adb logcat` to read logs 

![image](https://github.com/user-attachments/assets/edf68bd5-db16-4151-af0f-0afbf7d9b7bd)

we found it 

**Spark{AnDroid_FTW!}**
