entity Mux_8vers1 is
    port (
        flag : in std_logic_vector(63 downto 0);
        sel  : in std_logic_vector(2 downto 0);
        cipher : std_logic_vector(7 downto 0)
    );
end Mux_8vers1;

architecture arch of Mux_8vers1 is
begin
    process(flag, sel)
    begin
        case sel is
            when "000" => cipher <= flag(63 downto 56) ;
            when "001" => cipher <= flag(55 downto 48) ;
            when "010" => cipher <= flag(47 downto 40) ;
            when "011" => cipher <= flag(39 downto 32) ;
            when "100" => cipher <= flag(7 downto 0) ;
            when "101" => cipher <= flag(15 downto 8) ;
            when "110" => cipher <= flag(23 downto 16) ;
            when others => cipher <= flag(31 downto 24) ;
        end case;
    end process;
end arch;
