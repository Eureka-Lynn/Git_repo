import network

wlan = network.WLAN(network.STA_IF)
wlan.active(True)

nets = wlan.scan()  # 扫描周围所有Wi-Fi

for net in nets:
    ssid = net[0].decode('utf-8')  # WiFi 名称
    bssid = net[1]                 # BSSID（MAC地址）
    channel = net[2]               # 信道
    rssi = net[3]                  # 信号强度
    authmode = net[4]              # 认证模式
    hidden = net[5]                # 是否隐藏SSID（0或1）

    print(f"SSID: {ssid}, RSSI: {rssi}, Channel: {channel}")
