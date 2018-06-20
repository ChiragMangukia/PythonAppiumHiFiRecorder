echo y | del C:\Users\chirag.mangukia\AppData\Local\Temp\*.* /S
rd C:\Users\chirag.mangukia\AppData\Local\Temp\ /s /q
md C:\Users\chirag.mangukia\AppData\Local\Temp
Cacls C:\Users\chirag.mangukia\AppData\Local\Temp /E /P EveryOne:F