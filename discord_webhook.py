import requests
import socket

# Your Discord webhook URL; Replace [longnumbercomeshere] with your webhook number from the Discord channel
WEBHOOK_URL = "https://discord.com/api/webhooks/[longnumbercomeshere]"

def get_ip(version="ipv4"):
    """Fetch public IP address (v4 or v6)."""
    url = f"https://{version}.icanhazip.com"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()  # raise if non-200 status
        ip = response.text.strip()
        if not ip:  # empty response
            return None
        return ip
    except Exception:
        return None  # return None if any error happens

def send_to_discord(message):
    """Send message to Discord channel via webhook."""
    data = {"content": message}
    response = requests.post(WEBHOOK_URL, json=data)
    if response.status_code == 204:
        print("Message sent successfully!")
    else:
        print(f"Failed: {response.status_code} - {response.text}")

if __name__ == "__main__":
    hostname = socket.gethostname()  # get system hostname
    ipv4 = get_ip("ipv4")
    ipv6 = get_ip("ipv6")

    # Build the message based on what we found - we do the rocket thingy so the message doesn't start on the same line as the Discor Bot message
    message_lines = ["🚀", f"🖥️ **Host** (This message is coming from): `{hostname}`"]
    message_lines.append("🌐 **Public IPs:**")
    message_lines.append(f"- IPv4: `{ipv4 if ipv4 else 'Not available'}`")
    message_lines.append(f"- IPv6: `{ipv6 if ipv6 else 'Not available'}`")

    message = "\n".join(message_lines)
    send_to_discord(message)
