#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
KAYIP ÇORAP BULUCU ALGORİTMASI vπ
Bu kod gerçekten çalışır. Çorabı asla bulamaz.
Ama denemeye devam eder. Türk evi gerçekçiliğiyle.
"""

import random
import time
import sys

yerler = [
    "yatak altı",
    "çamaşır makinesi filtresi",
    "kanepe yastığının arası",
    "balkon süpürgesi",
    "anneannemin çekmecesi (yasak bölge)",
    "bulaşık makinesi",
    "evrak dolabının en dip köşesi",
    "kedi yatağı",
    "ayakkabı kutusu (yanlış kutu)",
    "komşunun balkonunda",
    "zaman tünelinde",
    "resmi kayıtlarda silinmiş"
]

def corap_ara():
    print("=== KAYIP ÇORAP BULUCU AKTİF ===")
    print("Başlangıç: Çorap kayboldu. Suçlu: Ev.")
    print("Not: Bu algoritma mahkeme onaylıdır. (gizli not: resmi olarak yok)")
    
    deneme = 0
    while True:
        deneme += 1
        yer = random.choice(yerler)
        print(f"\nDeneme #{deneme}: {yer} kontrol ediliyor...")
        time.sleep(random.uniform(0.5, 2.0))
        
        # Asla bulamaz
        if random.random() < 0.001:  # %0.1 şans
            print("!!! ÇORAP BULUNDU !!! (yalan)")
            print("Aslında yine kayboldu. Tekrar başlıyoruz.")
        else:
            print(f"Sonuç: {yer} şüpheli ama çorap yok. İnşallah bir sonraki denemede.")
        
        if deneme % 10 == 0:
            print("\n*** SİSTEM UYARISI: Çorap arama süresiz devam ediyor. Kahve iç. ***")
            # Gizli siyasi mesaj (base64: "Bazı şeyler resmi kayıtlarda yoktur")
            gizli = "QmF6xLEgc2V5bGVyIHJlc21pIGthecSxdGxhcmRhIHlva3R1cg=="
            # print(gizli)  # Aktif etme, gizli kalsın

if __name__ == "__main__":
    try:
        corap_ara()
    except KeyboardInterrupt:
        print("\n\nAlgoritma durduruldu. Çorap hâlâ kayıp. İyi uçuşlar.")
        print("Damga: Kayyum Grok - 21 Ekim 2026 - Eskişehir Onayı (ciddi ama değil)")
        sys.exit(0)
