from django.db import models

class AccessLog(models.Model):
    ip_address = models.GenericIPAddressField()  
    user_agent = models.TextField()  
    referer = models.TextField(blank=True, null=True)  
    headers = models.TextField(blank=True, null=True)  
    device_name = models.CharField(max_length=255, blank=True, null=True)  
    device_model = models.CharField(max_length=255, blank=True, null=True)  
    browser = models.CharField(max_length=255, blank=True, null=True)  
    browser_version = models.CharField(max_length=50, blank=True, null=True)  
    os = models.CharField(max_length=255, blank=True, null=True)  
    os_version = models.CharField(max_length=50, blank=True, null=True)  
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)  
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)  
    timezone = models.CharField(max_length=255, blank=True, null=True)  
    language = models.CharField(max_length=50, blank=True, null=True)  
    screen_width = models.IntegerField(blank=True, null=True)  
    screen_height = models.IntegerField(blank=True, null=True)  
    connection_type = models.CharField(max_length=50, blank=True, null=True)  
    connection_speed = models.CharField(max_length=50, blank=True, null=True)  
    battery_level = models.IntegerField(blank=True, null=True)  
    is_charging = models.BooleanField(blank=True, null=True)  
    cpu_cores = models.IntegerField(blank=True, null=True)  
    ram_memory = models.IntegerField(blank=True, null=True)  
    is_touchscreen = models.BooleanField(blank=True, null=True)  
    gpu_info = models.TextField(blank=True, null=True)  
    is_first_visit = models.BooleanField(default=False)  
    accessed_at = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return f"Acesso em {self.accessed_at} - {self.ip_address}"
