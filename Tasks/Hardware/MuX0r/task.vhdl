library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity Mux_16vers1 is
    port (
        Flag_bin   : in  std_logic_vector(127 downto 0);  
        Sel    : in  std_logic_vector(3 downto 0);   
        cipher : out std_logic_vector(7 downto 0)
    );
end Mux_16vers1;

architecture arch0 of Mux_16vers1 is
    signal key : std_logic_vector(7 downto 0) := "10101010";
begin
    process(Flag_bin, Sel)
    begin
        case Sel is
            when "0000" => cipher <= Flag_bin(63 downto 56)  xor key;
            when "0001" => cipher <= Flag_bin(55 downto 48)  xor key;
            when "0010" => cipher <= Flag_bin(47 downto 40)  xor key;
            when "0011" => cipher <= Flag_bin(39 downto 32)  xor key;
            when "0100" => cipher <= Flag_bin(7 downto 0)    xor key;
            when "0101" => cipher <= Flag_bin(15 downto 8)   xor key;
            when "0110" => cipher <= Flag_bin(23 downto 16)  xor key;
            when "0111" => cipher <= Flag_bin(31 downto 24)  xor key;
            when "1000" => cipher <= Flag_bin(127 downto 120) xor key;
            when "1001" => cipher <= Flag_bin(119 downto 112) xor key;
            when "1010" => cipher <= Flag_bin(111 downto 104) xor key;
            when "1011" => cipher <= Flag_bin(103 downto 96)  xor key;
            when "1100" => cipher <= Flag_bin(71 downto 64)   xor key;
            when "1101" => cipher <= Flag_bin(79 downto 72)   xor key;
            when "1110" => cipher <= Flag_bin(87 downto 80)   xor key;
            when others => cipher <= Flag_bin(95 downto 88)   xor key;
        end case;
    end process;
end arch0;
