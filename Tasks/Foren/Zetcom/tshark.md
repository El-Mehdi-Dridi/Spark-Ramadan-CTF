tshark -r zetc0M.pcap -Y "udp && ip.src == 10.10.1.4" -T fields -e frame.time_epoch -e data | sort -n | awk '{print $2}' | tr -d '\n' | xxd -r -p > Flag.jpg
