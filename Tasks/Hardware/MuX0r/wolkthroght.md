First we should encode this output to binary 

Output="11010001 11111001 11011010 11010111 11110010 11110101 11100111 10001011 11001111 10011010 11001111 11011000 11011000 11001011 11000001 11011000"

Now we should xor this output with the key "10101010"

```Python
Output_bin = "11010001 11111001 11011010 11010111 11110010 11110101 11100111 10001011 11001111 10011010 11001111 11011000 11011000 11001011 11000001 11011000"
key = "10101010"
binary_list = Output_bin.split()
def xor_binary(bin_value, key):
    return format(int(bin_value, 2) ^ int(key, 2), '08b')
xor_results = [xor_binary(i, key) for i in binary_list]
xor_output = " ".join(xor_results)
print(xor_output)
```
```bash
xor_output : 01111011 01010011 01110000 01111101 01011000 01011111 01001101 00100001 01100101 00110000 01100101 01110010 01110010 01100001 01101011 01110010
===========> {Sp}X_M!e0errakr
```
Sel values

```bash
1110 => cipher <= Flag_bin(79 downto 72) // flag[5]=01111011
1000 => cipher <= Flag_bin(127 downto 120) // flag[0]=01010011
1001 => cipher <= Flag_bin(119 downto 112) // flag[1]=01110000
0100 => cipher <= Flag_bin(7 downto 0) // flag[15]=01111101
1101 => cipher <= Flag_bin(79 downto 72) // flag[6]=01011000
0010 => cipher <= Flag_bin(47 downto 40) // flag[10]=01011111
0011 => cipher <= Flag_bin(39 downto 32) // flag[11]=01001101
0101 => cipher <= Flag_bin(15 downto 8) // flag[14]=00100001
0111 => cipher <= Flag_bin(31 downto 24) // flag[12]=01100101
1100 => cipher <= Flag_bin(71 downto 64) // flag[7]=00110000
0110 => cipher <= Flag_bin(23 downto 16) // flag[13]=01100101
1011 => cipher <= Flag_bin(103 downto 96) // flag[3]=01110010
0000 => cipher <= Flag_bin(63 downto 56) // flag[8]=01110010
1010 => cipher <= Flag_bin(111 downto 104) // flag[2]=01100001
1111 => cipher <= Flag_bin(95 downto 88) // flag[4]=01101011
0001 => cipher <= Flag_bin(55 downto 48) // flag[9]=01110010
```
We found it 
```bash
Flag_bin : 01010011 01110000 01100001 01110010 01101011 01111011 01011000 00110000 01110010 01110010 01011111 01001101 01100101 01100101 00100001 01111101
Flag : Spark{X0rr_Mee!}
```
