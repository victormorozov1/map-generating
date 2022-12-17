# map-generating

This code can generate a random map.

```
git clone https://github.com/victormorozov1/map-generating.git
cd map-generating
python main.py
```

Possible command line args:
1) ```-s={your size}``` or ```--size={your size}```. Size must be the power of two
2) ```-c``` or ```--clouds```
3) ```-nw``` or ```--no_water_around```

## Examples
```cmd
python main.py -s=8192
```
![alt text](/map_results/50_map.png)
---
```cmd
python main.py -s=1024 -c -nw
```
![alt text](/map_results/51_map.png)
---
```cmd
python main.py
```

![alt text](/map_results/52_map.png)
---
You can see more examples in ```map_results``` folder
