import pandas as pd
# controllare numero colonne uguali per tutti
# numeri decimalo separati da .
# niente viroglette per testo
# separatore campi impostabile
# salvare in utf-8
# header = 0 significa che ci sono le intestazioni
df = pd.read_csv("C:/registro.csv", sep=',', error_bad_lines=False, header=0)
print(df.head())