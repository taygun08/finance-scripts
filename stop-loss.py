# atr değerini baz alaraktan stop-loss hesaplamak için hızlı bir yol. hesaplanan değerin biraz daha altına koymanızı öneririm.
# atr tradingview indikatör kısmına yazarsanız ortalama gerçek aralık diye karşınıza çıkar.
# kendi kullandığım yöntemdir.
# stop tavsiyesi değildir :D

print("Created By Taygun Fırıncı")
buy = float(input("alım sinyali noktasını giriniz: "))
ath = float(input("atr değerini giriniz: "))
print("stop-loss: ", buy-atr*2)
