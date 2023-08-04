times = ('PALMEIRAS','INTERNACIONAL','FLAMENGO','FLUMINENSE','CORINTHIANS','ATHLETICO-PR',
         'ATLÉTICO-MG','AMERICA-MG','FORTALEZA','BOTAFOGO','SANTOS','SÃO PAULO','BRAGANTINO',
         'GOIÁS','CORITIBA','CEARÁ','CUIABÁ','ATLETICO-GO','AVAÍ','JUVENTUDE')
print(f'Os quatros primeiros colocados são\n{times[:4]}')
print(f'Os quatros ultimos colocados são\n{times[-4:]}')
print(f'O São Paulo está na {times.index("SÃO PAULO")} colocação')
print(f'Times em ordem alfabetica:\n{sorted(times)}')