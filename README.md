# droneFinder

## Repositório destinado a ajudar você, fpvzeiro raiz, que montou seu droninho e estava voando lindamente por cima de um matagal, quando do nada perdeu o sinal e ele caiu no meio do mato.



Com a ajuda de um drone comercial, por exemplo, um Mavic, sobrevoe e grave a região da queda. Mude as definições de cor HSV no código, que ao executar, todos os frames nos quais a cor foi detectada serão salvos na pasta ./frames, facilitando sua busca!


Clone o repositório:
```bash
git clone https://github.com/Luidooo/droneFinder.git
```
Ache o range dos valores HSV para a cor da sua hélice e os coloque no código (linha 61 e 62):

```python
#Mude os valores de x,y,z
lower_color = np.array([x1, y2, z1]) 
upper_color = np.array([x2, y2, z2])
```
Execute no terminal:
```python
python3 droneFinder.py ~/path/ate/seu/video.mp4
```
Boa sorte aos amantes de hélices verdes!

<img src="https://raw.githubusercontent.com/Luidooo/droneFinder/main/img/Drone.png" alt="Drone" width="400" height="500">
