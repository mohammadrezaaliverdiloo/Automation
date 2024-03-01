from django.shortcuts import render,get_object_or_404,redirect
from .models import Devices,Log
import paramiko
import time
from datetime import datetime




def home(request):
    all_devices = Devices.objects.all()
    cisco_devices = Devices.objects.filter(vendor="cisco")
    mikrotk_devices = Devices.objects.filter(vendor="mikrotik")
    last_event = Log.objects.all().order_by('-id')[:10]
    
    context={
        'all_device':len(all_devices),
        'cisco_device':len(cisco_devices),
        'mikrotik_device':len(mikrotk_devices),
        'last_event':last_event,
    }
    
    return render(request,'home.html',context)

def devices(requst):
    all_devices = Devices.objects.all()
    
    context = {
        "all_devices":all_devices
        
    }
    
    return render (requst,'devices.html',context)


def configure(request):
    if request.method =="POST":
        select_device_id = request.POST.getlist('device')
        mikrotik_command = request.POST['mikrotik_command'].splitlines()
        cisco_command = request.POST['cisco_command'].splitlines()
        for x in select_device_id:
            try:
                dev = get_object_or_404(Devices,pk=x)
                ssh_client = paramiko.SSHClient()
                ssh_client_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh_client.connect(hostname=dev.ip_address,username=dev.username,password=dev.password)
                
                if dev.vendor.lower() == "cisco":
                    conn = ssh_client.invoke_shell()
                    conn.send("conf t\n")
                    for cmd in cisco_command:
                        conn.send(cmd + "\n")
                        time.sleep(1)
                else:
                    for cmd in mikrotik_command:
                        ssh_client.exec_command(cmd)
                log = Log(target = dev.ip_address,action = "configure",status="success",time =datetime.now(),message = e )            
                log.save()        
            except Exception as e:
                log = Log(target = dev.ip_address,action = "configure",status="Error",time =datetime.now(),message = e )            
                log.save()                    
        return redirect ("home")       
    
    else:
        devices = Devices.objects.all()
        context = {
            "devices":devices,
            "mode":"configure"
            
        }
        return render(request,"config.html",context)
    
    
def verify_config(request):
    if request.method =="POST":
        try:
            result = []
            select_device_id = request.POST.getlist('device')
            mikrotik_command = request.POST['mikrotik_command'].splitlines()
            cisco_command = request.POST['cisco_command'].splitlines()
            for x in select_device_id:
                dev = get_object_or_404(Devices,pk=x)
                ssh_client = paramiko.SSHClient()
                ssh_client_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh_client.connect(hostname=dev.ip_address,username=dev.username,password=dev.password)
                
                if dev.vendor.lower() == "mikrotik":
                    for cmd in mikrotik_command:
                        stdin,stdout,stderr = ssh_client.exec_command(cmd)
                        result.append("Result on {}".format(dev.ip_address))
                        result.append(stdout.read().decode())
                else:
                    conn = ssh_client.invoke_shell()
                    conn.send('terminal length 0\n')
                    for cmd in cisco_command:
                        result.append("Result on {}".format(dev.ip_address))
                        conn.send(cmd,"\n")
                        time.sleep(1)
                        output = conn.recv(65535)
                        result.append(output.decode())
                                        
            log = Log(target = dev.ip_address,action = "verify_config",status="Error",time =datetime.now(),message = e )            
            log.save()        
        except Exception as e:
            log = Log(target = dev.ip_address,action = "verify_config",status="Error",time =datetime.now(),message = e )            
            log.save()  
        result = '\n'.join(result)    
        return render(request,"verify_result.html",{'result':result})
    else:
        devices = Devices.objects.all()
        context = {
            "devices":devices,
            "mode":"verify_config"
            
        }
        return render(request,"config.html",context)
    
def logs(request):
    logs = Log.objects.all()
    
    context = {
        'logs':logs
    }
    
    return render (request,'log.html',context)