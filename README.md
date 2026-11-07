# ip-push-to-discord
Pushes your IPv4 and IPv6 addresses to a Discord channel  
Here is how it looks:  
<img width="493" height="145" alt="discord_screenshot" src="https://github.com/user-attachments/assets/aa7c2a0b-39d9-4ac4-a198-9e00a0796e97" />

## How to get a webhook in Discord
- Go to your channel where you want the webhook interaction
- End of the line, click the cogwheel (Edit channel)
- Select ```Integrations``` / ```Create Webhook```
- You can add a name and then click ```Copy Webhook URL```

That's what you will copy in the line in the Python script:  
```WEBHOOK_URL = "https://discord.com/api/webhooks/[longnumbercomeshere]"```
