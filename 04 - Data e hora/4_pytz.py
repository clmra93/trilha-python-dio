from datetime import datetime

import pytz

data = datetime.now(pytz.timezone("Europe/Oslo"))
data2 = datetime.now(pytz.timezone("America/Sao_Paulo"))
data3 = datetime.now(pytz.timezone("US/Eastern"))
                                    # Encontra a info de região na documentação.
print(data)
print(data2)
print(data3)