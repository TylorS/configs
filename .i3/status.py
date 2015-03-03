from i3pystatus import Status

status = Status(standalone=True)

status.register("clock",
                color="#4488FF",
                format="%A %d %b %H:%M:%S %p")

status.register("battery",
    format="{status} {remaining:%E%hh:%Mm}",
    color="#4488FF",
    alert=True,
    alert_percentage=5,
    status={
        "DIS":  "Discharging",
        "CHR":  "Charging",
        "FULL": "Bat full",
    },)

status.register("wireless",
    interface="wlp1s0",
    format_up="{essid} {quality:03.0f}%",
    color_up="#4488FF",
    color_down="#FF0000",
    )

status.register("alsa",
                format="Vol {volume} {muted}",
                color="#4488FF",
                color_muted="#FF0000",
                )


status.run()
