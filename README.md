# droneFinder

## Repositorio destinado a ajudar voce, fpvzeiro raiz, que montou seu droninho e tava voando lindamente por cima de um matagal, quando do nada perdeu sinal e ele caiu no meio do mato


Com ajuda de um drone comercial, por exemplo, um mavic, sobrevoee grave a regiao da queda, mude as definicoes de cor hsv no codigo, que ao executar, todo os frames da qual a cor foi detctada sera salvo na pasta ./frames, facilitando sua busca!


Clone o Repositorio:
```bash
git clone https://github.com/Luidooo/droneFinder.git
```
Ache os range dos valores hsv para a cor da sua helice e os coloque no codigo (linha 61 e 62):
```python
#Mude os valores de x,y,z
lower_color = np.array([x1, y2, z1]) 
upper_color = np.array([x2, y2, z2])
```
Execute no terminal:
```python
python3 droneFinder.py ~/Path/Ate/seu/video.mp4
```
Boa sorte aos amantes de helices verdes!
