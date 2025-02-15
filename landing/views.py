from django.shortcuts import render
from .models import AccessLog
import json
import httpagentparser

def home(request):
    ip_address = request.META.get('REMOTE_ADDR', '')
    user_agent = request.META.get('HTTP_USER_AGENT', '')
    referer = request.META.get('HTTP_REFERER', '')

    headers_dict = {key: str(value) for key, value in request.META.items()}
    headers = json.dumps(headers_dict, indent=4)

    parsed_ua = httpagentparser.detect(user_agent)
    device_name = parsed_ua.get('platform', {}).get('name', '')
    device_model = parsed_ua.get('platform', {}).get('version', '')
    browser = parsed_ua.get('browser', {}).get('name', '')
    browser_version = parsed_ua.get('browser', {}).get('version', '')
    os = parsed_ua.get('os', {}).get('name', '')
    os_version = parsed_ua.get('os', {}).get('version', '')

    # Captura dados enviados pelo frontend e converte corretamente
    def convert(value, dtype, default=None):
        try:
            return dtype(value) if value is not None and value != "" else default
        except ValueError:
            return default

    latitude = convert(request.POST.get('latitude'), float)
    longitude = convert(request.POST.get('longitude'), float)
    timezone = request.POST.get('timezone')
    language = request.POST.get('language')
    screen_width = convert(request.POST.get('screen_width'), int)
    screen_height = convert(request.POST.get('screen_height'), int)
    connection_type = request.POST.get('connection_type')
    connection_speed = request.POST.get('connection_speed')
    battery_level = convert(request.POST.get('battery_level'), int)
    is_charging = request.POST.get('is_charging') == 'true'
    cpu_cores = convert(request.POST.get('cpu_cores'), int)
    ram_memory = convert(request.POST.get('ram_memory'), int)
    is_touchscreen = request.POST.get('is_touchscreen') == 'true'
    gpu_info = request.POST.get('gpu_info')

    # 🔍 Debug: Exibe os valores no terminal do Django
    print("📥 Dados recebidos no Django:", request.POST)

    # Salva os dados no banco de dados
    AccessLog.objects.create(
        ip_address=ip_address,
        user_agent=user_agent,
        referer=referer,
        headers=headers,
        device_name=device_name,
        device_model=device_model,
        browser=browser,
        browser_version=browser_version,
        os=os,
        os_version=os_version,
        latitude=latitude,
        longitude=longitude,
        timezone=timezone,
        language=language,
        screen_width=screen_width,
        screen_height=screen_height,
        connection_type=connection_type,
        connection_speed=connection_speed,
        battery_level=battery_level,
        is_charging=is_charging,
        cpu_cores=cpu_cores,
        ram_memory=ram_memory,
        is_touchscreen=is_touchscreen,
        gpu_info=gpu_info
    )

    return render(request, 'landing/home.html')
