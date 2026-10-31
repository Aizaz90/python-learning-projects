with open("security.log", "r") as file:
    logs = file.readlines()

successful_logins = 0
failed_logins = 0

failed_ips = {}

for i in logs:
    print(i.strip())

    if "login successful" in i.lower():
        successful_logins += 1

    elif "login failed" in i.lower():
        failed_logins += 1

        parts = i.split()
        ip_part = parts[-1]
        ip = ip_part.split("=")[1]

        if ip in failed_ips:
            failed_ips[ip] += 1
        else:
            failed_ips[ip] = 1

print("\n--- Security Log Summary ---")
print(f"Successful logins: {successful_logins}")
print(f"Failed logins: {failed_logins}")

print(f"Failed IPs: {failed_ips}")


print("\n---Failed Logins by IP ---")
suspicious_ips = 0
for ip, count in failed_ips.items():
    print(f"{ip}: {count} failed attempts")
    if count >= 3:
        suspicious_ips +=1
        print(f"ALERT: Suspicious IP detected : {ip}")

print(f"\nTotal suspicious IPs: {suspicious_ips}")