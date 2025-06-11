##Platform Algılama Modülü
İşletim sistemine özgü araçlar geliştirdiğimiz projemizde, kodumuzun doğru platforma uygun kısımlarını çalıştırmak hayati önem taşır. Bu modül, Python'ın yerleşik platform kütüphanesini kullanarak çalışan işletim sistemini güvenilir bir şekilde algılar.

Aşağıda, bu işlevselliği sağlayan basit bir Python modülü (os_detector.py olarak kaydedilebilir) ve nasıl kullanılabileceğine dair örnekler bulabilirsin:
import platform

class OSDetector:
    """
    Çalışan işletim sistemini algılamak ve platforma özgü bilgi sağlamak için sınıf.
    """

    def __init__(self):
        # platform.system() 'Windows', 'Linux', 'Darwin' (macOS), 'Java' vb. döndürür.
        # platform.machine() işlemci mimarisini döndürür (örn. 'x86_64', 'AMD64').
        self.os_name = platform.system()
        self.os_release = platform.release()
        self.os_version = platform.version()
        self.architecture = platform.machine()

    def get_os_type(self):
        """
        Algılanan işletim sistemi tipini döndürür.
        'Windows', 'Linux', 'macOS', 'Other' olabilir.
        """
        if self.os_name == "Windows":
            return "Windows"
        elif self.os_name == "Linux":
            return "Linux"
        elif self.os_name == "Darwin": # macOS için
            return "macOS"
        else:
            return "Other"

    def is_windows(self):
        """İşletim sistemi Windows ise True döner."""
        return self.get_os_type() == "Windows"

    def is_linux(self):
        """İşletim sistemi Linux ise True döner."""
        return self.get_os_type() == "Linux"

    def is_macos(self):
        """İşletim sistemi macOS ise True döner."""
        return self.get_os_type() == "macOS"

    def get_detailed_info(self):
        """
        İşletim sistemi hakkında detaylı bilgileri bir sözlük olarak döndürür.
        """
        info = {
            "OS Name": self.os_name,
            "OS Type": self.get_os_type(),
            "Release": self.os_release,
            "Version": self.os_version,
            "Architecture": self.architecture,
            "Python Version": platform.python_version()
        }
        return info

# Modülün doğrudan çalıştırıldığında test edilmesi
if __name__ == "__main__":
    detector = OSDetector()

    print(f"Algılanan İşletim Sistemi Tipi: {detector.get_os_type()}")
    print(f"Windows mı? {detector.is_windows()}")
    print(f"Linux mı? {detector.is_linux()}")
    print(f"macOS mı? {detector.is_macos()}")
    
    print("\nDetaylı İşletim Sistemi Bilgileri:")
    for key, value in detector.get_detailed_info().items():
        print(f"  {key}: {value}")

    print("\n--- Örnek Kullanım: Platforma Özgü Kod Çalıştırma ---")
    os_type = detector.get_os_type()

    if os_type == "Windows":
        print("Windows'a özgü kod çalıştırılıyor...")
        # Örnek: subprocess.run(["powershell", "Get-WmiObject -Class Win32_OperatingSystem"])
        # veya pywin32 kullanarak
        print("Windows Komut İstemi: dir")
        import subprocess
        try:
            result = subprocess.run(["cmd", "/c", "dir"], capture_output=True, text=True, check=True)
            print(result.stdout[:200] + "...") # İlk 200 karakteri göster
        except subprocess.CalledProcessError as e:
            print(f"Hata: {e.stderr}")

    elif os_type == "Linux":
        print("Linux'a özgü kod çalıştırılıyor...")
        # Örnek: subprocess.run(["lsb_release", "-a"])
        # veya psutil kullanarak
        print("Linux Terminal: ls -l")
        import subprocess
        try:
            result = subprocess.run(["ls", "-l"], capture_output=True, text=True, check=True)
            print(result.stdout[:200] + "...") # İlk 200 karakteri göster
        except subprocess.CalledProcessError as e:
            print(f"Hata: {e.stderr}")

    elif os_type == "macOS":
        print("macOS'a özgü kod çalıştırılıyor...")
        # Örnek: subprocess.run(["sw_vers"])
        # veya osascript kullanarak
        print("macOS Terminal: sw_vers")
        import subprocess
        try:
            result = subprocess.run(["sw_vers"], capture_output=True, text=True, check=True)
            print(result.stdout.strip())
        except subprocess.CalledProcessError as e:
            print(f"Hata: {e.stderr}")

    else:
        print("Desteklenmeyen veya bilinmeyen bir işletim sistemi algılandı.")

 ## Modülün Açıklaması:
OSDetector Sınıfı:
__init__: Sınıf başlatıldığında platform.system(), platform.release(), platform.version() ve platform.machine() gibi fonksiyonları kullanarak temel işletim sistemi bilgilerini yakalar.
get_os_type(): En önemli metodumuzdur. platform.system()'in döndürdüğü değeri (örneğin Windows için "Windows", Linux için "Linux", macOS için "Darwin") alarak daha anlaşılır ve tutarlı "Windows", "Linux", "macOS", "Other" gibi tipler döndürür.
is_windows(), is_linux(), is_macos(): Belirli bir işletim sisteminde olup olmadığını kontrol etmek için kolaylık sağlayan yardımcı metotlardır.
get_detailed_info(): İşletim sistemi hakkında daha fazla detayı bir sözlük olarak sunar, bu da loglama veya hata ayıklama için faydalıdır.
if __name__ == "__main__": Bloğu:
Bu kısım, modülün doğrudan çalıştırıldığında ne yapacağını gösterir.
Bir OSDetector nesnesi oluşturur.
Algılanan işletim sistemi tipini ve diğer detayları yazdırır.
En önemlisi, get_os_type() metodunun dönüş değerine göre platforma özgü kod bloklarını nasıl koşullu olarak çalıştırabileceğini gösterir. Bu, projenin geri kalanında kullanacağın ana yöntem olacaktır.

Nasıl Kullanacaksın?
1. Yukarıdaki kodu os_detector.py adıyla kaydet.
2. Ana projenin Python dosyalarında, platforma özgü bir işlem yapman gerektiğinde bu modülü içeri aktar:
from os_detector import OSDetector

detector = OSDetector()
current_os = detector.get_os_type()

if current_os == "Windows":
    # Windows'a özel fonksiyonları çağır veya Windows API'lerini kullan
    print("Windows için özel bir işlem yapılıyor...")
    # windows_specific_function()
elif current_os == "Linux":
    # Linux'a özel fonksiyonları çağır veya sistem çağrılarını kullan
    print("Linux için özel bir işlem yapılıyor...")
    # linux_specific_task()
elif current_os == "macOS":
    # macOS'a özel fonksiyonları çağır veya AppleScript/Cocoa kullan
    print("macOS için özel bir işlem yapılıyor...")
    # macos_specific_action()
else:
    print(f"Desteklenmeyen işletim sistemi: {current_os}")

##Temel Sistem Bilgileri Toplama Modülleri
İşletim sistemine özgü araçlar projenin önemli bir parçası da temel sistem bilgilerini toplamaktır. Bu modül, farklı işletim sistemlerinde (Windows, Linux, macOS) CPU, bellek, disk, ağ ve süreç bilgilerini almak için kullanılacak fonksiyonları içerir. Platformlar arası uyumluluğu sağlamak adına, öncelikle psutil kütüphanesini kullanacağız, çünkü bu kütüphane birçok OS için birleşik bir API sunar. Ancak, psutil'in kapsamadığı veya daha özel, OS'e özgü araçlarla daha iyi elde edilebilecek bilgiler için ilgili OS'in kendi modüllerini veya komutlarını kullanacağız.

Daha önceki Platform Algılama Modülü'nü kullandığımızı varsayarak kodumuzu düzenleyelim
import platform
import psutil
import subprocess
import re
import os

# os_detector.py dosyasından OSDetector sınıfını import ettiğimizi varsayalım
# from os_detector import OSDetector # Eğer ayrı bir dosyadaysa bu satırı kullanın.

# Basitlik adına, bu örnekte OSDetector sınıfını doğrudan tanımlayalım:
class OSDetector:
    def __init__(self):
        self.os_name = platform.system()

    def get_os_type(self):
        if self.os_name == "Windows":
            return "Windows"
        elif self.os_name == "Linux":
            return "Linux"
        elif self.os_name == "Darwin":
            return "macOS"
        else:
            return "Other"

    def is_windows(self):
        return self.get_os_type() == "Windows"

    def is_linux(self):
        return self.get_os_type() == "Linux"

    def is_macos(self):
        return self.get_os_type() == "macOS"


class SystemInfoCollector:
    """
    Çeşitli işletim sistemlerinden temel sistem bilgilerini toplayan sınıf.
    """
    def __init__(self):
        self.detector = OSDetector()
        self.os_type = self.detector.get_os_type()

    def get_cpu_info(self):
        """CPU çekirdek sayısı ve kullanım oranını döndürür."""
        info = {}
        info['physical_cores'] = psutil.cpu_count(logical=False)
        info['logical_cores'] = psutil.cpu_count(logical=True)
        # Per-CPU kullanım oranları (bir saniyelik bloklama)
        info['cpu_usage_percent'] = psutil.cpu_percent(interval=1, percpu=True)
        info['overall_cpu_usage_percent'] = psutil.cpu_percent(interval=1, percpu=False)
        return info

    def get_memory_info(self):
        """Toplam, kullanılan ve boş bellek bilgilerini (MB cinsinden) döndürür."""
        info = {}
        mem = psutil.virtual_memory()
        info['total_memory_mb'] = round(mem.total / (1024 ** 2), 2)
        info['available_memory_mb'] = round(mem.available / (1024 ** 2), 2)
        info['used_memory_mb'] = round(mem.used / (1024 ** 2), 2)
        info['percentage_used'] = mem.percent
        return info

    def get_disk_info(self):
        """
        Her bir disk bölümü için toplam, kullanılan ve boş disk alanı bilgilerini (GB cinsinden) döndürür.
        """
        info = []
        partitions = psutil.disk_partitions()
        for p in partitions:
            try:
                usage = psutil.disk_usage(p.mountpoint)
                info.append({
                    'device': p.device,
                    'mountpoint': p.mountpoint,
                    'fstype': p.fstype,
                    'total_gb': round(usage.total / (1024 ** 3), 2),
                    'used_gb': round(usage.used / (1024 ** 3), 2),
                    'free_gb': round(usage.free / (1024 ** 3), 2),
                    'percentage_used': usage.percent
                })
            except Exception as e:
                # Disk okuma hatası (örn. çıkarılabilir diskler)
                print(f"Disk bilgileri alınırken hata oluştu ({p.mountpoint}): {e}")
                continue
        return info

    def get_network_info(self):
        """IP adresleri ve ağ adaptörü bilgilerini döndürür."""
        info = []
        net_if_addrs = psutil.net_if_addrs()
        for interface_name, addresses in net_if_addrs.items():
            current_interface = {'interface': interface_name, 'addresses': []}
            for addr in addresses:
                if addr.family == psutil.AF_LINK: # MAC adresi
                    current_interface['mac_address'] = addr.address
                elif addr.family == socket.AF_INET: # IPv4 adresi
                    current_interface['addresses'].append({
                        'family': 'IPv4',
                        'address': addr.address,
                        'netmask': addr.netmask,
                        'broadcast': addr.broadcast
                    })
                elif addr.family == socket.AF_INET6: # IPv6 adresi
                    current_interface['addresses'].append({
                        'family': 'IPv6',
                        'address': addr.address
                    })
            info.append(current_interface)
        return info

    def get_process_info(self):
        """Çalışan süreçlerin listesini (PID, İsim, CPU/Bellek Kullanımı) döndürür."""
        info = []
        for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_info']):
            try:
                # cpu_percent ilk çağrıda 0 dönebilir, gerçek değer için ikinci çağrı gerekir.
                # Burada sadece anlık değer alıyoruz.
                info.append({
                    'pid': proc.info['pid'],
                    'name': proc.info['name'],
                    'cpu_percent': proc.info['cpu_percent'],
                    'memory_rss_mb': round(proc.info['memory_info'].rss / (1024 ** 2), 2) # Resident Set Size
                })
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                # Sürecin o an kapanmış veya erişilemez olması durumu
                continue
        # CPU kullanımına göre sıralama (isteğe bağlı)
        info.sort(key=lambda x: x['cpu_percent'], reverse=True)
        return info

    # --- OS-Specific Ek Bilgiler (psutil'in kapsamadığı veya alternatif yollar) ---

    def get_windows_specific_network_info(self):
        """Windows'a özgü ağ adaptörü detaylarını (örn. bağlantı durumu) PowerShell ile alır."""
        if not self.detector.is_windows():
            return "Sadece Windows için geçerlidir."
        try:
            # Get-NetAdapter -Physical | Select-Object Name, Status, LinkSpeed
            command = ["powershell", "Get-NetAdapter -Physical | Select-Object Name, Status, LinkSpeed | ConvertTo-Json"]
            result = subprocess.run(command, capture_output=True, text=True, check=True, encoding='utf-8')
            return result.stdout
        except subprocess.CalledProcessError as e:
            return f"PowerShell hatası: {e.stderr}"
        except FileNotFoundError:
            return "PowerShell bulunamadı. Lütfen yüklü olduğundan emin olun."

    def get_linux_distribution_info(self):
        """Linux dağıtım bilgilerini (örn. Ubuntu, Debian) alır."""
        if not self.detector.is_linux():
            return "Sadece Linux için geçerlidir."
        try:
            # lsb_release -a komutu yerine, distro kütüphanesini tercih ediyoruz.
            import distro # pip install distro
            return {
                "name": distro.name(),
                "id": distro.id(),
                "version": distro.version(),
                "like": distro.like()
            }
        except ImportError:
            return "distro kütüphanesi yüklü değil. (pip install distro)"
        except Exception as e:
            return f"Dağıtım bilgisi alınırken hata: {e}"

    def get_macos_build_version(self):
        """macOS yapım versiyonunu alır."""
        if not self.detector.is_macos():
            return "Sadece macOS için geçerlidir."
        try:
            command = ["sw_vers", "-buildVersion"]
            result = subprocess.run(command, capture_output=True, text=True, check=True)
            return result.stdout.strip()
        except subprocess.CalledProcessError as e:
            return f"Komut hatası: {e.stderr}"

# --- Kullanım Örneği ---
if __name__ == "__main__":
    import socket # get_network_info için gerekli

    collector = SystemInfoCollector()

    print("\n--- CPU Bilgileri ---")
    cpu_info = collector.get_cpu_info()
    print(f"Fiziksel Çekirdekler: {cpu_info['physical_cores']}")
    print(f"Mantıksal Çekirdekler: {cpu_info['logical_cores']}")
    print(f"Tüm CPU Kullanımı: {cpu_info['overall_cpu_usage_percent']}%")
    print(f"Her Çekirdek Kullanımı: {cpu_info['cpu_usage_percent']}")

    print("\n--- Bellek Bilgileri ---")
    mem_info = collector.get_memory_info()
    print(f"Toplam Bellek: {mem_info['total_memory_mb']} MB")
    print(f"Kullanılan Bellek: {mem_info['used_memory_mb']} MB")
    print(f"Boş Bellek: {mem_info['available_memory_mb']} MB")
    print(f"Kullanım Yüzdesi: {mem_info['percentage_used']}%")

    print("\n--- Disk Bilgileri ---")
    disk_infos = collector.get_disk_info()
    for disk in disk_infos:
        print(f"Cihaz: {disk['device']}, Bağlantı Noktası: {disk['mountpoint']}")
        print(f"  Toplam: {disk['total_gb']} GB, Kullanılan: {disk['used_gb']} GB, Boş: {disk['free_gb']} GB")
        print(f"  Kullanım Yüzdesi: {disk['percentage_used']}%")

    print("\n--- Ağ Bilgileri ---")
    net_infos = collector.get_network_info()
    for net in net_infos:
        print(f"Arayüz: {net['interface']}")
        if 'mac_address' in net:
            print(f"  MAC Adresi: {net['mac_address']}")
        for addr in net['addresses']:
            print(f"  {addr['family']} Adresi: {addr['address']}")
            if 'netmask' in addr:
                print(f"    Netmask: {addr['netmask']}")
    
    # OS'e özgü ağ bilgileri
    if collector.detector.is_windows():
        print("\n--- Windows'a Özgü Ağ Bilgileri (PowerShell) ---")
        print(collector.get_windows_specific_network_info())
    elif collector.detector.is_linux():
        print("\n--- Linux Dağıtım Bilgileri ---")
        print(collector.get_linux_distribution_info())
    elif collector.detector.is_macos():
        print("\n--- macOS Yapım Versiyonu ---")
        print(collector.get_macos_build_version())


    print("\n--- Süreç Bilgileri (İlk 10 Süreç) ---")
    process_infos = collector.get_process_info()
    for i, proc in enumerate(process_infos[:10]): # İlk 10 süreci göster
        print(f"PID: {proc['pid']}, İsim: {proc['name']}, CPU: {proc['cpu_percent']:.2f}%, Bellek (RSS): {proc['memory_rss_mb']:.2f} MB")

 
 ##Modülün Açıklaması:
1. Bağımlılıklar:
psutil: Çapraz platform sistem bilgilerini toplamak için ana kütüphanedir. Kurulum için: pip install psutil.
platform: İşletim sistemi tipini algılamak için.
subprocess: OS'e özgü komutları (örn. PowerShell, sw_vers) çalıştırmak için.
socket: Ağ bilgileri için psutil'in AF_INET gibi sabitlerini kullanır.
distro (Linux için özel): Linux dağıtım bilgilerini almak için pip install distro.
re, os: Gerekirse ek sistem işlemleri için.    

2. SystemInfoCollector Sınıfı:
__init__: OSDetector sınıfından bir örnek oluşturur ve mevcut işletim sistemi tipini belirler.
get_cpu_info(): Fiziksel ve mantıksal çekirdek sayılarını, anlık genel ve çekirdek başına CPU kullanım yüzdelerini döndürür. interval=1 parametresi 1 saniyelik bir gecikme ile CPU kullanımını daha doğru ölçmek için kullanılır.
get_memory_info(): Toplam, kullanılan, boş ve kullanılan bellek yüzdesini MB cinsinden döndürür.
get_disk_info(): Sistemdeki her bir disk bölümü için (sabit diskler, USB sürücüler vb.) bağlantı noktasını, dosya sistemi tipini, toplam, kullanılan, boş alanı ve kullanım yüzdesini GB cinsinden döndürür. Hatalı bölümler için hata yakalama da eklenmiştir.
get_network_info(): Tüm ağ arayüzlerini listeler, MAC adreslerini, IPv4 ve IPv6 adreslerini ve ilgili netmask/broadcast bilgilerini sağlar.
get_process_info(): Çalışan tüm süreçlerin PID'lerini, adlarını, CPU ve bellek kullanım yüzdelerini listeler. Çeşitli psutil istisnalarını yönetir (sürecin kapanması, erişim reddi vb.). CPU kullanımına göre sıralama yapar.

3. OS-Specific Ek Bilgiler:
get_windows_specific_network_info(): Windows'a özel olarak PowerShell komutu kullanarak ağ adaptörlerinin bağlantı durumu ve hız gibi ek detaylarını alır.
get_linux_distribution_info(): Linux'a özel olarak distro kütüphanesini kullanarak dağıtım adını, kimliğini ve sürümünü döndürür.
get_macos_build_version(): macOS'a özel olarak sw_vers -buildVersion komutunu çalıştırarak sistemin yapım versiyonunu alır.

## Nasıl Kullanacaksın?
1. Kütüphaneleri Kur: Projenin sanal ortamında pip install psutil distro komutlarını çalıştır. (Windows için pywin32 ve wmi gibi kütüphaneler bu örnekte doğrudan kullanılmadı ama eklenen OS-specific fonksiyonlar için gerekebilirler.)
2. Modülü Kaydet: Yukarıdaki kodu system_info_collector.py gibi bir isimle kaydet.
3. Import Et ve Kullan: Ana projenin ana betiğinde veya diğer modüllerinde bu sınıfı içeri aktararak sistem bilgilerini toplayabilirsin:
from system_info_collector import SystemInfoCollector

collector = SystemInfoCollector()

cpu_data = collector.get_cpu_info()
print(f"Toplam CPU Kullanımı: {cpu_data['overall_cpu_usage_percent']}%")

memory_data = collector.get_memory_info()
print(f"Kullanılan Bellek: {memory_data['used_memory_mb']} MB")

if collector.detector.is_windows():
    windows_net_details = collector.get_windows_specific_network_info()
    print(f"Windows Ağ Detayları: {windows_net_details}")


## Basit Otomasyon Fonksiyonları
Bu bölümde, projenin temel otomasyon yeteneklerini oluşturacağız. Bu yetenekler, dosya ve dizin işlemleri ile basit uygulama başlatma/durdurma gibi operasyonları kapsayacak. Python'ın yerleşik modülleri olan os, shutil, ve subprocess'ı kullanarak bu işlemleri gerçekleştireceğiz. Yine, daha önce oluşturduğumuz Platform Algılama Modülü'nü kullanarak işletim sistemine özel durumları yöneteceğiz.

import os
import shutil
import subprocess
import psutil # Süreç durdurma için gerekli
import time   # Testler için bekleme

# os_detector.py dosyasından OSDetector sınıfını import ettiğimizi varsayalım
# from os_detector import OSDetector

# Basitlik adına, bu örnekte OSDetector sınıfını doğrudan tanımlayalım:
class OSDetector:
    def __init__(self):
        self.os_name = platform.system()

    def get_os_type(self):
        if self.os_name == "Windows":
            return "Windows"
        elif self.os_name == "Linux":
            return "Linux"
        elif self.os_name == "Darwin":
            return "macOS"
        else:
            return "Other"

    def is_windows(self):
        return self.get_os_type() == "Windows"

    def is_linux(self):
        return self.get_os_type() == "Linux"

    def is_macos(self):
        return self.get_os_type() == "macOS"

class OSAutomation:
    """
    İşletim sistemi genelinde dosya, dizin ve uygulama yönetimi için otomasyon fonksiyonları sağlar.
    """
    def __init__(self):
        self.detector = OSDetector()
        self.os_type = self.detector.get_os_type()

    # --- Dosya İşlemleri ---

    def create_file(self, file_path, content=""):
        """Belirtilen yolda bir dosya oluşturur ve içine isteğe bağlı içerik yazar."""
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Dosya oluşturuldu: '{file_path}'")
            return True
        except IOError as e:
            print(f"Dosya oluşturulurken hata: '{file_path}' - {e}")
            return False

    def delete_file(self, file_path):
        """Belirtilen yoldaki dosyayı siler."""
        try:
            if os.path.exists(file_path) and os.path.isfile(file_path):
                os.remove(file_path)
                print(f"Dosya silindi: '{file_path}'")
                return True
            else:
                print(f"Dosya bulunamadı veya bir dosya değil: '{file_path}'")
                return False
        except OSError as e:
            print(f"Dosya silinirken hata: '{file_path}' - {e}")
            return False

    def copy_file(self, source_path, destination_path):
        """Bir dosyayı bir konumdan diğerine kopyalar."""
        try:
            if os.path.exists(source_path) and os.path.isfile(source_path):
                shutil.copy2(source_path, destination_path) # copy2 metadata da kopyalar
                print(f"Dosya kopyalandı: '{source_path}' -> '{destination_path}'")
                return True
            else:
                print(f"Kaynak dosya bulunamadı: '{source_path}'")
                return False
        except IOError as e:
            print(f"Dosya kopyalanırken hata: '{source_path}' -> '{destination_path}' - {e}")
            return False

    def move_file(self, source_path, destination_path):
        """Bir dosyayı bir konumdan diğerine taşır (yeniden adlandırabilir)."""
        try:
            if os.path.exists(source_path) and os.path.isfile(source_path):
                shutil.move(source_path, destination_path)
                print(f"Dosya taşındı: '{source_path}' -> '{destination_path}'")
                return True
            else:
                print(f"Kaynak dosya bulunamadı: '{source_path}'")
                return False
        except IOError as e:
            print(f"Dosya taşınırken hata: '{source_path}' -> '{destination_path}' - {e}")
            return False

    # --- Dizin İşlemleri ---

    def create_directory(self, dir_path):
        """Belirtilen yolda bir dizin oluşturur. Eğer varsa hata vermez."""
        try:
            os.makedirs(dir_path, exist_ok=True)
            print(f"Dizin oluşturuldu: '{dir_path}'")
            return True
        except OSError as e:
            print(f"Dizin oluşturulurken hata: '{dir_path}' - {e}")
            return False

    def delete_directory(self, dir_path, recursive=False):
        """Belirtilen yoldaki dizini siler. 'recursive' True ise alt dizinleri ve dosyaları da siler."""
        try:
            if os.path.exists(dir_path) and os.path.isdir(dir_path):
                if recursive:
                    shutil.rmtree(dir_path)
                    print(f"Dizin ve içeriği silindi (recursive): '{dir_path}'")
                else:
                    os.rmdir(dir_path) # Sadece boş dizinleri siler
                    print(f"Dizin silindi (boş): '{dir_path}'")
                return True
            else:
                print(f"Dizin bulunamadı veya bir dizin değil: '{dir_path}'")
                return False
        except OSError as e:
            print(f"Dizin silinirken hata: '{dir_path}' - {e}")
            return False

    # --- Uygulama Başlatma/Durdurma ---

    def start_application(self, command, args=None, wait=False):
        """
        Belirtilen komutu (uygulama yolu/adı) çalıştırır.
        Args: Ek argümanlar listesi.
        Wait: True ise uygulamanın bitmesini bekler, False ise arka planda çalıştırır.
        """
        full_command = [command] + (args if args else [])
        try:
            if self.os_type == "Windows" and " " in command and not command.startswith('"'):
                # Windows'ta boşluk içeren yollar için tırnak işareti ekle
                full_command[0] = f'"{command}"'
            
            # shell=True tehlikeli olabilir, ancak bazı durumlarda Windows'ta exec/PATH için gereklidir.
            # Güvenli kullanım için shell=False tercih edilir ve komutlar tam yollarıyla verilmelidir.
            # Burada genel bir kullanım örneği sunuluyor.
            
            if wait:
                print(f"Uygulama başlatılıyor ve bekleniyor: {' '.join(full_command)}")
                process = subprocess.run(full_command, check=True, shell=True if self.os_type == "Windows" else False)
                return process.returncode == 0
            else:
                print(f"Uygulama arka planda başlatılıyor: {' '.join(full_command)}")
                process = subprocess.Popen(full_command, shell=True if self.os_type == "Windows" else False)
                return process.pid # Arka planda çalışan sürecin PID'sini döndür
        except FileNotFoundError:
            print(f"Hata: Uygulama veya komut bulunamadı: '{command}'")
            return None
        except subprocess.CalledProcessError as e:
            print(f"Uygulama çalıştırılırken hata oluştu (dönüş kodu: {e.returncode}): {e.stderr}")
            return None
        except Exception as e:
            print(f"Uygulama başlatılırken genel hata: {e}")
            return None

    def stop_process_by_pid(self, pid):
        """Belirtilen PID'ye sahip bir süreci sonlandırır (kill)."""
        try:
            process = psutil.Process(pid)
            process_name = process.name()
            process.terminate() # Nazikçe sonlandırma denemesi
            print(f"Süreç sonlandırma isteği gönderildi: PID {pid} ({process_name})")
            time.sleep(1) # Sonlandırma için biraz bekle
            if process.is_running():
                process.kill() # Zorla sonlandırma
                print(f"Süreç zorla sonlandırıldı: PID {pid} ({process_name})")
            return True
        except psutil.NoSuchProcess:
            print(f"Hata: PID {pid} ile bir süreç bulunamadı.")
            return False
        except psutil.AccessDenied:
            print(f"Hata: PID {pid} sürecini sonlandırmak için yeterli yetki yok.")
            return False
        except Exception as e:
            print(f"Süreç sonlandırılırken genel hata: {e}")
            return False

    def find_and_stop_process_by_name(self, process_name):
        """Belirtilen isme sahip tüm süreçleri bulur ve sonlandırır."""
        found_processes = []
        for proc in psutil.process_iter(['pid', 'name']):
            if proc.info['name'] == process_name:
                found_processes.append(proc.info['pid'])

        if not found_processes:
            print(f"'{process_name}' isimli süreç bulunamadı.")
            return False
        
        print(f"'{process_name}' isimli {len(found_processes)} adet süreç bulundu. Sonlandırılıyor...")
        success = True
        for pid in found_processes:
            if not self.stop_process_by_pid(pid):
                success = False
        return success


# --- Kullanım Örnekleri ---
if __name__ == "__main__":
    automation = OSAutomation()
    test_dir = "test_automation_dir"
    test_file_name = "test_file.txt"
    test_file_path = os.path.join(test_dir, test_file_name)
    copied_file_path = os.path.join(test_dir, "copied_test_file.txt")
    moved_file_path = os.path.join(test_dir, "moved_test_file.txt")

    print(f"\n--- OS Tipi: {automation.os_type} ---")

    # Dizin Oluşturma
    automation.create_directory(test_dir)

    # Dosya Oluşturma
    automation.create_file(test_file_path, "Bu bir test dosyasıdır.")
    time.sleep(0.5)

    # Dosya Kopyalama
    automation.copy_file(test_file_path, copied_file_path)
    time.sleep(0.5)

    # Dosya Taşıma (yeniden adlandırma)
    automation.move_file(copied_file_path, moved_file_path)
    time.sleep(0.5)

    # Dosya Silme
    automation.delete_file(test_file_path)
    automation.delete_file(moved_file_path)
    time.sleep(0.5)

    # Dizin Silme (Boş Dizin)
    automation.delete_directory(test_dir, recursive=False)
    time.sleep(0.5)

    # Dizin Oluşturma ve İçine Dosya Koyma (Recursive Silme testi için)
    automation.create_directory(os.path.join(test_dir, "alt_dizin"))
    automation.create_file(os.path.join(test_dir, "alt_dizin", "ic_dosya.txt"), "Alt dizin dosyası.")
    # Dizin Silme (Recursive)
    automation.delete_directory(test_dir, recursive=True)

    print("\n--- Uygulama Başlatma/Durdurma Testleri ---")

    # Platforma göre basit bir uygulama başlatma
    process_pid = None
    if automation.is_windows():
        # Windows için Notepad'i arka planda başlat
        print("Windows: Not defteri arka planda başlatılıyor...")
        process_pid = automation.start_application("notepad.exe", wait=False)
        if process_pid:
            print(f"Not defteri PID: {process_pid}")
            time.sleep(2) # Uygulamanın başlamasına izin ver
            automation.stop_process_by_pid(process_pid)
            print("Not defteri kapatıldı.")
        else:
            print("Not defteri başlatılamadı.")

        print("\nWindows: Calc.exe başlatılıyor ve bitmesi bekleniyor...")
        # Calc.exe'yi başlat ve kapanana kadar bekle (Manuel kapatmanız gerekebilir)
        # automation.start_application("calc.exe", wait=True)
        # print("Calc.exe kapatıldı.")

    elif automation.is_linux() or automation.is_macos():
        # Linux/macOS için 'sleep' komutunu arka planda başlat
        print(f"{automation.os_type}: 'sleep 5' arka planda başlatılıyor...")
        process_pid = automation.start_application("sleep", args=["5"], wait=False)
        if process_pid:
            print(f"'sleep 5' PID: {process_pid}")
            time.sleep(2) # Sürecin başlamasına izin ver
            automation.stop_process_by_pid(process_pid)
            print("'sleep 5' sonlandırıldı.")
        else:
            print("'sleep 5' başlatılamadı.")
            
        print(f"\n{automation.os_type}: 'ls' komutu çalıştırılıyor ve bitmesi bekleniyor...")
        # ls komutunu çalıştır ve bitmesini bekle
        success = automation.start_application("ls", args=["-l"], wait=True)
        if success:
            print("'ls -l' komutu başarıyla tamamlandı.")
        else:
            print("'ls -l' komutunda hata oluştu.")

Basit Otomasyon Fonksiyonları
Bu bölümde, projenin temel otomasyon yeteneklerini oluşturacağız. Bu yetenekler, dosya ve dizin işlemleri ile basit uygulama başlatma/durdurma gibi operasyonları kapsayacak. Python'ın yerleşik modülleri olan os, shutil, ve subprocess'ı kullanarak bu işlemleri gerçekleştireceğiz. Yine, daha önce oluşturduğumuz Platform Algılama Modülü'nü kullanarak işletim sistemine özel durumları yöneteceğiz.

Python

import os
import shutil
import subprocess
import psutil # Süreç durdurma için gerekli
import time   # Testler için bekleme

# os_detector.py dosyasından OSDetector sınıfını import ettiğimizi varsayalım
# from os_detector import OSDetector

# Basitlik adına, bu örnekte OSDetector sınıfını doğrudan tanımlayalım:
class OSDetector:
    def __init__(self):
        self.os_name = platform.system()

    def get_os_type(self):
        if self.os_name == "Windows":
            return "Windows"
        elif self.os_name == "Linux":
            return "Linux"
        elif self.os_name == "Darwin":
            return "macOS"
        else:
            return "Other"

    def is_windows(self):
        return self.get_os_type() == "Windows"

    def is_linux(self):
        return self.get_os_type() == "Linux"

    def is_macos(self):
        return self.get_os_type() == "macOS"

class OSAutomation:
    """
    İşletim sistemi genelinde dosya, dizin ve uygulama yönetimi için otomasyon fonksiyonları sağlar.
    """
    def __init__(self):
        self.detector = OSDetector()
        self.os_type = self.detector.get_os_type()

    # --- Dosya İşlemleri ---

    def create_file(self, file_path, content=""):
        """Belirtilen yolda bir dosya oluşturur ve içine isteğe bağlı içerik yazar."""
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Dosya oluşturuldu: '{file_path}'")
            return True
        except IOError as e:
            print(f"Dosya oluşturulurken hata: '{file_path}' - {e}")
            return False

    def delete_file(self, file_path):
        """Belirtilen yoldaki dosyayı siler."""
        try:
            if os.path.exists(file_path) and os.path.isfile(file_path):
                os.remove(file_path)
                print(f"Dosya silindi: '{file_path}'")
                return True
            else:
                print(f"Dosya bulunamadı veya bir dosya değil: '{file_path}'")
                return False
        except OSError as e:
            print(f"Dosya silinirken hata: '{file_path}' - {e}")
            return False

    def copy_file(self, source_path, destination_path):
        """Bir dosyayı bir konumdan diğerine kopyalar."""
        try:
            if os.path.exists(source_path) and os.path.isfile(source_path):
                shutil.copy2(source_path, destination_path) # copy2 metadata da kopyalar
                print(f"Dosya kopyalandı: '{source_path}' -> '{destination_path}'")
                return True
            else:
                print(f"Kaynak dosya bulunamadı: '{source_path}'")
                return False
        except IOError as e:
            print(f"Dosya kopyalanırken hata: '{source_path}' -> '{destination_path}' - {e}")
            return False

    def move_file(self, source_path, destination_path):
        """Bir dosyayı bir konumdan diğerine taşır (yeniden adlandırabilir)."""
        try:
            if os.path.exists(source_path) and os.path.isfile(source_path):
                shutil.move(source_path, destination_path)
                print(f"Dosya taşındı: '{source_path}' -> '{destination_path}'")
                return True
            else:
                print(f"Kaynak dosya bulunamadı: '{source_path}'")
                return False
        except IOError as e:
            print(f"Dosya taşınırken hata: '{source_path}' -> '{destination_path}' - {e}")
            return False

    # --- Dizin İşlemleri ---

    def create_directory(self, dir_path):
        """Belirtilen yolda bir dizin oluşturur. Eğer varsa hata vermez."""
        try:
            os.makedirs(dir_path, exist_ok=True)
            print(f"Dizin oluşturuldu: '{dir_path}'")
            return True
        except OSError as e:
            print(f"Dizin oluşturulurken hata: '{dir_path}' - {e}")
            return False

    def delete_directory(self, dir_path, recursive=False):
        """Belirtilen yoldaki dizini siler. 'recursive' True ise alt dizinleri ve dosyaları da siler."""
        try:
            if os.path.exists(dir_path) and os.path.isdir(dir_path):
                if recursive:
                    shutil.rmtree(dir_path)
                    print(f"Dizin ve içeriği silindi (recursive): '{dir_path}'")
                else:
                    os.rmdir(dir_path) # Sadece boş dizinleri siler
                    print(f"Dizin silindi (boş): '{dir_path}'")
                return True
            else:
                print(f"Dizin bulunamadı veya bir dizin değil: '{dir_path}'")
                return False
        except OSError as e:
            print(f"Dizin silinirken hata: '{dir_path}' - {e}")
            return False

    # --- Uygulama Başlatma/Durdurma ---

    def start_application(self, command, args=None, wait=False):
        """
        Belirtilen komutu (uygulama yolu/adı) çalıştırır.
        Args: Ek argümanlar listesi.
        Wait: True ise uygulamanın bitmesini bekler, False ise arka planda çalıştırır.
        """
        full_command = [command] + (args if args else [])
        try:
            if self.os_type == "Windows" and " " in command and not command.startswith('"'):
                # Windows'ta boşluk içeren yollar için tırnak işareti ekle
                full_command[0] = f'"{command}"'
            
            # shell=True tehlikeli olabilir, ancak bazı durumlarda Windows'ta exec/PATH için gereklidir.
            # Güvenli kullanım için shell=False tercih edilir ve komutlar tam yollarıyla verilmelidir.
            # Burada genel bir kullanım örneği sunuluyor.
            
            if wait:
                print(f"Uygulama başlatılıyor ve bekleniyor: {' '.join(full_command)}")
                process = subprocess.run(full_command, check=True, shell=True if self.os_type == "Windows" else False)
                return process.returncode == 0
            else:
                print(f"Uygulama arka planda başlatılıyor: {' '.join(full_command)}")
                process = subprocess.Popen(full_command, shell=True if self.os_type == "Windows" else False)
                return process.pid # Arka planda çalışan sürecin PID'sini döndür
        except FileNotFoundError:
            print(f"Hata: Uygulama veya komut bulunamadı: '{command}'")
            return None
        except subprocess.CalledProcessError as e:
            print(f"Uygulama çalıştırılırken hata oluştu (dönüş kodu: {e.returncode}): {e.stderr}")
            return None
        except Exception as e:
            print(f"Uygulama başlatılırken genel hata: {e}")
            return None

    def stop_process_by_pid(self, pid):
        """Belirtilen PID'ye sahip bir süreci sonlandırır (kill)."""
        try:
            process = psutil.Process(pid)
            process_name = process.name()
            process.terminate() # Nazikçe sonlandırma denemesi
            print(f"Süreç sonlandırma isteği gönderildi: PID {pid} ({process_name})")
            time.sleep(1) # Sonlandırma için biraz bekle
            if process.is_running():
                process.kill() # Zorla sonlandırma
                print(f"Süreç zorla sonlandırıldı: PID {pid} ({process_name})")
            return True
        except psutil.NoSuchProcess:
            print(f"Hata: PID {pid} ile bir süreç bulunamadı.")
            return False
        except psutil.AccessDenied:
            print(f"Hata: PID {pid} sürecini sonlandırmak için yeterli yetki yok.")
            return False
        except Exception as e:
            print(f"Süreç sonlandırılırken genel hata: {e}")
            return False

    def find_and_stop_process_by_name(self, process_name):
        """Belirtilen isme sahip tüm süreçleri bulur ve sonlandırır."""
        found_processes = []
        for proc in psutil.process_iter(['pid', 'name']):
            if proc.info['name'] == process_name:
                found_processes.append(proc.info['pid'])

        if not found_processes:
            print(f"'{process_name}' isimli süreç bulunamadı.")
            return False
        
        print(f"'{process_name}' isimli {len(found_processes)} adet süreç bulundu. Sonlandırılıyor...")
        success = True
        for pid in found_processes:
            if not self.stop_process_by_pid(pid):
                success = False
        return success


# --- Kullanım Örnekleri ---
if __name__ == "__main__":
    automation = OSAutomation()
    test_dir = "test_automation_dir"
    test_file_name = "test_file.txt"
    test_file_path = os.path.join(test_dir, test_file_name)
    copied_file_path = os.path.join(test_dir, "copied_test_file.txt")
    moved_file_path = os.path.join(test_dir, "moved_test_file.txt")

    print(f"\n--- OS Tipi: {automation.os_type} ---")

    # Dizin Oluşturma
    automation.create_directory(test_dir)

    # Dosya Oluşturma
    automation.create_file(test_file_path, "Bu bir test dosyasıdır.")
    time.sleep(0.5)

    # Dosya Kopyalama
    automation.copy_file(test_file_path, copied_file_path)
    time.sleep(0.5)

    # Dosya Taşıma (yeniden adlandırma)
    automation.move_file(copied_file_path, moved_file_path)
    time.sleep(0.5)

    # Dosya Silme
    automation.delete_file(test_file_path)
    automation.delete_file(moved_file_path)
    time.sleep(0.5)

    # Dizin Silme (Boş Dizin)
    automation.delete_directory(test_dir, recursive=False)
    time.sleep(0.5)

    # Dizin Oluşturma ve İçine Dosya Koyma (Recursive Silme testi için)
    automation.create_directory(os.path.join(test_dir, "alt_dizin"))
    automation.create_file(os.path.join(test_dir, "alt_dizin", "ic_dosya.txt"), "Alt dizin dosyası.")
    # Dizin Silme (Recursive)
    automation.delete_directory(test_dir, recursive=True)

    print("\n--- Uygulama Başlatma/Durdurma Testleri ---")

    # Platforma göre basit bir uygulama başlatma
    process_pid = None
    if automation.is_windows():
        # Windows için Notepad'i arka planda başlat
        print("Windows: Not defteri arka planda başlatılıyor...")
        process_pid = automation.start_application("notepad.exe", wait=False)
        if process_pid:
            print(f"Not defteri PID: {process_pid}")
            time.sleep(2) # Uygulamanın başlamasına izin ver
            automation.stop_process_by_pid(process_pid)
            print("Not defteri kapatıldı.")
        else:
            print("Not defteri başlatılamadı.")

        print("\nWindows: Calc.exe başlatılıyor ve bitmesi bekleniyor...")
        # Calc.exe'yi başlat ve kapanana kadar bekle (Manuel kapatmanız gerekebilir)
        # automation.start_application("calc.exe", wait=True)
        # print("Calc.exe kapatıldı.")

    elif automation.is_linux() or automation.is_macos():
        # Linux/macOS için 'sleep' komutunu arka planda başlat
        print(f"{automation.os_type}: 'sleep 5' arka planda başlatılıyor...")
        process_pid = automation.start_application("sleep", args=["5"], wait=False)
        if process_pid:
            print(f"'sleep 5' PID: {process_pid}")
            time.sleep(2) # Sürecin başlamasına izin ver
            automation.stop_process_by_pid(process_pid)
            print("'sleep 5' sonlandırıldı.")
        else:
            print("'sleep 5' başlatılamadı.")
            
        print(f"\n{automation.os_type}: 'ls' komutu çalıştırılıyor ve bitmesi bekleniyor...")
        # ls komutunu çalıştır ve bitmesini bekle
        success = automation.start_application("ls", args=["-l"], wait=True)
        if success:
            print("'ls -l' komutu başarıyla tamamlandı.")
        else:
            print("'ls -l' komutunda hata oluştu.")

## Modülün Açıklaması:
1. Bağımlılıklar:
os: Dosya ve dizin oluşturma, silme, kontrol etme gibi temel işletim sistemi etkileşimleri için.
shutil: Yüksek seviyeli dosya işlemleri (kopyalama, taşıma, dizin ağaçlarını silme) için.
subprocess: Harici uygulamaları veya komutları başlatmak için.
psutil: Çalışan süreçleri bulmak ve PID ile sonlandırmak için. (Kurulum: pip install psutil)
time: Testler arasında gecikme eklemek için.

2. OSAutomation Sınıfı:
__init__: OSDetector sınıfından bir örnek oluşturur ve işletim sistemi tipini kaydeder.

Dosya İşlemleri:
create_file(file_path, content): Belirtilen yola yeni bir dosya oluşturur ve isteğe bağlı olarak içine metin yazar.
delete_file(file_path): Belirtilen yoldaki bir dosyayı siler. Dosyanın varlığını ve gerçekten bir dosya olup olmadığını kontrol eder.
copy_file(source_path, destination_path): Bir dosyayı kaynaktan hedefe kopyalar. shutil.copy2 kullanır, bu da dosya metadata'sını da korur.
move_file(source_path, destination_path): Bir dosyayı kaynaktan hedefe taşır. Bu aynı zamanda dosyayı yeniden adlandırmak için de kullanılabilir.

Dizin İşlemleri:
create_directory(dir_path): Belirtilen yolda bir dizin oluşturur. exist_ok=True sayesinde dizin zaten varsa hata vermez.
delete_directory(dir_path, recursive=False): Belirtilen dizini siler. recursive=True ise dizin içindeki tüm dosya ve alt dizinleri de siler (shutil.rmtree kullanır). recursive=False ise yalnızca boş dizinleri siler (os.rmdir kullanır).
            
Uygulama Başlatma/Durdurma:
start_application(command, args=None, wait=False):
Belirtilen komutu (uygulama adı veya tam yolu) ve argümanları kullanarak bir uygulamayı başlatır.
wait=True ise uygulama tamamlanana kadar bekler (subprocess.run).
wait=False ise uygulamayı arka planda başlatır (subprocess.Popen) ve sürecin PID'sini döndürür.
Platforma özel olarak Windows'ta boşluk içeren komut yollarını düzgün yönetir ve shell=True kullanımını Windows için düşünebilir (genellikle güvenlik riski içerir, tam yol kullanımı önerilir).
FileNotFoundError ve subprocess.CalledProcessError gibi yaygın hataları yakalar.
stop_process_by_pid(pid): Belirtilen PID'ye sahip bir süreci nazikçe sonlandırmaya çalışır, başarısız olursa zorla kapatır.
find_and_stop_process_by_name(process_name): Belirtilen isme sahip tüm süreçleri bulur ve tek tek stop_process_by_pid ile sonlandırır.

## Nasıl Kullanacaksın?
1. Kütüphaneleri Kur: Projenin sanal ortamında pip install psutil komutunu çalıştır.
2. Modülü Kaydet: Yukarıdaki kodu os_automation.py gibi bir isimle kaydet.
3. Import Et ve Kullan: Ana projenin ana betiğinde veya diğer modüllerinde bu sınıfı içeri aktararak otomasyon görevlerini gerçekleştirebilirsin:

from os_automation import OSAutomation

automation = OSAutomation()

# Örnek: Bir log dosyası oluştur
log_file_path = "my_app_log.txt"
automation.create_file(log_file_path, "Uygulama başlatıldı: " + time.ctime())

# Örnek: Windows'ta belirli bir uygulamayı başlat (örn. Hesap Makinesi)
if automation.is_windows():
    print("Hesap Makinesi başlatılıyor...")
    calc_pid = automation.start_application("calc.exe", wait=False)
    if calc_pid:
        print(f"Hesap Makinesi PID: {calc_pid}")
        time.sleep(5)
        automation.stop_process_by_pid(calc_pid)
        print("Hesap Makinesi kapatıldı.")
elif automation.is_linux() or automation.is_macos():
    print("Terminal uygulaması açılıyor (örneğin 'xterm' veya 'Terminal.app')...")
    # Linux için 'xterm', macOS için 'open -a Terminal'
    terminal_command = "xterm" if automation.is_linux() else "open"
    terminal_args = []
    if automation.is_macos():
        terminal_args = ["-a", "Terminal"]

    terminal_pid = automation.start_application(terminal_command, args=terminal_args, wait=False)
    if terminal_pid:
        print(f"Terminal PID: {terminal_pid}")
        time.sleep(5)
        automation.stop_process_by_pid(terminal_pid)
        print("Terminal kapatıldı.")


        
